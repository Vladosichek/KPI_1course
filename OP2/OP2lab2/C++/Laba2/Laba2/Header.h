#pragma once
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
struct Data {
    char name[50] = "";
    char creation_date[15] = "";
    char last_date[15] = "";
    float price = 0;
};
void enter_f(string, int);
void ou(string);
void fil(string, string, char[15]);
void ou_sp(string, char[15]);
