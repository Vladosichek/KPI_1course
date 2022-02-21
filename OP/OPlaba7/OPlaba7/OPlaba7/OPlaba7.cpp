#include <iostream>
#include<cmath>
#include <time.h>
using namespace std;
void generate(float*, int);
void output(float*, int);
float special_average(float*, int, int);
void change(float*, int, int, float);
void main() {
	const int c = 100;
	float M[c];
	float q;
	int k;
	int n;
	do {
		cout << "Enter k(natural number):";
		cin >>k;
	} while (k < 1);
	do {
		cout << "Enter n(size of an array; from 1 to 100):";
		cin >> n;
	} while (n < 1 || n > 100);
	generate(M, n);
	output(M, n);
	q = special_average(M, n, k);
	cout << "Seeken average number:" << q << endl;
	change(M, n, k, q);
	output(M, n);
	system("pause");
}
void generate(float* p,int l) {
	srand(time(NULL));
	for (int i = 0; i < l; i++) {
		*p = (rand() % 30000 - 15000) / 100.0;
		p += 1;
	}
}
void output(float* p, int l) {
	for (int i = 0; i < l; i++) {
		cout << *p << " ";
		p += 1;
	}
	cout << endl;
}
float special_average(float* p, int l, int e) {
	float b;
	int r = 0;
	float sum = 0.0;
	for (int i = 0; i < l; i++) {
		if (*p > e) {
			r += 1;
			sum += *p;
		}
		p += 1;
	}
	b = sum / r;
	cout << "Ammount of seeken numbers:" << r << endl;
	return b;
}
void change(float* p, int l, int e, float g) {
	for (int i = 0; i < l; i++) {
		if (*p > e) {
			*p = g;
		}
		p += 1;
	}
}