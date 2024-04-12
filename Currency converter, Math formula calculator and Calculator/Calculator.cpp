#include <iostream>
using namespace std;
	
int main()
{
	//beginning of user login

	cout << "hello" << endl;
	cout << "what is your name?" << endl;

	string FirstName;
	cin >> FirstName;

	cout << "Great " << FirstName << ", whats your last name?" << endl;

	string SecondName;
	cin >> SecondName;

	cout << "is your name " << FirstName << " " << SecondName << "? if not then type 0 to restart or enter 1 to continue" << endl;

	int OptionUser;
	cin >> OptionUser;

	if (OptionUser == 0) {
		return 0;
	}

	// end of user login


	// i had a "int Calculator();" class, but i wasnt sure how to start it so i took it out.
	// some variables defined here

	int divisor, dividend, quotient, remainder;
	float FirstNumber = 0, SecondNumber = 0, sum = 0;
	int Option;

	// list of functions, disorganised but ill get better

	main; void addition(); {

		sum = FirstNumber + SecondNumber;

		cout << sum << endl;
	}

	main; void multiplication(); {

		sum = FirstNumber * SecondNumber;

		cout << sum << endl;
	}

	main; void division(); {

		sum = FirstNumber / SecondNumber;

		cout << sum << endl;
	}

	main; void quotent(); {

		cout << "Enter dividend: ";
		cin >> dividend;

		cout << "Enter divisor: ";
		cin >> divisor;

		quotient = dividend / divisor;
		remainder = dividend % divisor;

		cout << "Quotient = " << quotient << endl;
		cout << "Remainder = " << remainder;

		cout << sum << endl;
	}

	// end of functions

	cout << "What function would you like to perform with the calculator " << FirstName << "?" << endl;
	cout << "type 1 for addition, 2 for multiplication, 3 for division and 4 for quotent/remainder." << endl;

	cin >> Option;

	if (Option == 1) {
		addition();
		return 0;
	}

	if (Option == 2) {
		multiplication();
		return 0;
	}

	if (Option == 3) {
		division();;
		return 0;
	}

	if (Option == 4) {
		quotent();
		return 0;
	}


		cout << "Enter your first number" << endl;
		cin >> FirstNumber;

		cout << "Enter your second number" << endl;
		cin >> SecondNumber;

		return 0;

	
}
	




