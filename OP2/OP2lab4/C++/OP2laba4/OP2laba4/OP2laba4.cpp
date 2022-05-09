#include "Header.h"
#include <iostream>
using namespace std;
int main()
{
    int x2f, y2f, x3i, y3i, x3f, y3f;
    cout << "Creating line segments:\nSegment_1:\nInitial coordinates:\nX:0\nY:0\n";
    cout << "Final coordinates:\nX:5\nY:5\nSegment_2:\nInitial coordinates:\nX:1\nY:-1\n";
    cout << "Final coordinates:\nX:";
    cin >> x2f;
    cout << "Y:";
    cin >> y2f;
    cout << "Segment_3:\nInitial coordinates:\nX:";
    cin >> x3i;
    cout << "Y:";
    cin >> y3i;
    cout << "Final coordinates:\nX:";
    cin >> x3f;
    cout << "Y:";
    cin >> y3f;
    Segment B1 = Segment();
    Segment B2 = Segment(x2f, y2f);
    Segment B3 = Segment(x3i, y3i, x3f, y3f);
    cout << "Are B1 and B2 ||?\nB1:\n";
    out_seg(B1);
    cout << "B2:\n";
    out_seg(B2);
    bool que = B1 || B2;
    if (que == 1) {
        cout << "B1 and B2 are ||\n";
    }
    else {
        cout << "B1 and B2 are not ||\n";
    }
    cout << "How long is NEW B3?\nOLD B3:\n";
    out_seg(B3);
    cout << "NEW B3:\n";
    ++B3;
    out_seg(B3);
    float leng = B3.len_calc();
    cout << "Length of NEW B3 is " << leng << endl;
    system("pause");
    return 0;
}