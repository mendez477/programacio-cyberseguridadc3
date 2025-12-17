#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Ingrese  el primer valor: ";
    cin >> a ;
    cout << "ingrese el segundo valor: ";
    cin >> b;

    cout << "Suma: " << a + b << endl;
    cout << "Resta: " << a - b << endl;
    cout << "Multiplicacion: " << a * b << endl;

    if (b != 0)
        cout << "Division: " << (float)a / b << endl;
    else
        cout << "Error: division por cero" << endl;

    cin.get(); // espera Enter
    cin.get(); // espera Enter otra vez
    return 0;
}

