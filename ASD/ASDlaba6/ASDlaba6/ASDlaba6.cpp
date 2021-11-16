#include<iostream>
#include<cmath>
using namespace std;
int trian(int u, int j, int n);
int main() {
	float n;
	int a;
	int b;
	int c;
	int p;
	cout << "Enter n:";
	cin >> n;
	cout << "Pifagor's triangles:" << endl;
	for (c = 1; c <= n; c += 1) {
		for (b = 1; b <= c; b += 1) {
			for (a = 1; a <= b; a += 1) {
				p = trian(a, b, c);
				if ( p == 1) {
					cout << a << "|" << b << "|" << c << endl;
				}
			}
		}
	}
	return 0;
	system("pause");
}
int trian(int u, int j, int q){
	int f;
	f = 0;
	if (u * u + j * j == q * q) {
		f=1;
	}
	else {
		f=0;
	}
	return f;
}