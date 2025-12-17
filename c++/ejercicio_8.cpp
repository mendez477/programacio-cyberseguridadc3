#include <iostream>
using namespace std;

int main() {
    int num, suma = 0;
    while (true) {
        cout << "Ingrese un numero (0 para terminar): ";
        cin >> num;
        if (num == 0) break;
        suma += num;
    }
    cout << "Suma total: " << suma << endl;
    return 0;
}
