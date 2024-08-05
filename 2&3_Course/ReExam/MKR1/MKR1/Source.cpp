#include "Header.h"
bool Money::operator ||(Money obj) {
    float i = hrn + float(kp) / 100;
    float u = obj.hrn + float(obj.kp) / 100;
    bool res = 0;
    if (i > u) {
        res = 1;
    }
    return res;
};
void Money::operator++() {
    hrn++;
};
void Money::ou_s() {
    cout << hrn << "hryvnas " << kp << "kopiykas\n";
};
Money::Money(string su) {
    string H = "";
    string U = "";
    int i = 0;
    while (su[i] != ',') {
        i++;
    }
    H += su.substr(0, i);
    i++;
    int u = su.length() - i;
    U += su.substr(i, u);
    hrn = stoi(H);
    kp = stoi(U);
}