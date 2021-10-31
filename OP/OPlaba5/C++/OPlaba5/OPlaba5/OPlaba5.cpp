#include<iostream>
#include<cstdlib>
#include<cmath>
#include<float.h>
using namespace std;

int main()
{
    float a;
    int n = 2;
    int max = 0;
    int min = 0;
    cout << "Enter the number: ";
    cin >> a;
    int i = 2;
    if (a < 2)
    {
        cout << "The nearest max: 2" << endl;
    }
    else
    {
        while (max <= a)
        {
            for (i = 2; n; i += 1)
            {
                if (n % i == 0)
                {
                    max = i;
                    break;
                }
            }
            n += 1;
        }
        n = a;
        while (min != i)
        {
            for (i = 2; n; i += 1)
            {
                if (n % i == 0)
                {
                    min = n;
                    break;
                }
            }
            n -= 1;
        }
        if (max - a > a - min)
        {
            cout << "The nearest min: ""The nearest min: " << min << endl;
        }
        else
        {
            cout << "The nearest max: " << max << endl;
        }
    }
}