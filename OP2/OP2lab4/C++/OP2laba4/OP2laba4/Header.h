#pragma once
#include <iostream>
#include <cmath>
using namespace std;
class Segment {
private:
    int X_init;
    int Y_init;
    int X_fin;
    int Y_fin;
public:
    Segment();
    Segment(int X_fin, int Y_fin);
    Segment(int X_init, int Y_init, int X_fin, int Y_fin);
    int Get_X_init();
    int Get_Y_init();
    int Get_X_fin();
    int Get_Y_fin();
    float len_calc();
    Segment operator ++();
    bool operator ||(Segment obj);
};
void out_seg(Segment);