/*Згенерувати матрицю Q(kxm), що складається з нулів та одиниць. 

Знайти номер її стовпця, що містить найдовший ланцюжок нулів. Якщо таких стовпців декілька, то взяти перший із них.

Замістити нулі знайденого ланцюжка різницею індексів відповідного елемента (нуля) у матриці (наприклад, 0, що знаходиться в позиції [2][5], слід замістити числом -3).   

На основі зміненої матриці Q побудувати масив R(m), кожен елемент якого Ri - це кількісь нульових елементів у i-му стовпці матриці.*/
#include "Header.h"
#include <iostream>
#include <ctime>
using namespace std;

int main()
{
	int k, m;
	cout << "Enter k:";
	cin >> k;
	cout << "Enter m:";
	cin >> m;
	int** Q = gen(k, m);
	outm(Q, k, m);
	int it = find(Q, k, m);
	cout << "Seeken row is " << it + 1 << endl;
	change(Q, k, it);
	outm(Q, k, m);
	int* R = fill(Q, k, m);
	outa(R, m);
	delete[] R;
	del(Q, k);
	return 0;
	system("pause");
}
