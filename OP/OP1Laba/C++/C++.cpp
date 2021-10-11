#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;

int main()
{
	// Initializing all needed variables
	double a, b, c;
	// Getting all needed inputs
	cout << "Enter the value of hypotenuse:";
	cin >> c;
	cout << "Enter the value of leg:";
	cin >> a;
	// Calculating values of the sides
	b = sqrt(pow(c, 2) - pow(a, 2));
	// Outputting the answers
	printf("The second leg: %f\n", b);
	system("pause");
}