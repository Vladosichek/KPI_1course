#include "Header.h"
#include <iostream>
using namespace std;
int main()
{
	char Text1[] = "text1.txt";
	char Text2[] = "text2.txt";
	cout << "   Enter - end of line\n   Ctrl + S - end of file (after Ctrl + S enter Enter to finish writing the text)\n";
	write(Text1);
	cout << "   If you want to add to file press Y, else - press any other symbol and press Enter: ";
	char Question;
	cin >> Question;
	add(Text1, Question);
	cout << "   Full text of file 1:\n";
	out(Text1);
	cout << "   Enter ammount of symbols:";
	int amm;
	cin >> amm;
	cout << "   Full text of file 2:\n";
	fill(Text1, Text2, amm);
	out(Text2);
	return 0;
	system("pause");
}
