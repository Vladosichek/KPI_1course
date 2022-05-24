#include "Header.h"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    string date;
    cout << "Enter date: ";
    getline(cin, date);
    int am;
    cout << "Enter ammount of meetings: ";
    cin >> am;
    Meeting* Lis = new Meeting[am];
    string H, J, K, L;
    cout << "Let`s begin with meetings! Enter info about them!\n";
    cin.ignore();
    for (int i = 0; i < am; i++) {
        cout <<"Meeting " << i+1 << "\nEnter PIB of person: ";
        getline(cin, H);
        cout << "Enter place of meeting: ";
        getline(cin, J);
        cout << "Enter time of begining (HH:MM): ";
        getline(cin, K);
        cout << "Enter endurance of meeting (HH:MM): ";
        getline(cin, L);
        Lis[i] = Meeting(H, J, date, K, L);
    }
    int year;
    cout << "Enter info about the birthday party!\nEnter PIB of person: ";
    getline(cin, H);
    cout << "Enter place of party: ";
    getline(cin, J);
    cout << "Enter time of begining (HH:MM): ";
    getline(cin, K);
    cout << "Enter endurance of party (HH:MM): ";
    getline(cin, L);
    cout << "Enter age of person: ";
    cin >> year;
    Birthday Party = Birthday(H, year, J, date, K, L);
    cout << "General info about the day:\n";
    for (int i = 0; i < am; i++) {
        cout << "Meeting " << i+1 << "\nPIB: " << Lis[i].Get_PIB();
        cout << "\nPlace of meeting: " << Lis[i].Get_place() << "\nDate of meeting: " << Lis[i].Get_dat();
        cout << "\nTime of begining: " << Lis[i].Get_in_t() << "\nEndurance: " << Lis[i].Get_en() << endl;
    }
    cout << "Birthday party:\nPIB: " << Party.Get_PIB() << "\nPlace of party: " << Party.Get_place();
    cout << "\nAge of person: " << Party.Get_age() << "\nDate of party: " << Party.Get_dat();
    cout << "\nTime of begining: " << Party.Get_in_t() << "\nEndurance: " << Party.Get_en() << endl;
    cout << "Info about the last meeting:\n";
    int num = seek(Lis, am);
    cout << "PIB: " << Lis[num].Get_PIB();
    cout << "\nPlace of meeting: " << Lis[num].Get_place() << "\nDate of meeting: " << Lis[num].Get_dat();
    cout << "\nTime of begining: " << Lis[num].Get_in_t() << "\nEndurance: " << Lis[num].Get_en() << endl;
    string res = Lis[num].Last_calc(Party.Get_in_t());
    cout << res << endl;
    delete[] Lis;
    system("pause");
    return 0;
}