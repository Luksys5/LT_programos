#include <stdio.h>
#include <stdlib.h>
#include <utility>
#include <algorithm>
#include <tuple>
#include <math.h>
#include <string.h>
#include <vector>
#include <fstream>
#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <ctime>
#include <cstdlib>
using namespace std;

bool exist(int x, vector<int> arr)
{
	for(int i = 0; i < arr.size(); i++)
		if(x == arr[i])
			return true;
	
	return false;
}

void cosx_gen()
{
	srand(time(NULL));  // Changing randomizing each time
	vector<int> poz;
	ofstream fw;
	fw.open("in_Lagrange");
	float random;
	for(int i = 0; i < 10; i++)
	{	
		random = int(10*abs(5 * rand() / (RAND_MAX + 1.0)));
		while(exist(random, poz))
			random = int(10*abs(5 * rand() / (RAND_MAX + 1.0)));
		poz.push_back(random);
	}
	int belong = 0; 
	for(int i = 0; i < poz.size(); i++)
		for(int j = 0; j < poz.size(); j++)
		{
			if(belong == poz[j])
			{
				fw << j << "\n";
				belong++;
				break;
			}		


		}
	fw.close();
}

vector<float> readNsort()
{
	vector<float> x_points;
	float nr;
	ifstream fh("in_Lagrange");

	// Reading input from 'test' file
	while(fh >> nr)
	{
		x_points.push_back(nr);
	} 
	
	// Sorting vector
	float tempx;
	for(int i = 0; i < x_points.size(); i++)
		for(int j = 0; j < i; j++)
		{
			if(x_points[j] > x_points[i])
			{
				tempx = x_points[j]; 
				x_points[j] = x_points[i];
				x_points[i] = tempx; 
			}
		}

	return x_points;

}

vector<float> nearby_points(float x, vector<float> x_given)
{
	vector<float> five_points;
	vector<int> added; int tempadd;
	vector<float> diffs; float tempdiff;
	for(int i = 0; i < x_given.size(); i++)
	{
		diffs.push_back(abs(x_given[i] - x));
		added.push_back(i);
	}

	for(int i = 0; i < x_given.size(); i++)
		for(int j = 0; j < i; j++)
			if(diffs[i] < diffs[j])
			{
				tempdiff = diffs[j]; tempadd = added[j];
				diffs[j] = diffs[i]; added[j] = added[i];
				diffs[i] = tempdiff; added[i] = tempadd;
			}
		
        for(int i = 0; i < 5; i++)
		five_points.push_back(x_given[added[i]]);
	return five_points;
}

int main()
{
	cosx_gen();  			// Random number generator
	vector<float> five;
	vector<float> x_points = readNsort();
	ofstream fw; fw.open("out_Lagrange");
	if(x_points.size() < 5)
	{
		cout << "duota per mazai tasku\n";
		return 0;	
	}
	
	int N = x_points.size() - 1; 
	float x_min = x_points[0]; float x_max = x_points[N];
	int Nkv = (N+1)*(N+1);
	float L_sum, L_now, x, sand, dalb;
	fw << 'x' << "\t" << 'y' << "\n";	
	
	for(int j = 0; j < Nkv; j++)
	{
		x = x_min + (float)(j - 1)*((float)(x_max- x_min))/((float)Nkv);
		five = nearby_points(x, x_points);
		
		L_sum = 0.0;
		for(int i = 0; i < five.size(); i++)
		{
			sand = 1; dalb = 1;
			for(int k = 0; k < five.size(); k++)
				if(i != k)
				{
					sand *= ((float)x - (float)five[k]);
					dalb *= ((float)five[i] - (float)five[k]);
				}

			if(dalb != 0.0)
			{
				L_now = (float)(sand)/(float)(dalb);
				L_sum += L_now * cos(2*five[i]);
			}
		}
		fw << x << "\t" << L_sum << "\n";	
		//break;
	}
	return 0;
}
