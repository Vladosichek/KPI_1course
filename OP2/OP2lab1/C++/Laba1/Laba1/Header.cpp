#include "Header.h"
void fill(char* A, char* Q, int q) {
	ifstream outp(A);
	ofstream fill(Q);
	string line = "";
	bool t = 0;
	while (!outp.eof()) {
		if (t) {
			line.insert(line.length(), 1, '\n');
		}
		if (t == 0) {
			t = 1;
		}
		fill << line;
		line = "";
		getline(outp, line);
		int i = 0;
		while (line[i] == ' ') {
			line.erase(i, 1);
		}
		i = line.length() - 1;
		if (i >= 0) {
			while (line[i] == ' ') {
				line.erase(i, 1);
				i--;
			}
		}
		i = 0;
		while (line[i] != '\0') {
			if (line[i] == ' ' && line[i + 1] == ' ') {
				line.erase(i, 1);
				i--;
			}
			i++;
		}
		i = 0;
		int c = 0;
		while (line[i] != '\0') {
			if (line[i] == ' ') {
				c++;
			}
			i++;
		}
		i = 0;
		int h;
		h = q - line.length();
		if (h > 0) {
			if (!c) {
				line.insert(i, h, ' ');
			}
			else {
				int h1 = h / c;
				int h2 = h % c;
				while (line[i] != '\0') {
					if (line[i] == ' ') {
						line.insert(i, h1, ' ');
						i += h1;
						if (h2 > 0) {
							line.insert(i, 1, ' ');
							i++;
							h2--;
						}
					}
					i++;
				}
			}
		}
	}
	fill << line;
	outp.close();
	fill.close();
}
void out(char* A) {
	ifstream outp(A);
	string line;
	cin.ignore();
	while (!outp.eof()) {
		line = "";
		getline(outp, line);
		cout << line << endl;
	}
	outp.close();
}
void add(char* A, char sym) {
	if (sym == 'Y') {
		cout << "   Add text to file 1:\n";
		ofstream inp(A, ios::app);
		string text;
		getline(cin, text, (char)19);
		inp << text;
		inp.close();
	}
}
void write(char* A) {
	ofstream inp(A);
	string text;
	getline(cin, text, (char)19);
	inp << text;
	inp.close();
}