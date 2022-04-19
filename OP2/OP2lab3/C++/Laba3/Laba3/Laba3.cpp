#include <iostream>
#include <string>
#include "Header.h"
using namespace std;
int main()
{
    int n;
    cout << "Enter ammount of workers: ";
    cin >> n;
    Worker* Lis=fill(n);
    string today;
    cout << "Enter todays date (DD.MM.YYYY): ";
    cin >> today;
    outList(n, Lis);
    int num=seek(n, Lis, today);
    if (num == -1) {
        cout << "There is no worker with proper date of hirement!!!\n";
    }
    else {
        cout << "The worker with the biggest experience is number: " << num + 1 << endl;
        cout << Lis[num].GetSurname() << " " << Lis[num].GetName() << " " << Lis[num].GetPatronym() << " Date of hirement: " << Lis[num].GetDate() << endl;
    }
    delete[] Lis;
    system("pause");
    return 0;
}
