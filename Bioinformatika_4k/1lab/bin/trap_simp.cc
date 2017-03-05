#include <string>
#include <math.h>
#include <iterator>
#include <vector>
#include <iostream>
#include <stdlib.h>
using namespace std;

void print_arr(std::vector<double> vect1, std::vector<double> vect2)
{
	cout << "Trap\tSimpson\n";
	for(int i = 0;i != vect2.size();i++)
		cout << vect1[i] << "\t" << vect2[i] << "\n";
	
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
		//cout << "rez\t" << rez.back() << "\n";
	}
	return rez;
}

std::vector<double> Simpson(float st, float end, float step)
{
        std::vector<double> rez;
        double sum;
        for(float alfa = 0; alfa < 1-0.01; alfa += 0.01)
        {
                sum = 0;
		int z = 0;
                for(double j = st+step; j < end-step; j += step)
		{
			if(z % 2 == 0){
				sum += 4*pow( 2-j, alfa*j );
			}else
				sum += 2*pow( 2-j, alfa*j ); 
			z+= 1;
		}
		double First = pow(2-st, alfa*st);
		double Last = pow(2-end, alfa*end); 
		rez.push_back( (step/3)*( pow(2-st, alfa*st)
                                + pow(2-end, alfa*end) + sum) );	
        }
        return rez;
}

int main()
{
	float a = -1; float b = 1; int N = 100;
	float h = (b-a)/N;
	std::vector<double> trap;
	std::vector<double> simp;
	trap = Trapec(a, b, h, N);
	simp = Simpson(a, b, h);
	print_arr(trap, simp);	
	return 0;
}
