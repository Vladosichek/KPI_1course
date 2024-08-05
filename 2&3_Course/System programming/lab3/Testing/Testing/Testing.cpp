#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void doAdd(string FName, int& Amount);
void doRetire();
void doRaise();
void doLower();
void doAll(string FName);
void doAllActual(string FName);
void doAllUnactual(string FName);

int main() {
	int Numer = 0;
	int Salary = 0;
	bool Actual = true;
	string Code = "";
	string Name = "";
	string Duties = "";
	string Requirements = "";

	int TotalAmount = 0;
	string FileName = "records.txt";
	string HelpLine = "";
	ifstream MyFile(FileName);
	if (!MyFile.is_open()) {
		cerr << "File does not exist!";
		return 0;
	}
	while (getline(MyFile, HelpLine)) {
		TotalAmount++;
	}
	MyFile.close();
	TotalAmount /= 7;

	string Selection = "";
	int SelectionInt = 0;
	bool IsDone = false;
	while (!IsDone) {
		cout << "1) Add a new position" << endl << "2) Deactualise the position" << endl << "3) Raise salary" << endl 
			<< "4) Lower salary" << endl << "5) List all positions" << endl << "6) List all actual positions" << endl
			<< "7) List all unactual positions" << endl << "0) Quit" << endl << "---> ";
		getline(cin, Selection);
		try {
			SelectionInt = stoi(Selection);
		}
		catch (exception ex) {
			SelectionInt = -1;
		}
		switch (SelectionInt) {
		case 1:
			doAdd(FileName, TotalAmount);
			break;
		case 2:
			doRetire();
			break;
		case 3:
			doRaise();
			break;
		case 4:
			doLower();
			break;
		case 5:
			doAll(FileName);
			break;
		case 6:
			doAllActual(FileName);
			break;
		case 7:
			doAllUnactual(FileName);
			break;
		case 0:
			IsDone = true;
			break;
		default:
			cerr << "Unknown command." << endl;
		}
	}
	return 0;
}

void doLower() {
	ifstream MyFile("records.txt");
	ofstream HelpFile("helpfile.txt");
	string Position;
	string Code;
	string Name;
	string Salary;
	string Duties;
	string Requirements;
	string Actual;
	string HelpLine = "";
	bool IsExec = false;
	bool IsStart = true;
	int Helpint = 0;
	int Recordnum = 0;
	int Amount = 0;
	cout << "Number of position: ";
	getline(cin, HelpLine);
	try {
		Recordnum = stoi(HelpLine);
	}
	catch (exception ex) {
		Recordnum = -1;
	}
	cout << "Amount: ";
	getline(cin, HelpLine);
	try {
		Amount = stoi(HelpLine);
	}
	catch (exception ex) {
		Amount = 0;
	}
	while (getline(MyFile, Position)) {
		getline(MyFile, Code);
		getline(MyFile, Name);
		getline(MyFile, Salary);
		getline(MyFile, Duties);
		getline(MyFile, Requirements);
		getline(MyFile, Actual);
		if (!IsStart) {
			HelpFile << endl;
		}
		IsStart = false;
		HelpFile << Position << endl << Code << endl << Name << endl;
		if (stoi(Position) == Recordnum) {
			IsExec = true;
			Helpint = stoi(Salary) - Amount;
			if (Helpint < 0) {
				Helpint = 0;
			}
			HelpFile << Helpint;
		}
		else {
			HelpFile << Salary;
		}
		HelpFile << endl << Duties << endl << Requirements << endl << Actual;
	}
	MyFile.close();
	HelpFile.close();
	remove("records.txt");
	rename("helpfile.txt", "records.txt");
	if (!IsExec) {
		cout << "Record is not found!\n";
	}
}

void doRaise() {
	ifstream MyFile("records.txt");
	ofstream HelpFile("helpfile.txt");
	string Position;
	string Code;
	string Name;
	string Salary;
	string Duties;
	string Requirements;
	string Actual;
	string HelpLine = "";
	bool IsExec = false;
	bool IsStart = true;
	int Helpint = 0;
	int Recordnum = 0;
	int Amount = 0;
	cout << "Number of position: ";
	getline(cin, HelpLine);
	try {
		Recordnum = stoi(HelpLine);
	}
	catch (exception ex) {
		Recordnum = -1;
	}
	cout << "Amount: ";
	getline(cin, HelpLine);
	try {
		Amount = stoi(HelpLine);
	}
	catch (exception ex) {
		Amount = 0;
	}
	while (getline(MyFile, Position)) {
		getline(MyFile, Code);
		getline(MyFile, Name);
		getline(MyFile, Salary);
		getline(MyFile, Duties);
		getline(MyFile, Requirements);
		getline(MyFile, Actual);
		if (!IsStart) {
			HelpFile << endl;
		}
		IsStart = false;
		HelpFile << Position << endl << Code << endl << Name << endl;
		if (stoi(Position) == Recordnum) {
			IsExec = true;
			Helpint = stoi(Salary) + Amount;
			if (Helpint < 0) {
				Helpint = 0;
			}
			HelpFile << Helpint;
		}
		else {
			HelpFile << Salary;
		}
		HelpFile << endl << Duties << endl << Requirements << endl << Actual;
	}
	MyFile.close();
	HelpFile.close();
	remove("records.txt");
	rename("helpfile.txt", "records.txt");
	if (!IsExec) {
		cout << "Record is not found!\n";
	}
}

