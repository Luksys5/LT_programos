#include <iostream>
using namespace std;

void hanoj(char b1, char b2, char b3, int n)
{
	static int perkelimu_sk = 1;
	if(n == 1)
	{
		cout << "Perkelimu skaičius: " <<  perkelimu_sk << "\n";
		perkelimu_sk++;
		cout << "Keliamas žiedas nuo " << b1 << " ant " << b2 << "\n";
	
	}else
	{
		hanoj(b1, b3, b2, n-1);
		hanoj(b1, b2, b3, 1);
		hanoj(b3, b2, b1, n-1);
	}
	
}

int main()
{
	int n;
	cout << "Nurodykite Hanojaus boksto ziedų skaičių\n";
	cin >> n;
	if(n)
		hanoj('A', 'C', 'B', n);
	else cout << "Neleistinas ziedu skaičius.\nNurodykite 1 ar daugiau\n";
	return 0;
}
