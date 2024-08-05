/*Побудувати ієрархію класів відповідно наведеній схемі успадкування. Кожен клас повинен мати власний атрибут типу int, 
згенерований випадковим чином, містити конструктор, метод виведення об’єкта відповідного класу, можливо інші методи. 
Також спроектувати клас Set для представлення множини цілих чисел (обов'язково унікальних і впорядкованих). 
Визначити у класі конструктор (конструктори), методи для виконання поставленого завдання. Створити два об’єкта: 
класу D3 і класу D4. Зберегти значення атрибутів об’єкта класу D3 у множині М3, а атрибутів об’єкта класу D4 у множині М4. 
Визначити максимальне значення серед елементів множини М, сформованої наступним чином: М = (М3∪М4) \ (М3∩М4). 
Програма повинна забезпечувати наочне виведення усіх вхідних, 
вихідних та проміжних даних, а також контроль можливих помилок. Для обробки помилок використати виключні ситуації.*/
#include <iostream>
#include <iostream>
#include "Header.h"
class Set {
    int* arr;
    int size;
    int am;
public:
    Set() {
        size = 10;
        arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = NULL;
        }
        am = 0;
    }
    Set(Set A1, Set A2) {
        size = 10;
        arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = NULL;
        }
        am = 0;
        Set h;
        Set h1;
        Set h2;
        for (int i = 0; i < A1.am; i++) {
            h.Insert(A1.Get(i));
        }
        for (int i = 0; i < A2.am; i++) {
            h.Insert(A2.Get(i));
        }
    }
    int Get(int a) {
        if (a >= am) {
            a = am - 1;
        }
        return arr[a];
    }
    void Insert(int a) {
        bool f = 1;
        for (int i = 0; i < am; i++) {
            if (a == arr[i]) {
                f = 0;
            }
        }
        if (f == 1) {
            int i = 0;
            if (am == size) {
                int* h = new int[2 * size];
                size *= 2;
                for (int i = 0; i < am; i++) {
                    h[i] = arr[i];
                }
                delete[] arr;
                arr = h;
                delete[] h;
            }
            while (arr[i] < a && i<am) {
                i++;
            }
            arr[i] = a;
            am++;
        }
    }
    int Max() {
        int max = -1;
        for (int i = 0; i < am; i++) {
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        return max;
    }
    /*void Out() {
        for (int i = 0; i < am; i++) {
            cout << arr[i] << " ";
        }
    }*/
};
class D1 : public B {
    int par;
public:
    D1(){
        srand(time(NULL));
        par = rand() % 50;
    };
    int Get() {
        return this->par;
    }
};
class D2 : private B {
    int par;
public:
    D2() {
        srand(time(NULL));
        par = rand() % 50;
    };
    int Get() {
        return this->par;
    }
};
class D3 : private D1, public D2 {
    int par;
public:
    D3() {
        srand(time(NULL));
        par = rand() % 50;
    };
    int Get() {
        return this->par;
    }
};
class D4 : private D1, public D2 {
    int par;
public:
    D4() {
        srand(time(NULL));
        par = rand() % 50;
    };
    int Get() {
        return this->par;
    }
};
class B {
    int par;
public:
    B() {
        srand(time(NULL));
        par = rand() % 50;
    };
    int Get() {
        return this->par;
    }
};
using namespace std;
int main()
{
    D3 Obj1 = D3();
    D4 Obj2 = D4();
    Set M3 = Set();
    Set M4 = Set();
    M3.Insert(Obj1.Get());
    M4.Insert(Obj2.Get());
}
