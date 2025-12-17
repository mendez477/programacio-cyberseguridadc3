#include <iostream>
using namespace std;

int main()
{
    float celsius;
    cout << "ingrese la temperatura el grado celsius: ";
    cin >> celsius ;
    float fahrenheit = (celsius * 9/5) + 32;
    cout << "su temperatura el fahrenheit es : " << fahrenheit << endl;

    cin.get();
    cin.get();
    return 0 ;
}
