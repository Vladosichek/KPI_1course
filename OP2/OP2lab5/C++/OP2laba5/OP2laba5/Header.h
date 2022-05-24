#pragma once
#include <iostream>
#include <string>
using namespace std;
class Event {
private:
    string dat;
    string in_t;
    string en;
public:
    Event();
    Event(string dat_n, string in_t_n, string en_n);
    string Get_dat();
    string Get_in_t();
    string Get_en();
    string Last_calc(string time_n);
};
class Birthday : public Event {
private:
    string PIB;
    int age;
    string place;
public:
    Birthday();
    Birthday(string PIB_n, int age_n, string place_n, string dat_n, string in_t_n, string en_n) :Event(dat_n, in_t_n, en_n)
    {
        this->PIB = PIB_n; this->age = age_n; this->place = place_n;
    };
    string Get_PIB();
    int Get_age();
    string Get_place();
};
class Meeting : public Event {
private:
    string PIB;
    string place;
public:
    Meeting();
    Meeting(string PIB_n, string place_n, string dat_n, string in_t_n, string en_n) :Event(dat_n, in_t_n, en_n)
    {
        this->PIB = PIB_n; this->place = place_n;
    };
    string Get_PIB();
    string Get_place();
};
int seek(Meeting*, int);