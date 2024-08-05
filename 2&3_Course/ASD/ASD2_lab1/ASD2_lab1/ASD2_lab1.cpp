#include <iostream>
#include <ctime>
using namespace std;
void comb(int* , int , long int& , int& );
void buble(int* , int , long int& , int& );
void out(int* );
void fill(int* , int* , int* , int* , int* , int );
int main()
{
	int a;
	cout << "Enter ammount:" ;
	cin >> a;
	if (a < 10) {
		a = 10;
	}
	int* Best = new int[a];
	int* Worst1 = new int[a];
	int* Worst2 = new int[a];
	int* Random1 = new int[a];
	int* Random2 = new int[a];
	fill(Best, Worst1, Worst2, Random1, Random2, a);
	long int steps = 0;
	int swaps = 0;
	cout << "Best:\n";
	cout << "Initial array:\n";
	out(Best);
	buble(Best, a, steps, swaps);
	cout << "Sorted array:\n";
	out(Best);
	cout << "Bublesort\nSteps:" << steps << "   Swaps:" << swaps << endl;
	steps = 0;
	swaps = 0;
	comb(Best, a, steps, swaps);
	cout << "Combsort\nSteps:" << steps << "   Swaps:" << swaps << endl;
	steps = 0;
	swaps = 0;
	cout << "Worst:\n";
	cout << "Initial array:\n";
	out(Worst1);
	//out(Worst2);
	buble(Worst1, a, steps, swaps);
	cout << "Sorted array:\n";
	out(Worst1);
	cout << "Bublesort\nSteps:" << steps << "   Swaps:" << swaps << endl;
	steps = 0;
	swaps = 0;
	comb(Worst2, a, steps, swaps);
	cout << "Combsort\nSteps:" << steps << "   Swaps:" << swaps << endl;
	steps = 0;
	swaps = 0;
	cout << "Random:\n";
	cout << "Initial array:\n";
	out(Random1);
	//out(Random2);
	buble(Random1, a, steps, swaps);
	cout << "Sorted array:\n";
	out(Random1);
	cout << "Bublesort\nSteps:" << steps << "   Swaps:" << swaps << endl;
	steps = 0;
	swaps = 0;
	comb(Random2, a, steps, swaps);
	cout << "Combsort\nSteps:" << steps << "   Swaps:" << swaps << endl;
	delete[] Best, Worst1, Worst2, Random1, Random2;
	return 0;
	system("pause");
}
void fill(int* A, int* B1, int* B2, int* C1, int* C2, int q) {
	srand(time(NULL));
	for (int i = 0; i < q; i++) {
		A[i] = i + 1;
		B1[i] = q - i;
		B2[i] = q - i;
		C1[i] = q - i;
		C2[i] = q - i;
	}
	int h;
	int y;
	int pos1;
	int pos2;
	h = rand() % (q / 2) + q / 4;
	for (int i = 0; i < h; i++) {
		pos1 = rand() % q;
		pos2 = rand() % q;
		y = C1[pos1];
		C1[pos1] = C1[pos2];
		C2[pos1] = C2[pos2];
		C1[pos2] = y;
		C2[pos2] = y;
	}
}
void out(int* A) {
	for (int i = 0; i < 10; i++) {
		cout << A[i] << "\t";
	}
	cout << endl;
}
void buble(int* A, int q, long int& st, int& sw) {
	bool flag = 1;
	int h;
	int j = q;
	while (flag) {
		flag = 0;
		for (int i = 0; i < j - 1; i++) {
			st++;
			if (A[i] > A[i + 1]) {
				h = A[i];
				A[i] = A[i + 1];
				A[i + 1] = h;
				flag = 1;
				sw++;
			}
		}
		j--;
	}
}
void comb(int* A, int q, long int& st, int& sw) {
	int h;
	double factor = 1.2473309;
	int len = q;
	bool flag = 1;
	while (len > 1 || flag) {
		flag = 0;
		len /= factor;
		if (len < 1) {
			len = 1;
		}
		for (int i = 0; i < q - len; i++) {
			st++;
			if (A[i] > A[i + len]) {
				h = A[i];
				A[i] = A[i + len];
				A[i + len] = h;
				sw++;
				flag = 1;
			}
		}
	}
}
