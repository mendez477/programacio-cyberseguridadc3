#biblioteca
dispositivo_red = {
    'ip' : '192.168.1.10',
    'hostname' : 'firewall-corp',
    'estado' : 'activo'


}
#mostrar el hostname
print(" hostname del dispositivo:", dispositivo_red['hostname'])
 
 #nueva clave
dispositivo_red['ubicacion'] = 'centro_de_datos'

#cambiando valor
dispositivo_red['estado'] = 'inativo'

#valor de diccionario actual
print("\n diccionary actualizado")
for clave, valor in dispositivo_red.items():
    print(f"-{clave}:{valor}")

