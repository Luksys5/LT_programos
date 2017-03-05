#include <stdio.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

struct map_bool
{
	vector< vector<int> > m1;
	bool check;
};

void output_Labirinth(vector< vector<int> > LAB, int maxval, int size, string tarp, string del, bool on)
{
	float mkiek = (float)maxval; 
	int mtarp = 1;
        while(mkiek > 1)
        {
                mkiek = mkiek / 10;
                mtarp++;
        }
	
	cout << "   ^\n";
	for(int i = 0; i < size; i++)
        {
                if(size - i < 10)
                        cout << size - i << "  |  ";
                else
                        cout << size - i << " |  ";
	
                int index = 0;

                for(int j = 0; j < LAB[i].size(); j++)
                {
			
			//if(on)
			if(LAB[size - i - 1][j] > 9)
				cout << LAB[size - i - 1][j] << "  ";
			else
				cout << LAB[size - i - 1][j] << "   ";
			//else
			//cout << " " << LAB[i-1][j] << " ";
		
                }cout << "\n";
        }
        cout << "   ";

        for(int j = 0; j < size; j++)
                cout << "-----";
        cout <<  "--> X\n";

        cout << tarp;
        for(int j = 1; j < size + 1; j++)
        {
                if(j > 9)
                        cout << j << del;
                else
                        cout << j << del + " ";
        }
        cout << "\n";
}

bool eiti(vector< vector<int> > &LAB,vector< vector<int> > &newmap, vector<int> CX, vector<int> CY,
	int N, int M, int &X, int &Y, int &BANDSK, int &L, bool YRA, int &max, vector<pair<int, int> > &coord, string tarp, vector<string> &rod, vector<int> RV)	
{
	int K, U, V;
	int size = LAB.size();
	max = LAB[Y][X];
	//newmap[Y][X] = max;
	//cout << "X: " << X << " Y: " << Y << "\n";
	if(X == 0 || X == (M-1) || Y == 0 || Y == (N-1))
	{
		YRA = true;
		return YRA;
	}else
	{
		K = 0;
		while(YRA != true && K < 4)
		{
			U = X + CX[K];
			V = Y + CY[K];
			//cout << V + 1  << ' ' << U + 1 << "\n";
			string R = "R" + to_string(RV[K]);
			cout << tarp << R << ": X=" << U + 1 << " Y=" << V + 1;

			if(LAB[V][U] == 1)
				cout << " Siena";
			else if(LAB[V][U] != 0)
				cout << " Siulas"; 
			cout << "\n";	

			if(LAB[V][U] == 0)
			{
				rod.push_back(R);
				coord.push_back(make_pair(U + 1, V + 1));
				BANDSK++;
				if( L < 2 )
					L = 2;
				L++;
				//if(V == 4 && U == 4)
				//	L += 2;
				newmap[V][U] = L;
				LAB[V][U] = L;
				YRA = eiti(LAB, newmap, CX, CY, N, M, U, V, BANDSK, L, YRA, max, coord, tarp + "  ", rod, RV);
				if(YRA != true)
				{
					rod.pop_back();
					coord.pop_back();
					LAB[V][U] = 0;
					L--;
					if( L < 2) 
						L = 2;
				}
				
			}
			K++;
		}
	}
	return YRA;
}

int main(int argc, char* argv[])
{
	ifstream fh(argv[1]);
	vector< vector<int> > map;
	vector<int> info;
	int BANDSK = 0;
	int L = 2;
	int sk, X, Y, maxas;
	bool siena = true;
	bool yra = false;
	vector<string> rod;
	vector< pair<int, int> > coord;
	
	while(fh >> sk)
	{
		info.push_back(sk);
	}
	
	int size = sqrt(info.size());
	for(int i = 0; i < size; i++)
	{
		vector<int> col;
                map.push_back(col);
	}
	
	for(int i = 0; i < size; i++)
	{
		
		for(int j = 0; j < size; j++)
		{
			map[size - 1 - i].push_back( info[(i*size) + j] );
		}
	}
	
	int N = map.size(); int M = map[0].size();	
	vector<int> rv = {2, 1, 3, 4};
	//vector<int> cy = {1, -1, 0, 0};
	//vector<int> cx = {0, 0, 1, -1};
	//vector<int> cx = {0, -1, 0, 1, };
	//vector<int> cy = {-1, 0, 1, 0, };
	vector<int> cy = {-1, 0, 0, 1 };
        vector<int> cx = {0, -1, 1, 0 };
	cout << "1. Labirintas\n\n";
	output_Labirinth(map, 1, size, "      ", "  ", false);
	while(siena)
	{
		cout << "\nIveskite pradines X, Y koordinates\n";
		cin >> X; cin >> Y;
		X -= 1;
		Y -= 1;
		cout << "X: " << X << "\n";
		cout << "Y: " << Y << "\n";
		cout << map[Y][X] << "\n";
		if(map[Y][X] != 1)
			siena = false;
		else
			cout << "Rasta siena kartojama iš naujo\n";
	}
	int pradX = X;
	int pradY = Y;
	cout << "\n";
	map[Y][X] = L;
	L = 3;
	vector< vector<int> > newmap = map;
	//output_Labirinth(map, 1, size, "     ", " ", true);
	bool ats = eiti(map, newmap, cx, cy, N, M, X, Y, L, BANDSK, yra, maxas, coord, "", rod, rv);
	cout << "\n\n";
	if(ats)
		cout << "3.1 Kelias egzistuoja\n\n";
	else
	{
		cout << "3.1 Kelias neegzistuoja\n\n";
		output_Labirinth(newmap, 1, size, "      ", "  ", false);
		return 0;
	}
	cout << "3.2 Kelias pagal rodykles\n";
	
	for(int i = 0; i < rod.size(); i++)
	{
		cout << rod[i] << "; ";
		if((i+1) % 6 == 0)
			cout << "\n";
	}cout << "\n\n";

	
	cout << "3.3 Kelias pagal virsunes\n";
	
	int last = coord[0].second;
	cout << "["<< pradX + 1 << ", " << pradY + 1 << "];  ";
	for(int i = 0; i < coord.size(); i++)
	{
		cout << "[" << coord[i].first <<", " << coord[i].second << "];  ";
		if((i+1) % 6 == 0)
			cout << "\n";
	}cout << "\n";

	cout << "\n3.4 Kelias pagal Labirinta\n   Y\n";
	//output_Labirinth(newmap, maxas, size, "      ", "  ", false);	
	output_Labirinth(newmap, 1, size, "      ", "  ", false);

	return 0;

}
