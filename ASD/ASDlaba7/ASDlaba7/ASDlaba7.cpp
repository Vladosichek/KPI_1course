#include <iostream>
#include<cmath>
using namespace std;
void fill_arr(char*, char*, int);
int fill_arr3(char*, char*, char*, int);
void output(char*, int);
int code_multiply(char*, int);
void main()
{
    const int z = 10;
    char arr1[z];
    char arr2[z];
    char arr3[z];
    fill_arr(arr1, arr2, z);
    int q;
    q = fill_arr3(arr1, arr2, arr3, z);
    cout << "Array 1: ";
    output(arr1, z);
    cout << "Array 2: ";
    output(arr2, z);
    cout << "Array 3: ";
    output(arr3, q);
    int dobutok;
    dobutok = code_multiply(arr3, q);
    cout << "Result: " << dobutok << endl;
    system("pause");
}
void fill_arr(char* p1, char* p2, int v) {
    for (int i = 0; i < v; i++) {
        p1[i] = char(100 + i);
        p2[i] = char(110 - i * i);
    }
}
int fill_arr3(char* p1, char* p2, char* p3, int v) {
    int t = 0;
    for (int i = 0; i < v; i++) {
        for (int k = 0; k < v; k++) {
            if (p1[i] == p2[k]) {
                p3[t] = p1[i];
                t++;
            }
        }
    }
    return t;
}
void output(char* p, int v) {
    for (int i = 0; i < v; i++) {
        cout << p[i] << " ";
    }
    cout << endl;
}
int code_multiply(char* p, int v) {
    int d = 1;
    for (int i = 0; i < v; i++) {
        if (int(p[i]) > 100) {
            d *= int(p[i]);
        }
    }
    return d;
}