#include<iostream>
#include<cstdlib>
#include<cmath>
#include<float.h>
using namespace std;

int main()
{
	double a = 0;
	double b = 0;
	double c = 1.5;
	double d = 0;
	int n;
	cout << "Enter n (n>=4):";
	cin >> n;
	if (n < 4)
	{
		cout << "Error";
	}
	else
	{
		for (long int i=4; i <= n; i+=1)
		{
			d = (i + 1) / (pow(i, 2) + 1) * c - a * b;
			a = b;
			b = c;
			c = d;
			cout << d << endl;
		}
		cout << "Speed is:" << d << endl;
	}
	return 0;
	system("pause");
}