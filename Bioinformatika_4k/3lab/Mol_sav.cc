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
	}
	
	for(int t = 0; t < 10000; t++)
	{	
		for(int i = 0; i < coord.size(); i++)
		{
			Vlj = 0;
			for(int j = 0; j < coord.size(); j++)
			{
				if(j != i)
				{
					distab = coord[j] - coord[i];
					distab2 = coord[j] + ( 1 - coord[i] );
								
					if(abs(distab2) < abs(distab))
						distab = distab2;
		
					Vlj = 4*eps*( pow(sigma/distab, 12) - 
						pow(sigma/distab, 6) );
					//F += -24*eps*(2*( pow(sigma, 12)/pow(distab, 13) ) - (pow(sigma, 6) - pow(distab, 7)) );
					F += Vlj/distab;
				}
			}
			Force[i] = F;
			F = 0;
		}
		for(int i = 0; i < coord.size(); i++)
                {
                        if(coord[i] > 1.0)
                                coord[i] = coord[i] - 1;
                        else if(coord[i] < 0.0)
                                coord[i] = 1 + coord[i];
                        cout << coord[i] << ' '; //*1855 << ' ';
                }
		for(int i = 0; i < coord.size(); i++)
		{
			
			a = Force[i]/mass[i];
                        v = a * delta_t + speed[i]; 
                        s = coord[i] + v*delta_t;
                        speed[i] = v; coord[i] = s;
		}
		cout << "\n";
	}
	
	
}


int main()
{
	info all = input();
	Potential(all.coord, all.weight, all.speed);
}
