#include "Header.h"
void out_seg(Segment A) {
    cout << "Initial coordinates: X-" << A.Get_X_init();
    cout << " Y-" << A.Get_Y_init() << endl;
    cout << "Final coordinates: X-" << A.Get_X_fin();
    cout << " Y-" << A.Get_Y_fin() << endl;
}
Segment::Segment() {
    this->X_init = 0;
    this->Y_init = 0;
    this->X_fin = 5;
    this->Y_fin = 5;
};
Segment::Segment(int X_fin, int Y_fin) {
    this->X_init = 1;
    this->Y_init = -1;
    this->X_fin = X_fin;
    this->Y_fin = Y_fin;
};
Segment::Segment(int X_init, int Y_init, int X_fin, int Y_fin) {
    this->X_init = X_init;
    this->Y_init = Y_init;
    this->X_fin = X_fin;
    this->Y_fin = Y_fin;
};
int Segment::Get_X_init() {
    return this->X_init;
};
int Segment::Get_Y_init() {
    return this->Y_init;
};
int Segment::Get_X_fin() {
    return this->X_fin;
};
int Segment::Get_Y_fin() {
    return this->Y_fin;
};
float Segment::len_calc() {
    float len = 0;
    len = sqrt(pow((X_fin - X_init), 2) + pow((Y_fin - Y_init), 2));
    return len;
};
Segment Segment :: operator ++() {
    X_init++;
    Y_init++;
    return *this;
};
bool Segment ::operator ||(Segment obj) {
    bool res = 0;
    if (float((Y_fin - Y_init) / (X_fin - X_init)) == float((obj.Y_fin - obj.Y_init) / (obj.X_fin - obj.X_init))) {
        res = 1;
    }
    return res;
};