void doRetire() {
	ifstream MyFile("records.txt");
	ofstream HelpFile("helpfile.txt");
	string Position;
	string Code;
	string Name;
	string Salary;
	string Duties;
	string Requirements;
	string Actual;
	string HelpLine = "";
	bool IsExec = false;
	bool IsStart = true;
	int Recordnum = 0;
	cout << "Number of position: ";
	getline(cin, HelpLine);
	try {
		Recordnum = stoi(HelpLine);
	}
	catch (exception ex) {
		Recordnum = -1;
	}
	while (getline(MyFile, Position)) {
		getline(MyFile, Code);
		getline(MyFile, Name);
		getline(MyFile, Salary);
		getline(MyFile, Duties);
		getline(MyFile, Requirements);
		getline(MyFile, Actual);
		if (!IsStart) {
			HelpFile << endl;
		}
		IsStart = false;
		HelpFile << Position << endl << Code << endl << Name << endl << Salary << endl << Duties << endl << Requirements << endl;
		if (stoi(Position) == Recordnum) {
			HelpFile << "false";
			IsExec = true;
		}
		else {
			HelpFile << Actual;
		}
	}
	MyFile.close();
	HelpFile.close();
	remove("records.txt");
	rename("helpfile.txt", "records.txt");
	if (!IsExec) {
		cout << "Record is not found!\n";
	}
}

void doAllUnactual(string FName) {
	ifstream MyFile(FName);
	string Position;
	string Code;
	string Name;
	string Salary;
	string Duties;
	string Requirements;
	string Actual;
	while (getline(MyFile, Position)) {
		getline(MyFile, Code);
		getline(MyFile, Name);
		getline(MyFile, Salary);
		getline(MyFile, Duties);
		getline(MyFile, Requirements);
		getline(MyFile, Actual);
		if (Actual == "false") {
			cout << "Position: " << Position << endl;
			cout << "Code: " << Code << endl;
			cout << "Name: " << Name << endl;
			cout << "Salary: " << Salary << endl;
			cout << "Duties: " << Duties << endl;
			cout << "Requirements: " << Requirements << endl;
			cout << "Position is not actual!\n\n";
		}
	}
	MyFile.close();
}

void doAllActual(string FName) {
	ifstream MyFile(FName);
	string Position;
	string Code;
	string Name;
	string Salary;
	string Duties;
	string Requirements;
	string Actual;
	while (getline(MyFile, Position)) {
		getline(MyFile, Code);
		getline(MyFile, Name);
		getline(MyFile, Salary);
		getline(MyFile, Duties);
		getline(MyFile, Requirements);
		getline(MyFile, Actual);
		if (Actual == "true") {
			cout << "Position: " << Position << endl;
			cout << "Code: " << Code << endl;
			cout << "Name: " << Name << endl;
			cout << "Salary: " << Salary << endl;
			cout << "Duties: " << Duties << endl;
			cout << "Requirements: " << Requirements << endl;
			cout << "Position is actual!\n\n";
		}
	}
	MyFile.close();
}

void doAll(string FName) {
	ifstream MyFile(FName);
    string HelpLine;
	while (getline(MyFile, HelpLine)) {
		cout << "Position: " << HelpLine << endl;
		getline(MyFile, HelpLine);
		cout << "Code: " << HelpLine << endl;
		getline(MyFile, HelpLine);
		cout << "Name: " << HelpLine << endl;
		getline(MyFile, HelpLine);
		cout << "Salary: " << HelpLine << endl;
		getline(MyFile, HelpLine);
		cout << "Duties: " << HelpLine << endl;
		getline(MyFile, HelpLine);
		cout << "Requirements: " << HelpLine << endl;
		getline(MyFile, HelpLine);
		if (HelpLine == "true") {
			cout << "Position is actual!\n\n";
		}
		else {
			cout << "Position is not actual!\n\n";
		}
	}
	MyFile.close();
}

void doAdd(string FName, int& Amount) {
	int Salary = 0;
	string Code;
	string Name;
	string Duties;
	string Requirements;
	string Help;

	if (Amount >= 5) {
		cout << "Unable to add new position!" << endl;
	}
	else {
		ofstream File(FName, ios::app);
		cout << "Enter data:\nCode: ";
		getline(cin, Code);
		cout << "Name: ";
		getline(cin, Name);
		cout << "Duties: ";
		getline(cin, Duties);
		cout << "Requirements: ";
		getline(cin, Requirements);
		cout << "Salary: ";
		getline(cin, Help);
		try {
			Salary = stoi(Help);
		}
		catch (exception ex) {
			Salary = 0;
		}
		if (Salary < 0) {
			Salary = 0;
		}
		if (Amount != 0) {
			File << endl;
		}
		Amount++;
		File << to_string(Amount) << endl << Code << endl << Name << endl << to_string(Salary) << endl << Duties << endl << Requirements << endl << "true";
		File.close();
	}
}