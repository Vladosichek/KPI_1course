#include <iostream>
#include<cmath>
#include <time.h>
using namespace std;
int enter_n();
float** array_2d(int);
void generate_2d_array(float**, int);
void output_2d_array(int, int, float**);
void num_of_col(float**, int, float*);
float** delete_column_2d_array(float**, int, int);
void delition_of_2d_array(float**, int);
void main() {
	float** A;
	int n= enter_n();
	float Q[2];
	A = array_2d(n);
	generate_2d_array(A, n);
	output_2d_array(n, n, A);
	num_of_col(A, n, Q);
	float m = Q[1];
	int r = Q[0];
	cout << "Seeken number:" << m << endl << "Number of column of the seeken number: " << r + 1 << endl;
	delete_column_2d_array(A, n, r);
	output_2d_array(n, n - 1, A);
	delition_of_2d_array(A, n);
	system("pause");
}
int enter_n() {
	int o = 0;
	while (o <= 1) {
		cout << "Enter n:";
		cin >> o;
	}
	return o;
}
float** array_2d(int q) {
	float** M = new float* [q];
	for (int i = 0; i < q; i++) {
		M[i] = new float[q];
	}
	return M;
}
void generate_2d_array(float** M, int q) {
	srand(time(NULL));
	for (int i = 0; i < q; i++) {
		for (int j = 0; j < q; j++) {
			M[i][j] = (rand() % 5000) / 100.0;
		}
	}
}
void output_2d_array(int z, int e, float** M) {
	for (int i = 0; i < z; i++) {
		for (int j = 0; j < e; j++) {
			cout << M[i][j] << "\t";
		}
		cout << endl;
	}
}
void num_of_col(float** M, int q, float* L) {
	float max = 0;
	int l = 0;
	int g = 0;
	for (int i = 0; i < q - 1; i++) {
		for (int j = l + 1; j < q; j++) {
			if (M[i][j] > max) {
				max = M[i][j];
				g = j;
			}
		}
		l++;
	}
	L[0] = g;
	L[1] = max;
}
float** delete_column_2d_array(float** M, int q, int s) {
	for (int i = 0; i < q; i++) {
		for (int j = s; j < q; j++) {
			M[i][j] = M[i][j + 1];
		}
	}
	return M;
}
void delition_of_2d_array(float** M, int q) {
	for (int i = 0; i < q; i++) {
		delete[] M[i];
	}
	delete[] M;
}