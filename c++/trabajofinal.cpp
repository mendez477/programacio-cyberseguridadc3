#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;

void RegistrarUsuario(vector<string>& usuarios, vector<string>& contraseñas) {
    string user, pass;
    cout << "Ingrese usuario: ";
    cin >> user;
    cout << "Ingrese contraseña: ";
    cin >> pass;
    usuarios.push_back(user);
    contraseñas.push_back(pass);
}

bool VerificarContraseña(const string& pass) {
    bool tieneMayus = false, tieneMinus = false, tieneNum = false, tieneEspecial = false;

    for (char c : pass) {
        if (isupper(c)) tieneMayus = true;
        else if (islower(c)) tieneMinus = true;
        else if (isdigit(c)) tieneNum = true;
        else tieneEspecial = true;
    }

    return (pass.length() >= 8 && tieneMayus && tieneMinus && tieneNum && tieneEspecial);
}

void GenerarAlertas(const vector<string>& usuarios, const vector<string>& contraseñas) {
    for (size_t i = 0; i < usuarios.size(); i++) {
        if (!VerificarContraseña(contraseñas[i])) {
            cout << "⚠️ Alerta: La contraseña de " << usuarios[i] << " es débil.\n";
        } else {
            cout << "✅ La contraseña de " << usuarios[i] << " es segura.\n";
        }
    }
}

int main() {
    vector<string> usuarios;
    vector<string> contraseñas;

    int opcion;
    do {
        cout << "\n1. Registrar usuario\n2. Verificar contraseñas\n3. Salir\nOpcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1: RegistrarUsuario(usuarios, contraseñas); break;
            case 2: GenerarAlertas(usuarios, contraseñas); break;
        }
    } while (opcion != 3);

    return 0;
}
