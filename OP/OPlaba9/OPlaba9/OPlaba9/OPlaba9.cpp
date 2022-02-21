#include <iostream>
#include <string>
using namespace std;
void concl(string, int*, char*);
void out(char*);
void main()
{
	string s;
	int C[3];
	char R[100];
	cout << "Enter string:";
	getline(cin, s);
	concl(s, C, R);
	out(R);
	cout << "Ammounts of ( and ) are: " << C[0] << " and " << C[1] << endl;
	cout << "Balance of () is ";
	if ((C[2] == 1)&(C[0]-C[1]==0)) {
		cout << "kept" << endl;
	}
	else {
		cout << "unkept" << endl;
	}
	system("pause");
}
void concl(string str, int* A, char* B) {
	int i = 0, k = 0, l = 0, j =0 , con = 1;
	do {
		if (str[i] == '(') {
			k += 1;
			B[j] = '(';
			++j;
		}
		else if (str[i] == ')') {
			l += 1;
			B[j] = ')';
			++j;
		}
		if(k<l){
			con = 0;
		}
		++i;
	} while (str[i] != '\0');
	B[j] = '\0';
	A[0] = k;
	A[1] = l;
	A[2] = con;
}
void out(char* B) {
	int i = 0;
	while (B[i] != '\0') {
		cout << B[i];
		++i;
	}
	cout << endl;
}