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

bool back(vector< vector<int> > &LAB,vector< vector<int> > &newmap, vector<int> CX, vector<int> CY,
		int Krast, int &X, int &Y)	
{
	int K, U, V;
	int size = LAB.size();
	LAB[V][U] = newmap[V][U];
	K = 0;
	do
	{
		K++;
		U = X + CX[K];
		V = V + CY[K];
		if((0 <= U) && ( U <= Krast - 1 ) && (0 <= V) && (V <= Krast - 1))
			if(newmap[V][U] == newmap[Y][X] - 1);
			{
				LAB[V][U] = newmap[V][U];
				X = U; Y = V;
				K = 0;
			
			}

	}while( newmap[V][U] == 2 );
}

bool wave(vector< vector<int> > &LAB,vector< vector<int> > &newmap, vector<int> CX, vector<int> CY, 
		vector<int> &ROD, vector<int> &COORD, int Krast, int &X, int &Y, 
		vector<int> &FX, vector<int> &FY, int &NAUJA, bool &YRA, int &UZD)
{
	int K;
	int U = X; int V = Y;
	cout << X << ' ' << Y << ' ' << Krast << ' '<< LAB.size() << "\n";
	if((X == 0) || (X == Krast - 1) || (Y == 0) || (Y == Krast - 1))
	{
		YRA = true;
	} 
	else
	{
		do
		{
			X = FX[UZD]; Y = FY[UZD];
			cout << "Uzdaroma " << "X=" << X + 1 << " Y=" <<  Y + 1 << "\n";
			cout << "\tBus banga nr." << UZD + 1 << " zyme " << NAUJA << "\n";
			K = 0;
			do
			{	
				U = X + CX[K];
				V = Y + CY[K];
				cout << "\t R" << K + 1 << ".  X=" << U + 1 << "  Y=" << V + 1;
					
				if(newmap[V][U] == 0)
				{
					//string R = "R" + (K + 1).toString();
					ROD.push_back(K + 1);
					cout << ", Atidaroma = " << NAUJA + 1 << "\n";
					newmap[V][U] = newmap[Y][X] + 1;
					
					if( (U == 0) || (U == Krast - 1) || (V == 0) || (V == Krast - 1) )
						YRA = true;
					else
					{
						NAUJA++;
						if(NAUJA == FX.size())
						{
							FX.push_back(U);
							FY.push_back(V);
						}
						else
						{
							FX[NAUJA] = U; 
							FY[NAUJA] = V;
						}
		
					}
					
				}
				else if(newmap[V][U] == 1)
					cout << ", Siena\n";
				else
					cout << ", Siulas\n";
				K++;

			}while( (K < 4) && (YRA != true) );
			UZD++;

		}while( (UZD < NAUJA + 1) && (YRA != true) );
	}	
	int UU, VV;
	int size = LAB.size();
	LAB[V][U] = newmap[V][U];
	K = 0;
	do
	{
		UU = U + CX[K];
		VV = V + CY[K];

		if((0 <= UU) && ( UU <= Krast - 1 ) && (0 <= VV) && (VV <= Krast - 1))
			if(newmap[VV][UU] == newmap[Y][X] - 1);
			{
				LAB[VV][UU] = newmap[VV][UU];
				U = UU; V = VV;
				K = 0;

			}
		K++;
	}while( newmap[V][U] != 2 );
}

void read_initmap(vector<int> allarr, vector< vector<int> > &outmap, char* file, vector<int> &FX, vector<int> &FY)
{
	ifstream fh(file);
	int sk;
	
	fh >> sk;
	fh >> sk;
	while(fh >> sk)
	{
                allarr.push_back(sk);
		FX.push_back(0);
		FY.push_back(0);
	}
	int size = sqrt(allarr.size());

	vector<int> col;
	for(int i = 0; i < size; i++)
		outmap.push_back(col);	
	
	for(int i = 0; i < size; i++)
                for(int j = 0; j < size; j++)
			outmap[size - 1 -i].push_back(allarr[(i*size) + j]);
	
}

int main(int argc, char* argv[])
{
	vector< vector<int> > map;
	vector<int> info;
	vector<int> fx; vector<int> fy;
	vector<int> cy = {-1, 0, 1, 0 };
        vector<int> cx = {0, -1, 0, 1 };

	int X, Y;
	read_initmap(info, map, argv[1], fx, fy);

	int Kr = map.size(); 
        bool yra = false;
	int NeW = 0;
	int Uzd = 0;

	if(map.size() < 1)
		cout << "empty\n";
	
	cout << "1. Labirintas\n\n";
	output_Labirinth(map, 1, map.size(), "      ", "  ", false);
	bool siena = true;
	while(siena)
	{
		cout << "\nIveskite pradines X, Y koordinates\n";
		cin >> X; cin >> Y;
		X -= 1;
		Y -= 1;
		cout << "X: " << X << ' ' << "Y: " << Y << "\n";
		if(map[Y][X] != 1)
			siena = false;
		else
			cout << "Rasta siena kartojama iš naujo\n";
	}cout << "\n";
	fx[0] = X; fy[0] = Y;
	vector< vector<int> > newmap = map;
	output_Labirinth(map, 1, map.size(), "      ", "  ", true);
	vector<int> rod; vector<int> coord;
	//bool ats = false;
	bool ats = wave(map, newmap, cy, cx, rod, coord, Kr, X, Y, fx, fy, NeW, yra, Uzd);
	//system("Labirintas2.cpp labirintas")
	/*
	if(ats == true)
		cout << "Kelias egzistuoja\n";
	else
		cout << "Kelias neegzistuoja\n";
	output_Labirinth(map, 1, map.size(), "      ", "  ", true);
	for(int i = 0; i < fx.size(); i++)
	{
		if( fx[i] != 0 && fy[i] != 0)
			cout << fx[i] + 1  << ' ' << fy[i] + 1<< "\n";
	}
	//	cout << "R" << rod[i] << "\n";
	*/
}
