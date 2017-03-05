#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

#define fori(endi) for(int i = 0; i < endi; i++)
#define forj(endj) for(int j = 0; j < endj; j++)

using namespace std;

void labirinto_isvedimas(int **labirintas, int n, int m) {

	cout << "  y" << endl;
	cout << "  ^" << endl;
	fori(n) {
		cout << setw(2) << n - i << "|";
		forj(m) {
			cout << setw(4) << labirintas[i][j];
		}
		cout << endl;
	}

	cout << "  ";
	forj(m) {
		cout << "----";
	}
	cout << "---> x" << endl << "   ";
	forj(m) {
		cout << setw(4) << j + 1;
	}

	cout << endl;

}

int main(int argc, char* argv[])
{
	//failo nuskaitymas
	string baigti = "";
	while (baigti.compare("n")) {

		int **labirintas, **labirintas_kopija,
			*fx, *fy;
		int n, m, x, y;

		ifstream file;
		file.open(argv[1]);

		file >> n >> m;

		labirintas = new int*[n];
		labirintas_kopija = new int*[n];
		fx = new int[n * m];
		fy = new int[n * m];

		fori(n) {
			labirintas[i] = new int[m];
			labirintas_kopija[i] = new int[m];
		}

		fori(n) {
			forj(m) {
				file >> labirintas[i][j];
				labirintas_kopija[i][j] = labirintas[i][j];
			}
		}

		file.close();

		//labirinto_isvedimas(labirintas, n, m);

		labirinto_isvedimas(labirintas_kopija, n, m);
		cout << "Iveskite zmogaus padeti: ";
		cin >> y >> x;
		cout << endl;

		x = n - x;
		y --;

		labirintas_kopija[x][y] = 2;

		//labirinto_isvedimas(labirintas_kopija, n, m);
		// produkcijos

		int *cx = new int[4],
			*cy = new int[4];

		cy[0] = -1; cx[0] = 0;
		cy[1] = 0; cx[1] = 1;
		cy[2] = 1; cx[2] = 0;
		cy[3] = 0; cx[3] = -1;

		// pradines reiksmes kintamiesiems

		fx[0] = x;
		fy[0] = y;
		int uzd = 0, nauja = 0,
			sena_banga = 0, nauja_banga;
		bool yra = false;

		// algorithm
		int u = x, v = y;

		if (x == 0 || x == n - 1 || y == 0 || y == m - 1) 
			yra = true;
		else {
			do {
				x = fx[uzd];
				y = fy[uzd];
				nauja_banga = labirintas_kopija[x][y] - 1;

				cout << uzd + 1 << ". Uzdaroma x=" << y + 1 << " y=" << n - x << "." << endl;
				if (sena_banga < nauja_banga) {
					cout << "    Bus banga nr=" << nauja_banga << ", zyme '"
						<< nauja_banga + 2 << "'." << endl;
					sena_banga = nauja_banga;
				}
				//labirinto_isvedimas(labirintas_kopija, n, m);

				int k = 0;
				do {

					cout << "      ";
					if (k == 0)
						cout << "R1. ";
					else if (k == 1)
						cout << "R2. ";
					else if (k == 2)
						cout << "R3. ";
					else
						cout << "R4. ";

					u = x + cx[k];
					v = y + cy[k];
					

					cout << "x=" << v + 1 << " y=" << n - u ;

					if (labirintas_kopija[u][v] == 0) {	
						labirintas_kopija[u][v] = labirintas_kopija[x][y] + 1;
						cout << ", atidaroma=" << nauja + 2 << ".";
						if (u == 0 || u == n - 1 || v == 0 || v == m - 1) {
							yra = true;
						}
						else {
							nauja++;
							fx[nauja] = u;
							fy[nauja] = v;
						}

						
					}
					else
						cout << ", siena.";
					cout << endl;
					k++;
				} while (k < 4 && !yra);
				uzd++;
				
				//cout << x << " " << y << endl;
			} while (uzd <= nauja && !yra);
		}

		// atgal

		vector<string> rodykles, koordinates;

		int k = 0, uu, vv;

		labirintas[u][v] = labirintas_kopija[u][v];
		koordinates.push_back("[x=" + to_string(v + 1) + ", y=" + to_string(n - u) + "]");
		do {
			uu = u + cx[k];
			vv = v + cy[k];

			if (uu > 0 && uu < n && vv > 0 && vv < m)
				if (labirintas_kopija[uu][vv] == labirintas_kopija[u][v] - 1) {
					labirintas[uu][vv] = labirintas_kopija[uu][vv];

					if (k == 0)
						rodykles.push_back("R1");
					else if (k == 1)
						rodykles.push_back("R2");
					else if (k == 2)
						rodykles.push_back("R3");
					else
						rodykles.push_back("R4");

					u = uu;
					v = vv;
					k = 0;

					koordinates.push_back("[x=" + to_string(v + 1) + ", y=" + to_string(n - u) + "]");
				}

			k++;
		} while (labirintas_kopija[u][v] != 2);
		cout << endl;

		// rezultatas
		
		if (yra) {
			cout << "Kelias egzistuoja." << endl;
		}
		else
			cout << "Kelias neegzistuoja" << endl;

		cout << endl << "Kelias pagal labirinta." << endl;
		labirinto_isvedimas(labirintas, n, m);

		//isvedimas

		cout << endl << "Kelias pagal rodykles.";
		int ind = 0;
		for (int i = rodykles.size() - 1; i > -1; i--) {
			if (ind++ % 5 == 0)
				cout << endl;
			cout << rodykles[i] << " ";
		}
		cout << endl;

		cout << endl << "Kelias pagal koordinates.";
		ind = 0;
		for (int i = koordinates.size() - 2 ; i > -1 ; i--) {
			if (ind++ % 5 == 0)
				cout << endl;
			cout << koordinates[i] << " ";
		}
		cout << endl;

		//atminties valymas

		fori(n) {
			delete[] labirintas[i];
			delete[] labirintas_kopija[i];
		}
		delete[] labirintas;
		delete[] labirintas_kopija;

		delete[] fx;
		delete[] fy;
		delete[] cx;
		delete[] cy;

		cout << endl;
		baigti="n";	
	}
	return 0;
}



