#include "Header.h"
int seek(Meeting* A, int q) {
    int max = -1;
    int pos = -1;
    string H;
    string F;
    int min = 0;
    for (int i = 0; i < q; i++) {
        F = A[i].Get_in_t();
        H = F.substr(0, 2);
        min += stoi(H) * 60;
        H = F.substr(3, 2);
        min += stoi(H);
        if (max < min) {
            max = min;
            pos = i;
        }
        min = 0;
    }
    return pos;
}
Event::Event() {};
Event::Event(string dat_n, string in_t_n, string en_n) {
    this->dat = dat_n;
    this->in_t = in_t_n;
    this->en = en_n;
};
string Event::Get_dat() {
    return this->dat;
};
string Event::Get_in_t() {
    return this->in_t;
};
string Event::Get_en() {
    return this->en;
};
Birthday::Birthday() {};
string Birthday::Get_PIB() {
    return this->PIB;
};
int Birthday::Get_age() {
    return this->age;
};
string Birthday::Get_place() {
    return this->place;
};
Meeting::Meeting() {};
string Meeting::Get_PIB() {
    return this->PIB;
};
string Meeting::Get_place() {
    return this->place;
};
string Event::Last_calc(string time_n) {
    string H;
    string F;
    int min = 0;
    F = time_n;
    H = F.substr(0, 2);
    min += stoi(H) * 60;
    H = F.substr(3, 2);
    min += stoi(H);
    int d = 0;
    F = this->in_t;
    H = F.substr(0, 2);
    d += stoi(H) * 60;
    H = F.substr(3, 2);
    d += stoi(H);
    F = this->en;
    H = F.substr(0, 2);
    d += stoi(H) * 60;
    H = F.substr(3, 2);
    d += stoi(H);
    min -= d;
    string R = "";
    if (min > 0) {
        d = min / 60;
        R += to_string(d) + ':';
        d = min % 60;
        R += to_string(d);
        R += " will left to the party!";
    }
    else {
        R += "Party will have begun!";
    }
    return R;
};