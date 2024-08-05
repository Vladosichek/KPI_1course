#include <iostream>

using namespace std;

namespace Records {

	class Position
	{
	public:
		Position();
		Position(string inCode, string inName, int inSalary, string inDuties, string inRequirements);
		void sRaise(int num);
		void sLower(int num);
		void display();
		// Accessors and setters
		void setCode(string inCode);
		string getCode();
		void setName(string inName);
		string getName();
		void setSalary(int inSalary);
		int getSalary();
		void setDuties(string inDuties);
		string getDuties();
		void setRequirements(string inRequirements);
		string getRequirements();
		void setNumber(int inNumber);
		int getNumber();
	private:
		string pCode;
		string pName;
		int pSalary;
		string pDuties;
		string pRequirements;
		int pNumber;
	};
}