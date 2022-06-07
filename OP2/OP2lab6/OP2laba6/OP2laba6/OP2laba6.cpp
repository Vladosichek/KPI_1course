#include "Header.h"
#include <iostream>
#include <string>
using namespace std;
int main()
{
	string H;
	int q, c, it;
	Branch* Root = 0;
	cout << "Enter ammount of elements: ";
	cin >> it;
	for (int i = 0; i < it; i++) {
		cin.ignore();
		cout << "Enter name of product: ";
		getline(cin, H);
		cout << "Enter ammount of product: ";
		cin >> q;
		cout << "Enter cost of 1 piece of product: ";
		cin >> c;
		add_elem(H, c, q, Root);
	}
	int ta = 0;
	cout << "Tree:\n";
	oubt(Root, ta);
	cout << "Enter ammount of new elements: ";
	cin >> it;
	string E;
	for (int i = 0; i < it; i++) {
		cin.ignore();
		cout << "Enter name of product: ";
		getline(cin, H);
		cout << "Enter ammount of product: ";
		cin >> q;
		cout << "Enter cost of 1 piece of product: ";
		cin >> c;
		add_elem(H, c, q, Root);
	}
	cout << "New tree:\n";
	oubt(Root, ta);
	int tc = calc(Root);
	cout << "Total cost of product: " << tc << endl;
	FT(Root);
	system("pause");
	return 0;
}