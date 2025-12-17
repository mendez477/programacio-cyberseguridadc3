#include <iostream>
using namespace std;

struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};

int main() {
    Estudiante e[3];
    float mejor;
    string mejorNombre;

    // Primer estudiante para inicializar
    cout << "Nombre: ";
    cin >> e[0].nombre;
    cout << "Edad: ";
    cin >> e[0].edad;
    cout << "Promedio: ";
    cin >> e[0].promedio;

    mejor = e[0].promedio;
    mejorNombre = e[0].nombre;

    // Los otros dos
    for (int i = 1; i < 3; i++) {
        cout << "Nombre: ";
        cin >> e[i].nombre;
        cout << "Edad: ";
        cin >> e[i].edad;
        cout << "Promedio: ";
        cin >> e[i].promedio;

        if (e[i].promedio > mejor) {
            mejor = e[i].promedio;
            mejorNombre = e[i].nombre;
        }
    }

    cout << "Mejor promedio: " << mejor << " (" << mejorNombre << ")\n";

    cin.get();
    cin.get();
    cin.ignore();
    return 0;
}
