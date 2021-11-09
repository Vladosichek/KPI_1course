#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
long double arctg(long double a, int l);
int main(){
	long double x;
	int j;
	int q;
	cout << "Enter x (x>=0): ";
	cin >> x;
	cout << "Enter accuracy (10^e): ";
	cin >> j;
	q = -j;
	long double t, u, c;
	if (x < 0){
		cout << "Invalid x"<< endl;
	}
	else if (x <= 1) {
		cout << "y=arctg(x)+arctg(2x)" << endl;
		t = arctg(x,j);
		cout << "arctg(x)=" << fixed << setprecision(q) << t << endl;
		if (x <= 0.5) {
			u = arctg(2 * x,j);
			c = t+u;
			cout << "arctg(2x)=" << fixed << setprecision(q) << u << endl << "y=" << fixed << setprecision(q) << c<<endl;
		}
		else {
			cout << "arctg(2x) can not be counted because taylor series for arctg(a) can be used if |a|<=1" << endl << "Error"<<endl;
		}
	}
	else {
		cout << "y=arctg(x)/arctg(x-5)" << endl;
		cout << "arctg(x) can not be counted because taylor series for arctg(a) can be used if |a|<=1" << endl << "Error"<<endl;
	}
	system("pause");
	return 0;
}
long double arctg(long double a, int l) {
	int i = 1;
	long double z = 1;
	long double result = 0;
	while (fabs(z) >= pow(10, l)) {
		z = pow(-1, i - 1) * pow(a, 2 * i - 1) / (2 * i - 1);
		result += z;
		i += 1;
	}
	return result;
}