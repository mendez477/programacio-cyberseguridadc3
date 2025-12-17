#include <iostream>
using namespace std;

int main()
{
    int multiplicador;
    int inicio =1;
    int fin =12;
    cout << "ingrese el numero que desee multiplicar: ";
    cin>> multiplicador;
    for (int i=inicio; i<fin;i++){
        cout  << multiplicador << " x " << i << " = " << multiplicador * i << endl;

    }

    cin.get();
    cin.ignore();
    return 0;
}
