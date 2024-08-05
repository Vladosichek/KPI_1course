#pragma once
#include <iostream>
#include <string>
using namespace std;
class Money {
private:
    int hrn;
    int kp;
public:
    Money(string su);
    void ou_s();
    void operator++();
    bool operator ||(Money obj);
};