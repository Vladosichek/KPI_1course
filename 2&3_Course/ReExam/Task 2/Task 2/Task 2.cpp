/*Ввести текст, що містить декілька рядків.

У кожному рядку тексту усі входження вказаного символу замінити на «*».

Видалити із рядків зміненого тексту слова, які починаються з символу «*».

Підрахувати кількість слів у зміненому тексті. */
#include "Header.h"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n;
    cout << "Enter n: ";
    cin >> n;
    string* T = gen(n);
    char sym;
    cout << "Enter symbol:";
    cin >> sym;
    change(T, n, sym);
    outt(T, n);
    del(T, n);
    outt(T, n);
    int amm = count(T, n);
    cout << "Ammount of words in new text is " << amm << endl;
    delete[] T;
    return 0;
    system("pause");
}
