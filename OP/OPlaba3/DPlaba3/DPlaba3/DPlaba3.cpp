#include<iostream>
#include<cstdlib>
#include<cmath>
#include<float.h>
using namespace std;

int main()
{
	// Declaring all needed variables
	double x;
	long double sum = 0;
	long double a = 1;
	double b;
	long double pow1;
	long double sin1;
	cout << "Enter x (x belongs (-2;2)): " << endl;
	cin >> x;
	if (-2 < x and x < 2)
	{
		int k = 10;
		while (abs(a) >= 0.0001)
		{
			k++;
			pow1 = pow(x, k);
			sin1 = sin(pow1);
			a = (pow(x, 2 * k) * sin1) / (pow(k, 2));
		}
		int i = 0;
		while (i < k)
		{
			i++;
			pow1 = pow(x, i);
			sin1 = sin(pow1);
			b = (pow(x, 2 * i) * sin1) / (pow(i, 2));
			sum = sum + b;
			cout << i << endl << sum << endl;
		}
		cout <<"The sum is: "<< sum << endl;
	}
	else
	{
		cout << "Error" << endl;
	}
	system("pause");
	return 0;
}