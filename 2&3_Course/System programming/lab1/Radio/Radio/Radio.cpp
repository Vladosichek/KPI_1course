#include <iostream>
#include <stdexcept>
#include <string>
#include "Database.h"
using namespace std;
using namespace Records;
int displayMenu();
void doAdd(Database& inDB);
void doRaise(Database& inDB);
void doLower(Database& inDB);

int main(int argc, char** argv)
{
	Database positionDB;
	bool done = false;
	while (!done) {
		int selection = displayMenu();
		switch (selection) {
		case 1:
			doAdd(positionDB);
			break;
		case 2:
			doRaise(positionDB);
			break;
		case 3:
			doLower(positionDB);
			break;
		case 4:
			positionDB.displayAll();
			break;
		case 0:
			done = true;
			break;
		default:
			cerr << "Unknown command." << endl;
		}
	}
}
int displayMenu()
{
	int selection;
	cout << endl;
	cout << "Position Database" << endl;
	cout << "-----------------" << endl;
	cout << "1) Add a new position" << endl;
	cout << "2) Raise salary" << endl;
	cout << "3) Lower salary" << endl;
	cout << "4) List all positions" << endl;
	cout << "0) Quit" << endl;
	cout << endl;

	cout << "---> ";
	cin >> selection;
	return selection;
}
void doAdd(Database& inDB)
{
	string Code, Name, Duties, Requirements;
	int Salary;
	cout << "Name of the position? ";
	cin >> Name;
	cout << "Code of the position? ";
	cin >> Code;
	cout << "Duties of the position? ";
	cin >> Duties;
	cout << "Requirements of the position? ";
	cin >> Requirements;
	cout << "Salary of the position? ";
	cin >> Salary;
	if (Salary < 0) {
		cout << "Wromg input!\n";
		return;
	}
	try {
		inDB.addPosition(Code, Name, Salary, Duties, Requirements);
	}
	catch (std::exception ex) {
		cerr << "Unable to add new position!" << endl;
	}
}
void doRaise(Database& inDB)
{
	int positionNumber, raiseAmount;
	cout << "Position number? ";
	cin >> positionNumber;
	try {
		Position& emp = inDB.getPosition(positionNumber);
	}
	catch (std::exception ex) {
		cerr << "Unable to find position!" << endl;
		return;
	}
	Position& emp = inDB.getPosition(positionNumber);
	cout << "Position " << emp.getName() << " salary: " << emp.getSalary() << endl;
	cout << "How much? ";
	cin >> raiseAmount;
	emp.sRaise(raiseAmount);
}
void doLower(Database& inDB)
{
	int positionNumber, lowerAmount;
	cout << "Position number? ";
	cin >> positionNumber;
	try {
		Position& emp = inDB.getPosition(positionNumber);
	}
	catch (std::exception ex) {
		cerr << "Unable to find position!" << endl;
		return;
	}
	Position& emp = inDB.getPosition(positionNumber);
	cout << "Position " << emp.getName() << " salary: " << emp.getSalary() << endl;
	cout << "How much? ";
	cin >> lowerAmount;
	emp.sLower(lowerAmount);
}