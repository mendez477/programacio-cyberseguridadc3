#Ingresa el monto de una compra. Si es mayor a 500 aplica un 10% de descuento, sino paga precio normal.
total = float(input("ingrese el valor total de la compra: "))

if total > 500:
    descuento = total * 0.10
    entoces = total-descuento
    print("aplica el descuento del 10% ", entoces)
else: 
    print("no se aplica el descuento", total)