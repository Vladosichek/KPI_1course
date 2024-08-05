#include <iostream>
#include <stdexcept>
#include <string>
#include "Database.h"
using namespace std;
namespace Records {
	Database::Database()
	{
		mNextSlot = 0;
		mNextPositionNumber = kFirstPositionNumber;
	}
	Database::~Database()
	{
	}
	Position& Database::addPosition(string inCode, string inName, int inSalary, string inDuties, string inRequirements)
	{
		if (mNextSlot >= kMaxPositions) {
			cerr << "There is no more room to add the new position!" << endl;
			throw exception();

		}
		Position& thePosition = mPosition[mNextSlot++];
		thePosition.setCode(inCode);
		thePosition.setName(inName);
		thePosition.setSalary(inSalary);
		thePosition.setDuties(inDuties);
		thePosition.setRequirements(inRequirements);
		thePosition.setNumber(mNextPositionNumber++);

		return thePosition;
	}

	Position& Database::getPosition(int inPositionNumber)
	{
		for (int i = 0; i < mNextSlot; i++) {
			if (mPosition[i].getNumber() == inPositionNumber) {
				return mPosition[i];
			}
		}
		cerr << "No position with number " << inPositionNumber << endl;
		throw exception();
	}

	Position& Database::getPosition(string inName)
	{
		for (int i = 0; i < mNextSlot; i++) {
			if (mPosition[i].getName() == inName) {
				return mPosition[i];
			}
		}
		cerr << "No match with name " << inName << endl;
		throw exception();
	}

	void Database::displayAll()
	{
		for (int i = 0; i < mNextSlot; i++) {
			mPosition[i].display();
		}
	}
}