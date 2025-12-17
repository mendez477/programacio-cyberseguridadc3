#include <iostream>
using namespace std;

struct factura
{
   string nombre_del_producto;
   float precion;
   int cantidad;
};

int main()
{
    factura p[5];
    float total =0;
    for (int i= 0; i <5; i++){
     cout << "ingrese el nombre del producto: ";
     cin >> p[i].nombre_del_producto;
     cout << "precio del producto: ";
     cin >>p[i].precion;
     cout << "ingrese la cantidad de productos: ";
     cin >>p[i].cantidad;
     total+= p[i].precion* p[i].cantidad;
    }
    cout << "el valor total del la factura es  :"<< total << endl;
    cin.get();
    cin.ignore();
}
