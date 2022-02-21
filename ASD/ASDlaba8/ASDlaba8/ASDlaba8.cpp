#include <iostream>
#include<cmath>
#include <time.h>
using namespace std;
int** array_2d(int, int);
void generate_2d_array(int**, int, int);
void output_2d_array(int, int, int**);
void fill_arr(int**, int*, int, int);
void arragement(int*, int);
void output_array(int*, int);
void delition_of_2d_array(int**, int);
void main() {
	int n = 5;
	int k = 8;
	int** A;
	A = array_2d(n, k);
	generate_2d_array(A, n, k);
	cout << "matrix:" << endl;
	output_2d_array(n, k, A);
	int* B = new int[k];
	fill_arr(A, B, n, k);
	cout << "array before arregement:" << endl;
	output_array(B, k);
	arragement(B, k);
	cout << "array after arregement:" << endl;
	output_array(B, k);
	delition_of_2d_array(A, n);
	delete[] B;
	system("pause");
}
int** array_2d(int q, int z) {
	int** M = new int* [q];
	for (int i = 0; i < q; i++) {
		M[i] = new int[z];
	}
	return M;
}
void generate_2d_array(int** M, int q, int z) {
	srand(time(NULL));
	for (int i = 0; i < q; i++) {
		for (int j = 0; j < z; j++) {
			M[i][j] = rand() % 101 - 50;
		}
	}
}
void output_2d_array(int q, int z, int** M) {
	for (int i = 0; i < q; i++) {
		for (int j = 0; j < z; j++) {
			cout << M[i][j] << "\t";
		}
		cout << endl;
	}
}
void fill_arr(int** M, int* Q, int q, int z) {
	for (int j = 0; j < z; j++) {
		Q[j] = 1;
		for (int i = 0; i < q; i++) {
			if (M[i][j] > 0) {
				Q[j] *= M[i][j];
			}
		}
	}
}
void arragement(int* Q, int z) {
	for (int j = 1; j < z; j++) {
		for (int i = 0; i < z - j; i++) {
			if (Q[i] > Q[i + 1]) {
				int s = Q[i];
				Q[i] = Q[i + 1];
				Q[i + 1] = s;
			}
		}
	}
}
void output_array(int* Q, int z) {
	for (int j = 0; j < z; j++) {
		cout << Q[j] << "\t";
	}
	cout << endl;
}
void delition_of_2d_array(int** M, int q) {
	for (int i = 0; i < q; i++) {
		delete[] M[i];
	}
	delete[] M;
}