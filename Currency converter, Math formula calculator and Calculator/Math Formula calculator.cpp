#include <iostream>
#include <cmath>
using std::cout;
using std::cin;

//defining variables
double Area, Perimeter, Side1, Side2, Side3;

// circles
double Radius, Circumf;
double const Pi = 3.141592653589793238;

// triangles
double Base, Height;

//end of declarations

//circle functions
void CircleArea() {
	double RadiusSqr = pow(Radius, 2);
	Area = RadiusSqr * Pi;
}

void CircleCircumf() {
	Circumf = 2 * Pi * Radius;
}

// square functions
void SquareArea() {
	Area = Side1 * Side1;
}

void SquarePerimeter() { 
	Perimeter = Side1 + Side1 + Side1 + Side1;
}

// triangle functions
void TriangleArea() {
	Area = 0.5 * Base * Height;
}

void TrianglePerimeter() {
	Perimeter = Side1 + Side2 + Side3;
}


// main function
int main() {
	cout << "This is a circles, triangles and squares formula calculator." << '\n';
	cout << "To begin, begin with entering what shape you have." << '\n' << '\n';

	cout << "If you have a circle, enter 1:" << '\n' << "If you have a square, enter 2:" << '\n' << "If you have a triangle, enter 3:" << '\n';
	int Option;
	cin >> Option;

	cout << "If you want to find the area of the shape, enter 1:" << '\n' << "If you want to find the perimeter (or circumference for circles), enter 2:" << '\n';
	int FormOpt;
	cin >> FormOpt;

	switch (Option) {
	case 1:
		if (FormOpt == 1) {
			cout << "Enter the Radius of the circle (half the diameter):" << '\n';
			cin >> Radius;
			CircleArea(); //call function
			cout << "The Area of your circle is: " << Area << '\n';
		}
		else if (FormOpt == 2) {
			cout << "Enter the Radius of the circle (half the diameter):" << '\n';
			cin >> Radius;
			CircleCircumf();
			cout << "The Circumference of your circle is: " << Circumf << '\n';
		}
		else {
			return 0;
		}

		break;

	case 2:
		if (FormOpt == 1) {
			cout << "Enter 1 side of your square:" << '\n';
			cin >> Side1;
			SquareArea();
			cout << "The Area of your square is: " << Area << '\n';
		}
		else if (FormOpt == 2) {
			cout << "Enter 1 side of your square" << '\n';
			cin >> Side1;
			SquarePerimeter();
			cout << "The Perimeter of your square is: " << Perimeter << '\n';
		}
		else {
			return 0;
		}

		break;

	case 3:
		if (FormOpt == 1) {
			cout << "Enter the Base, then enter the Height of your triangle:" << '\n';
			cin >> Base >> Height;
			TriangleArea();
			cout << "The Area of your triangle is: " << Area << '\n';
		}
		else if (FormOpt == 2) {
			cout << "Enter the 3 sides your triangle:" << '\n';
			cin >> Side1 >> Side2 >> Side3;
			TrianglePerimeter();
			cout << "The Perimeter of your triangle is: " << Perimeter << '\n';
		}
		else {
			return 0;
		}

		break;

	default:
		cout << "Please restart the program";
		return 0;
	}

	return 0;
}