#include "Header.h"
void ou_sp(string nam, char dat[15]) {    //вив≥д товар≥в, виготовлених за останн≥ 10 д≥б
    Data lis;
    ifstream outp(nam, ios::binary);
    int am_days = 0;     //к-сть д≥б на сьогодн≥
    int am_days_c;       //к-сть д≥б на момент створенн€
    string help = dat;
    string H = "";
    H = help.substr(0, 2);          //п≥драхунок к-ст≥ д≥б (у кожному м≥с€ц≥ 30 д≥б, у роц≥ - 360)
    am_days += stoi(H);
    H = help.substr(3, 2);
    am_days += stoi(H) * 30;
    H = help.substr(6, 4);
    am_days += stoi(H) * 360;
    while (outp.read((char*)&lis, sizeof(Data))) {       //п≥драхунок к-ст≥ д≥б (у кожному м≥с€ц≥ 30 д≥б, у роц≥ - 360)
        am_days_c = 0;
        help = lis.creation_date;
        H = "";
        H = help.substr(0, 2);
        am_days_c += stoi(H);
        H = help.substr(3, 2);
        am_days_c += stoi(H) * 30;
        H = help.substr(6, 4);
        am_days_c += stoi(H) * 360;
        if ((am_days - am_days_c) < 10 && (am_days - am_days_c) >= 0) {           //€кщо р≥зниц€ д≥б Ї [0;10)
            cout << lis.name << " - " << lis.creation_date << " - " << lis.last_date << " - " << lis.price << " dollars" << endl;
        }
    }
    outp.close();
}
void fil(string nam1, string nam2, char dat[15]) {
    Data lis;
    ifstream outp(nam1, ios::binary);
    ofstream inp(nam2, ios::binary);
    int am_days = 0;      //к-сть д≥б на сьогодн≥
    int am_days_c;         //к-сть д≥б на момент створенн€
    int am_days_l;          //к-сть д≥б на момент к≥нц€ придатност≥
    string help = dat;
    string H = "";
    H = help.substr(0, 2);        //п≥драхунок к-ст≥ д≥б (у кожному м≥с€ц≥ 30 д≥б, у роц≥ - 360)
    am_days += stoi(H);
    H = help.substr(3, 2);
    am_days += stoi(H) * 30;
    H = help.substr(6, 4);
    am_days += stoi(H) * 360;
    while (outp.read((char*)&lis, sizeof(Data))) {   //п≥драхунок к-ст≥ д≥б (у кожному м≥с€ц≥ 30 д≥б, у роц≥ - 360)
        am_days_c = 0;
        am_days_l = 0;
        help = lis.creation_date;
        H = "";
        H = help.substr(0, 2);
        am_days_c += stoi(H);
        H = help.substr(3, 2);
        am_days_c += stoi(H) * 30;
        H = help.substr(6, 4);
        am_days_c += stoi(H) * 360;
        help = lis.last_date;
        H = "";
        H = help.substr(0, 2);
        am_days_l += stoi(H);
        H = help.substr(3, 2);
        am_days_l += stoi(H) * 30;
        H = help.substr(6, 4);
        am_days_l += stoi(H) * 360;
        if (float((am_days_l - am_days)) / (am_days_l - am_days_c) < 0.1 && float((am_days_l - am_days)) / (am_days_l - am_days_c) >= 0) {
            inp.write((char*)&lis, sizeof(Data));
        }
    }
    outp.close();
    inp.close();
}
void ou(string name) {     //вив≥д ≥нформац≥њ з файл≥в у консоль
    Data lis;
    ifstream outp(name, ios::binary);
    while (outp.read((char*)&lis, sizeof(Data))) {
        cout << lis.name << " - " << lis.creation_date << " - " << lis.last_date << " - " << lis.price << " dollars" << endl;
    }
    outp.close();
}
void enter_f(string n1, int q) {   //введенн€ ≥нформац≥њ про товари
    int a;
    cout << "Enter ammount of products: ";
    cin >> a;
    Data lis;
    if (q == 1) {   //користувач може вибрати, чи хоче в≥н очистити файл в≥д попередн≥х данних (в main() вводимо que)
        ofstream inp(n1, ios::binary);
        inp.close();
    }
    ofstream inp(n1, ios::binary | ios::app);   // у будь-€кому випадку ми доповнюЇмо наш б≥нарний файл
    for (int i = 0; i < a; i++) {                // використовуЇмо структуру типу Date
        cin.ignore();
        cout << "Name: "; cin >> lis.name;
        cout << "Date of creation (dd.mm.yyyy): ";
        cin >> lis.creation_date;
        cout << "Last date (dd.mm.yyyy): ";
        cin >> lis.last_date;
        cout << "Price: "; cin >> lis.price;
        inp.write((char*)&lis, sizeof(Data));
    }
    inp.close();
}