#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	int Numer = 0;
	int Salary = 0;
	bool Actual = true;
	string Code = "";
	string Name = "";
	string Duties = "";
	string Requirements = "";

	int TotalAmount = 0;
	string Selection = "";
	int SelectionInt = 0;
	bool IsDone = false;
	while (!IsDone) {
		cout << "1) Add a new position" << endl << "2) Deactualise the position" << endl << "3) Raise salary" << endl << "4) Lower salary" << endl << "5) List all positions" << endl << "6) List all actual positions" << endl
			<< "7) List all unactual positions" << endl << "0) Quit" << endl << "---> ";
		cin >> Selection;
		try {
			SelectionInt = stoi(Selection);
		}
		catch (exception ex) {
			SelectionInt = -1;
		}
		switch (SelectionInt) {
		case 1:
			cout << "Add";
			break;
		case 0:
			IsDone = true;
			break;
		default:
			cerr << "Unknown command." << endl;
		}
	}

}