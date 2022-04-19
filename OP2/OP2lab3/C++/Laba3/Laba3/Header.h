#pragma once
#include <iostream>
#include <string>
using namespace std;
class Worker {
private:
    string patronym;
    string name;
    string surname;
    string date;
public:
    Worker() {};
    Worker(string patronym, string name, string surname, string date) {
        this->patronym = patronym;
        this->name = name;
        this->surname = surname;
        this->date = date;
    };
    string GetPatronym() { return this->patronym; };
    string GetName() { return this->name; };
    string GetSurname() { return this->surname; };
    string GetDate() { return this->date; };
    void SetPatronym(string patronym_new) { patronym = patronym_new; };
    void SetName(string name_new) { name = name_new; };
    void SetSurname(string surname_new) { surname = surname_new; };
    void SetDate(string date_new) { date = date_new; };
};
Worker* fill(int);
void outList(int, Worker*);
int seek(int, Worker*, string);