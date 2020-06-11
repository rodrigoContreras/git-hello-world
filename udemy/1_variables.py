#variables
print ("Datos de una persona")
print ("....................")
print("")
nombreProducto1 = input("ingrese nombre producto 1 :")
valorProducto1 = int(input("ingrese valor producto 1"))

nombreProducto2 = input("ingrese nombre producto 2:")
valorProducto2 = int (input("ingrese valor Producto 2"))


BONIFICACION = 20

comparar = (valorProducto1 == valorProducto2)

print(comparar)

print(valorProducto1 * BONIFICACION)
#CONCATENAR

cabecera = "nombre1: {0} + nombre2: {1}"
print(cabecera.format(nombreProducto1, nombreProducto2))

#INCREMENTAR

sumaValores = valorProducto1 + valorProducto2
sumaValores += BONIFICACION

print ("vsuma de valores + bonifiacion : " + str(sumaValores))