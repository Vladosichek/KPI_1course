#include "Header.h"
void oubt(Branch* Element, int tabs)
{
	if (!Element) {
	}
	else {
		tabs += 3;
		oubt(Element->Left, tabs);
		for (int i = 0; i < tabs; i++) cout << " ";
		cout << Element->Info << "|" << Element->Cost << " per 1 piece|" << Element->Amm << " pieces" << endl;
		oubt(Element->Right, tabs);
		tabs -= 3;
	}
}
void add_elem(string Data, int cn, int amn, Branch*& Element)
{
	if (!Element)
	{
		Element = new Branch;
		Element->Info = Data;
		Element->Cost = cn;
		Element->Amm = amn;
		Element->Left = 0;
		Element->Right = 0;
	}
	else
	{
		if ((Element->Cost * Element->Amm) < (cn * amn)) {
			add_elem(Data, cn, amn, Element->Right);
		}
		else {
			add_elem(Data, cn, amn, Element->Left);
		}
	}
}
void FT(Branch* Element)
{
	if (!Element) {
	}
	else {
		FT(Element->Left);
		FT(Element->Right);
		delete Element;
	}
}
int calc(Branch*& Element) 
{
	int a = 0;
	if (!Element) {
	}
	else {
		a = Element->Cost * Element->Amm + calc(Element->Left) + calc(Element->Right);
	}
	return a;
}