#include "Header.h"
int seek(int q, Worker* A, string D) {
    int am_days = 0;
    string help = D;
    string H = "";
    H = help.substr(0, 2);        //підрахунок к-сті діб (у кожному місяці 30 діб, у році - 360)
    am_days += stoi(H);
    H = help.substr(3, 2);
    am_days += stoi(H) * 30;
    H = help.substr(6, 4);
    am_days += stoi(H) * 360;
    int am_days_worker;
    int am_days_max = 0;
    int numb = -1;
    for (int i = 0; i < q; i++) {
        am_days_worker = 0;
        help = A[i].GetDate();
        H = "";
        H = help.substr(0, 2);
        am_days_worker += stoi(H);
        H = help.substr(3, 2);
        am_days_worker += stoi(H) * 30;
        H = help.substr(6, 4);
        am_days_worker += stoi(H) * 360;
        if ((am_days - am_days_worker) > am_days_max) {
            am_days_max = am_days - am_days_worker;
            numb = i;
        }
    }
    return numb;
}
void outList(int q, Worker* A) {
    cout << "List of workers: \n";
    for (int i = 0; i < q; i++) {
        cout << "Worker " << i + 1 << ": ";
        cout << A[i].GetSurname() << " " << A[i].GetName() << " " << A[i].GetPatronym() << " Date of hirement: " << A[i].GetDate() << endl;
    }
}
Worker* fill(int q) {
    Worker* A = new Worker[q];
    string Help;
    for (int i = 0; i < q; i++) {
        cout << "Worker " << i + 1 << endl;
        cout << "Enter surname: ";
        cin >> Help;
        A[i].SetSurname(Help);
        cout << "Enter name: ";
        cin >> Help;
        A[i].SetName(Help);
        cout << "Enter patronym: ";
        cin >> Help;
        A[i].SetPatronym(Help);
        cout << "Enter date of hirement (DD.MM.YYYY): ";
        cin >> Help;
        A[i].SetDate(Help);
    }
    return A;
}
Worker::Worker() {};
Worker::Worker(string patronym, string name, string surname, string date) {
    this->patronym = patronym;
    this->name = name;
    this->surname = surname;
    this->date = date;
};
string Worker::GetPatronym() { return this->patronym; };
string Worker::GetName() { return this->name; };
string Worker::GetSurname() { return this->surname; };
string Worker::GetDate() { return this->date; };
void Worker::SetPatronym(string patronym_new) { patronym = patronym_new; };
void Worker::SetName(string name_new) { name = name_new; };
void Worker::SetSurname(string surname_new) { surname = surname_new; };
void Worker::SetDate(string date_new) { date = date_new; };