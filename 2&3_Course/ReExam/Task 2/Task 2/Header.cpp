#include "Header.h"
int count(string* A, int q) {
    int c = 0;
    int y;
    for (int i = 0; i < q; i++) {
        string* Y = split(A[i], y);
        c += y;
        delete[] Y;
    }
    return c;
}
void del(string* A, int q) {
    int y;
    for (int i = 0; i < q; i++) {
        string* Y = split(A[i], y);
        for (int j = 0; j < y; j++) {
            if (Y[j][0] == '*') {
                Y[j] = "";
            }
        }
        A[i] = "";
        for (int j = 0; j < y; j++) {
            A[i] += Y[j] + " ";
        }
        delete[] Y;
    }
}
void outt(string* A, int q) {
    cout << "Text:\n";
    for (int i = 0; i < q; i++) {
        cout << A[i] << endl;
    }
}
void change(string* A, int q, char s) {
    int a = 0;
    char e = '*';
    for (int i = 0; i < q; i++) {
        while (A[i][a] != '\0') {
            if (A[i][a] == s) {
                A[i].erase(a, 1);
                A[i].insert(a, 1, e);
            }
            a++;
        }
        a = 0;
    }
}
string* split(string A, int& q) {
    string w = "";
    string* W = new string[A.length()];
    int c = 0;
    int a = 0;
    while (A[a] != '\0') {
        if (A[a] == ' ') {
            if (w.length() > 0) {
                W[c] = w;
                c++;
                w = "";
            }
        }
        else {
            w += A[a];
        }
        a++;
    }
    if (w.length() > 0) {
        W[c] = w;
        c++;
        w = "";
    }
    q = c;
    return W;
}
string* gen(int q) {
    string* A = new string[q];
    cin.ignore();
    for (int i = 0; i < q; i++) {
        getline(cin, A[i]);
    }
    return A;
}