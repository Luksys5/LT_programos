#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main()
{
	float v_st = 0;
	int cc = 0;
	float delta_t = 0.01;
	float a = -1;
	float s, s_last, v_now;
	for(int t = 0; t < 100; t++)
	{
		v_now = v_st + a*delta_t;
		s = s_last + v_st * delta_t + a*delta_t*delta_t/2;//v_gal = v_prad + a*delta_t;
		v_st = v_now;
		s_last = s;
		
		cc++;
		cout << cc << " kelias: " << s_last << "\n"; 
	}
	v_st = 0;
	v_now = v_st + a*1;
	float kelias = (v_st + v_now)*1/2;
	cout << kelias << "\n";
	return 0;
}
