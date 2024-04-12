#include <iostream>
using std::cout;
using std::cin;

namespace USD {
	double CurrConv = 0.79;
}

namespace EUR {
	double CurrConv = 0.92;
}

namespace YEN {
	double CurrConv = 190.80;
}

int main() {
	cout << "Welcome to the £ currency converter." << '\n';
	cout << "To begin, please select an option" << '\n';

	cout << "Enter 1 for GBP to USD, Enter 2 for GBP to EUR, Enter 3 for GBP to YEN." << '\n';
	int Option;
	cin >> Option;

	cout << "Enter the amount you'd like to convert to your chosen currency:" << '\n';
	double Amount;
	cin >> Amount;

	double FinalAmount;

	switch (Option) {
	case 1:
		FinalAmount = Amount * USD::CurrConv;
		cout << "You have $" << FinalAmount;
		break;
	case 2:
		FinalAmount = Amount * EUR::CurrConv;
		cout << "You have €" << FinalAmount;
		break;
	case 3:
		FinalAmount = Amount * YEN::CurrConv;
		cout << "You have ¥" << FinalAmount;
		break;
	default:
		cout << "Please rerun the program";
		return 0;
	};
	return 0;
}