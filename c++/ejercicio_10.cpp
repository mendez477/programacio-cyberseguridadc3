#include <iostream>
using namespace std;

int main() {
    int num, pares = 0, impares = 0;
    for (int i = 0; i < 10; i++) {
        cout << "Numero " << i+1 << ": ";
        cin >> num;
        if (num % 2 == 0) pares++;
        else impares++;
    }
    cout << "Pares: " << pares << ", Impares: " << impares << endl;
    cin.get();
    cin.ignore();
    return 0;
}
