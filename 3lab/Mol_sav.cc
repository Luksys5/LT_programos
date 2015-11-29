#include <stdio.h>
#include <cmath>
#include <math.h>
#include <tuple>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

struct info
{
	vector<double> coord;
	vector<double> weight;
	vector<double> speed;
};

struct rez
{
	vector< vector<double> > coord;
	vector< vector<double> > speed;
};

info input()
{
	info all;
	ifstream file("molecules");
	double x, m, v;

	while(file >> x >> v >> m)
	{
		all.coord.push_back(x);
		all.speed.push_back(v);
		all.weight.push_back(m);
	}
	return all;	
}

void Potential(vector<double> coord, vector<double> mass, vector<double> &speed)
{
	double Vlj, distab, distab1, distab2;
	double eps = 1;
	rez koord_sp;
	double sigma = 0.01;	
	double F = 0.0;
	double v, a, s;
	double delta_t = 0.01;
	int to_print = 0;
	double which;
	vector<double> Force;
	
	for(int i = 0; i < coord.size(); i++){
		Force.push_back(0.0);
		cout << "koord" << i+1 << " speed" << i+1 << ' ';
	}
	cout << "\n";
	for(int t = 0; t < 100000; t++)
	{	
		for(int i = 0; i < coord.size(); i++)
		{
			/*
			if(t == 0)
			{
				for(int i = 0; i < coord.size(); i++)
					cout << coord[i] << ' ' << speed[i] << ' ';
				cout << "\n";
			}
			*/
			//if(t == 1)
			//	return;
			Vlj = 0;
			for(int j = 0; j < coord.size(); j++)
			{
				if(j != i)
				{
					distab = coord[j] - coord[i];
					distab2 = coord[j] + ( 1 - coord[i] );
					//if(coord[i] < coord[j])
					//	distab2 = 1 + coord[i] + ( 1 - coord[j] );
								
					if(abs(distab2) < abs(distab))
						distab = distab2;
					Vlj = 4*eps*( pow(sigma/distab, 12) - pow(sigma/distab, 6) ); 
					F += Vlj/distab;
					//cout << j << ' '<< distab << ' ' << Vlj << "\n";
				}
			}
			Force[i] = F;
			F = 0;
		}
		for(int i = 0; i < coord.size(); i++)
		{
			a = Force[i]/mass[i];
                        v = a * delta_t + speed[i]; 
                        //cout << coord[i] << ' ' << speed[i] << ' ' << F << ' ';       
                        s = coord[i] + v*delta_t;
                        speed[i] = v; coord[i] = s;
			cout << coord[i] << ' ' << speed[i] << ' ';

			if(coord[i] > 1.0)
                        {
                                to_print = 1;
                                which = coord[i];
                                coord[i] = 0.0;
                        }
                        else if(coord[i] < 0.0)
                        {
                                to_print = 1;
                                which = coord[i];
                                coord[i] = 1.0;
                        }

		}
		cout << "\n";
		/*
		cout << "\n";
		if( to_print == 1)
			cout << which << "\n";
		to_print = 0;
		*/
	}
	
	
}


int main()
{
	info all = input();
	Potential(all.coord, all.weight, all.speed);
}
