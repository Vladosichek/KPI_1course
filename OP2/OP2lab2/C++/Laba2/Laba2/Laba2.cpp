#include "Header.h"
#include <iostream>
#include <string>
int main()
{
    string name1 = "file1.txt";
    string name2 = "file2.txt";
    int que;
    cout << "====>If you want to clear file enter 1: ";
    cin >> que;
    enter_f(name1, que);
    cout << "====>File 1:\n";
    ou(name1);
    char date[15];
    cout << "====>Today`s date (dd.mm.yyyy): ";
    cin >> date;
    fil(name1, name2, date);
    cout << "====>File 2:\n";
    ou(name2);
    cout << "====>Products produced in the last 10 days:\n";
    ou_sp(name1, date);
    system("pause");
    return 0;
}