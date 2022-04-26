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
    Worker();
    Worker(string patronym, string name, string surname, string date);
    string GetPatronym();
    string GetName();
    string GetSurname();
    string GetDate();
    void SetPatronym(string patronym_new);
    void SetName(string name_new);
    void SetSurname(string surname_new);
    void SetDate(string date_new);
};
Worker* fill(int);
void outList(int, Worker*);
int seek(int, Worker*, string);