#include <iostream>
#include <string>
#include "Position.h"

using namespace std;
namespace Records {
	Position::Position()
	{
		pCode = "";
		pName = "";
		pSalary = 0;
		pDuties = "";
		pRequirements = "";
	}
	Position::Position(string inCode, string inName, int inSalary, string inDuties, string inRequirements)
	{
		this->pCode = inCode;
		this->pName = inName;
		this->pSalary = inSalary;
		this->pDuties = inDuties;
		this->pRequirements = inRequirements;
	}

	void Position::sRaise(int num)
	{
		if (pSalary + num >= 0) {
			pSalary += num;
		}
		else {
			cout << "Wrong input!\n";
		}
	}
	void Position::sLower(int num)
	{
		if (pSalary - num >= 0) {
			pSalary -= num;
		}
		else {
			cout << "Wrong input!\n";
		}
	}
	void Position::display()
	{
		cout << "Number: " << getNumber() << endl;
		cout << "Position: " << getName() << endl;
		cout << "-------------------------" << endl;
		cout << "Code: " << getCode() << endl;
		cout << "Salary: " << getSalary() << endl;
		cout << "Duties: " << getDuties() << endl;
		cout << "Requirements: " << getRequirements() << endl;
		cout << endl;
	}
	// Accessors and setters
	void Position::setCode(string inCode)
	{
		pCode = inCode;
	}
	string Position::getCode()
	{
		return pCode;
	}

	void Position::setName(string inName)
	{
		pName = inName;
	}
	string Position::getName()
	{
		return pName;
	}

	void Position::setSalary(int inSalary)
	{
		if (inSalary >= 0) {
			pSalary = inSalary;
		}
		else {
			cout << "Wrong input!\n";
		}
	}
	int Position::getSalary()
	{
		return pSalary;
	}

	void Position::setDuties(string inDuties)
	{
		pDuties = inDuties;
	}
	string Position::getDuties()
	{
		return pDuties;
	}

	void Position::setRequirements(string inRequirements)
	{
		pRequirements = inRequirements;
	}
	string Position::getRequirements()
	{
		return pRequirements;
	}
	void Position::setNumber(int inNumber)
	{
		pNumber = inNumber;
	}
	int Position::getNumber()
	{
		return pNumber;
	}
}