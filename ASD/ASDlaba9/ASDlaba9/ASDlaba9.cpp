#include <iostream>
#include <time.h>
using namespace std;
float** array_2d(int, int);
void generate_2d_array(float**, int, int);
void output_2d_array(int, int, float**);
void min(float**, int, int, float*);
void output_array(float*);
void delition_of_2d_array(float**, int);
int main() {
	float** A;
	int m, n;
	float R[100];
	cout << "Enter m: ";
	cin >> m;
	cout <<  "Enter n: ";
	cin >> n;
	A = array_2d(m, n);
	generate_2d_array(A, m, n);
	cout << "Matrix initial:" << endl;
	output_2d_array(m, n, A);
	min(A, m, n, R);
	output_array(R);
	cout << "Matrix final:" << endl;
	output_2d_array(m, n, A);
	delition_of_2d_array(A, m);
	system("pause");
}
float** array_2d(int q, int z) {
	float** M = new float* [q];
	for (int i = 0; i < q; i++) {
		M[i] = new float[z];
	}
	return M;
}
void generate_2d_array(float** M, int q, int z) {
	srand(time(NULL));
	for (int i = 0; i < q; i++) {
		for (int j = 0; j < z; j++) {
			M[i][j] = ((rand() % 5000) / 100.0)-15;
		}
	}
}
void output_2d_array(int q, int z, float** M) {
	for (int i = 0; i < q; i++) {
		for (int j = 0; j < z; j++) {
			cout << M[i][j] << "\t";
		}
		cout << endl;
	}
}
void min(float** M, int q, int z, float* Q) {
	float min, medium;
	int y=0, h = 0;
	for (int i = 0; i < q; i++) {
		min = 35;
		medium = M[i][z / 2];
		for (int j = 0; j < z; j++) {
			if (M[i][j] < min) {
				min = M[i][j];
				y = j;
			}
		}
		Q[h] = min;
		Q[h + 1] = i + 1;
		Q[h + 2] = y + 1;
		h += 3;
		M[i][y] = medium;
	}
	Q[h] = -100;
}
void output_array(float* Q) {
	int h = 0;
	cout << "Minimal elements:" << endl;
	while (Q[h] != -100) {
		cout << Q[h] << '\t' << Q[h + 1] << '\t' << Q[h + 2] << endl;
		h += 3;
	}
}
void delition_of_2d_array(float** M, int q) {
	for (int i = 0; i < q; i++) {
		delete[] M[i];
	}
	delete[] M;
}