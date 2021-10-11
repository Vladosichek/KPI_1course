#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	// Declaring all needed variables
	double a1;
	double b1;
	double c1;
	double a2;
	double b2;
	double c2;

	// Getting all needed inputs (a1x+b1y=c1; a2x+b2y=c2)
	cout << "Getting all needed inputs (a1x+b1y=c1; a2x+b2y=c2)";
	cout << "Enter a1 ";
	cin >> a1;
	cout << "Enter b1 ";
	cin >> b1;
	cout << "Enter c1 ";
	cin >> c1;
	cout << "Enter a2 ";
	cin >> a2;
	cout << "Enter b2 ";
	cin >> b2;
	cout << "Enter c2 ";
	cin >> c2;

	// Cheking ammount of solutions
	if (a1 / a2 - b1 / b2 == 0)
	{
		if (b1 / b2 - c1 / c2 == 0)
		{
			cout << "There is an infinite ammount of solutions of the system";
		}
		else
		{
			cout << "There is no solution of the system";
		}
	}
	else
	{
		cout << "There is one solution of the system";
	}
}