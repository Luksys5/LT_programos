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

rez Potential(vector<double> coord, vector<double> mass, vector<double> &speed)
{
	double Vlj, distab;
	double eps = 1;
	rez koord_sp;
	double sigma = 0.01;	
	double F, v, a, s;
	double delta_t = 0.01;
	vector< vector<double> > coords;
	for(int i = 0; i < coord.size(); i++)
	{
		vector<double> col;
		coords.push_back(col);
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
					//cout << i << ' ' << j << ' ';
					if(coord[i] < coord[j])
						distab = 1 - coord[j] + abs(-1 - coord[i]);
					else
						distab = 1 - coord[i] + abs(-1 - coord[j]);
				
					if(distab > abs(coord[i] - coord[j]))
						distab = abs(coord[i]-coord[j]);

					Vlj = 4*eps*( pow(sigma/distab, 12) - pow(sigma/distab, 6) ); 
					F += Vlj/distab;
				}
			}
			coords.at(i).push_back(coord[i]);
			a = F/mass[i];	
			v = speed[i] - a*delta_t;
			s = coord[i] + (speed[i]*delta_t) + (a*delta_t*delta_t)/2;
			if(coord[i] >= 1.0)
				coord[i] = coord[i] - 2;
			speed[i] = v; coord[i] = s;
			F = 0;
			for(int j = 0; j < coord[i].size(); i++)
				cout << coord[j] << "\t" << speed[i] << "\t";
		}
		cout << "\n";
	}
	
	return koord_sp;
}


int main()
{
	int time = 100;
	info all = input();
	rez data;

	/*freopen("output", "w", stdout);
	for(int i = 0; i < all.coord.size(); i++)
		cout << "koord" << i << "\t" << "speed" << i << "\n";

	for(int i = 0; i < all.coord.size(); i++)
	coordinates = Potential(all.coord, all.weight, all.speed);{
		if(i==0)
			cout << "koord speed" << "\n";
		cout << all.coord[i] << ' ' << all.speed[i]  << "\n";
	
	}*/
	data = Potential(all.coord, all.weight, all.speed);
	//fclose(stdout);
	//system("./Rgraph output");
	//system("evince Rplots.pdf");

	/*
	cout << "M1\tM2\tM3\tM4\n";
	for(int j = 0; j < coordinates.at(0).size(); j++)
		cout << coordinates[0][j] << "\t" << coordinates[1][j] << "\t" << coordinates[2][j] << "\t" << coordinates[3][j] << "\n";
	*/
}
