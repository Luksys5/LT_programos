#include <string>
#include <math.h>
#include <iterator>
#include <vector>
#include <iostream>
#include <stdlib.h>
using namespace std;

void print_arr(std::vector<double> vect)
{
	for(std::vector<double>::iterator i = vect.begin();i != vect.end();i++)
		cout << j << ' ' << *i << "\n";
}

std::vector<double> Trapec(float st, float end, float step, int quant)
{
	std::vector<double> rez;
	double sum;
	for(float alfa = 0; alfa < 1-0.01; alfa += 0.01)
	{
		sum = 0;
		for(int j = 1; j < quant; j++)
			sum += pow( 2-(st+j*step), alfa*(st+j*step) );
	
		rez.push_back( (step/2)*( pow(2-st, alfa*st) 
				+ pow(2-end, alfa*end) + sum*2) );
	}
	return rez;
}


int main()
{
	float a = -1; float b = 1; int N = 100;
	float h = (b-a)/N;
	std::vector<double> temp;
	temp = Trapec(a, b, h, N);
	print_arr(temp);	
	return 0;
}
