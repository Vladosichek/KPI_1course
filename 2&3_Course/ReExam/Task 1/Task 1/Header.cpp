#include "Header.h"
void del(int** A, int q) {
	for (int i = 0; i < q; i++) {
		delete[] A[i];
	}
	delete[] A;
}
void outa(int* A, int q) {
	cout << "Array:\n";
	for (int i = 0; i < q; i++) {
		cout << A[i] << "\t";
	}
	cout << endl;
}
int* fill(int** A, int q, int w) {
	int* U = new int[w];
	int c = 0;
	for (int j = 0; j < w; j++) {
		for (int i = 0; i < q; i++) {
			if (A[i][j] == 0) {
				c++;
			}
		}
		U[j] = c;
		c = 0;
	}
	return U;
}
void change(int** A, int q, int pos) {
	int it = -1;
	int ite;
	int c = 0;
	int max = 0;
	for (int i = 0; i < q; i++) {
		if (A[i][pos] == 0) {
			c++;
			if (it == -1) {
				it = i;
			}
		}
		else {
			if (max < c) {
				max = c;
				ite = it;
			}
			it = -1;
			c = 0;
		}
	}
	if (max < c) {
		max = c;
		ite = it;
	}
	it = -1;
	c = 0;
	for (int i = 0; i < max; i++) {
		A[ite + i][pos] = ite + i - pos;
	}
}
int find(int** A, int q, int w) {
	int max = 0;
	int c = 0;
	int pos;
	for (int j = 0; j < w; j++) {
		for (int i = 0; i < q; i++) {
			if (A[i][j] == 0) {
				c++;
			}
			else {
				if (max < c) {
					max = c;
					pos = j;
				}
				c = 0;
			}
		}
		if (max < c) {
			max = c;
			pos = j;
		}
		c = 0;
	}
	return pos;
}
void outm(int** A, int q, int w) {
	cout << "Matrix:\n";
	for (int i = 0; i < q; i++) {
		for (int j = 0; j < w; j++) {
			cout << A[i][j] << "\t";
		}
		cout << endl;
	}
}
int** gen(int q, int w) {
	int** A = new int* [q];
	for (int i = 0; i < q; i++) {
		A[i] = new int[w];
	}
	srand(time(NULL));
	for (int i = 0; i < q; i++) {
		for (int j = 0; j < w; j++) {
			A[i][j] = rand() % 2;
		}
	}
	return A;
}