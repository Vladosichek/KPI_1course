#include <iostream>
#include "Position.h"
using namespace std;
namespace Records {
	const int kMaxPositions = 100;
	const int kFirstPositionNumber = 1;
	class Database
	{
	public:
		Database();
		~Database();
		Position& addPosition(string inCode, string inName, int inSalary, string inDuties, string inRequirements);
		Position& getPosition(int inPositionNumber);
		Position& getPosition(string inName);
		void displayAll();
	protected:
		Position mPosition[kMaxPositions];
		int mNextSlot;
		int mNextPositionNumber;
	};
}