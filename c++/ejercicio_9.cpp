#include <iostream>
using namespace std;

int main() {
    int opcion, a, b;
    do {
        cout << "\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Salir\nOpcion: ";
        cin >> opcion;
        if (opcion >= 1 && opcion <= 3) {
            cout << "Ingrese un numeros: ";
            cin >> a;
            cout << "ingrese un numero: ";
            cin >> b;
        }
        switch (opcion) {
            case 1: cout << "Suma: " << a + b << endl; break;
            case 2: cout << "Resta: " << a - b << endl; break;
            case 3: cout << "Multiplicacion: " << a * b << endl; break;
        }
    } while (opcion != 4);
    return 0;
}
