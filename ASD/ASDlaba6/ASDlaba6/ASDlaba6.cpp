#include<iostream>
#include<cmath>
using namespace std;
void tr(int, float);
void main() {
	float n;
	int s = 5;
	cout << " Enter n:";
	cin >> n;
	cout << "Pifagor triangles: " << endl;
	tr(s, n);
	cout << endl;
	system("pause");
}
void tr(int c, float l) {
	int a = 3;
	int b = 4;
	if (c > l) {
	}
	else {
		for (b = 4; b < c; b++) {
			for (a = 3; a < b; a++) {
				if (a * a + b * b == c * c) {
					printf("%1d%12d%12d\n", a, b, c);
				}
			}
		}
		tr(c + 1, l);
	}
}