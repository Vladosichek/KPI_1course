#pragma once
#include <iostream>
#include <string>
using namespace std;
struct Branch
{
	string Info;
	int Cost;
	int Amm;
	Branch* Left;
	Branch* Right;
};
int calc(Branch*&);
void FT(Branch*);
void add_elem(string, int, int, Branch*&);
void oubt(Branch*, int);