#include "Header.h"
void ou_sp(string nam, char dat[15]) {    //���� ������, ������������ �� ������ 10 ��
    Data lis;
    ifstream outp(nam, ios::binary);
    int am_days = 0;     //�-��� �� �� �������
    int am_days_c;       //�-��� �� �� ������ ���������
    string help = dat;
    string H = "";
    H = help.substr(0, 2);          //��������� �-�� �� (� ������� ����� 30 ��, � ���� - 360)
    am_days += stoi(H);
    H = help.substr(3, 2);
    am_days += stoi(H) * 30;
    H = help.substr(6, 4);
    am_days += stoi(H) * 360;
    while (outp.read((char*)&lis, sizeof(Data))) {       //��������� �-�� �� (� ������� ����� 30 ��, � ���� - 360)
        am_days_c = 0;
        help = lis.creation_date;
        H = "";
        H = help.substr(0, 2);
        am_days_c += stoi(H);
        H = help.substr(3, 2);
        am_days_c += stoi(H) * 30;
        H = help.substr(6, 4);
        am_days_c += stoi(H) * 360;
        if ((am_days - am_days_c) < 10 && (am_days - am_days_c) >= 0) {           //���� ������ �� � [0;10)
            cout << lis.name << " - " << lis.creation_date << " - " << lis.last_date << " - " << lis.price << " dollars" << endl;
        }
    }
    outp.close();
}
void fil(string nam1, string nam2, char dat[15]) {
    Data lis;
    ifstream outp(nam1, ios::binary);
    ofstream inp(nam2, ios::binary);
    int am_days = 0;      //�-��� �� �� �������
    int am_days_c;         //�-��� �� �� ������ ���������
    int am_days_l;          //�-��� �� �� ������ ���� ����������
    string help = dat;
    string H = "";
    H = help.substr(0, 2);        //��������� �-�� �� (� ������� ����� 30 ��, � ���� - 360)
    am_days += stoi(H);
    H = help.substr(3, 2);
    am_days += stoi(H) * 30;
    H = help.substr(6, 4);
    am_days += stoi(H) * 360;
    while (outp.read((char*)&lis, sizeof(Data))) {   //��������� �-�� �� (� ������� ����� 30 ��, � ���� - 360)
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
void ou(string name) {     //���� ���������� � ����� � �������
    Data lis;
    ifstream outp(name, ios::binary);
    while (outp.read((char*)&lis, sizeof(Data))) {
        cout << lis.name << " - " << lis.creation_date << " - " << lis.last_date << " - " << lis.price << " dollars" << endl;
    }
    outp.close();
}
void enter_f(string n1, int q) {   //�������� ���������� ��� ������
    int a;
    cout << "Enter ammount of products: ";
    cin >> a;
    Data lis;
    if (q == 1) {   //���������� ���� �������, �� ���� �� �������� ���� �� ��������� ������ (� main() ������� que)
        ofstream inp(n1, ios::binary);
        inp.close();
    }
    ofstream inp(n1, ios::binary | ios::app);   // � ����-����� ������� �� ���������� ��� ������� ����
    for (int i = 0; i < a; i++) {                // ������������� ��������� ���� Date
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