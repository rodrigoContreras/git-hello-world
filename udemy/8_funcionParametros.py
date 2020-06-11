#FUNION ACEPRA UN PARAMETRO
def mostrarMensaje(mensaje):
    print("el mensaje es  : " + mensaje)

#NO TIENE PARAMETROS
def cargarSuma():
    val1 = int(input("Ingrese num1 : "))
    val2 = int(input("Ingrese num2 : "))
    suma = val1 +  val2
    print("La suma es : " + str(suma))

#RETORNA VALOR
def cargarSuma2():
    val3 = int(input("Ingrese num3 : "))
    val4 = int(input("Ingrese num4 : "))
    suma2 = val3 +  val4
    return suma2
    
#TIENE PARAMETRO POR DEFECTO POR SI NO SE LE ENVIA
def mensaje2(nombre, mensajeParam="hola"):
    print("Hola : " + nombre + " " + mensajeParam)

# MULTIPLES PRAMETROS
def funcionMultiplesParamatros(v1, v2, *lista):
    sumav = v1+ v2
    for i in range(len(lista)):
        sumav = sumav + lista[i]
    return sumav


# RETORNA LISTA - AGREGA DATOS A UN LISTA
def cargaLi():
    li = []
    for i in range(5):
        valorr = int(input("Valor Lista : "))
        li.append(valorr) # AGREGA DATOS A UNA LISTA
    return li

#LLAMADA A FUNCIONES
mess = input("Ingrese mensaje : ")
mostrarMensaje(mess)
cargarSuma()
valor=cargarSuma2()
print("La suma2 es : " + str(valor))

mensaje2("rodrigo")
mensaje2("Rodrigo","segundo parametro")

sumav1 = funcionMultiplesParamatros(1,2)
sumav2 = funcionMultiplesParamatros(1,2,3,4)
sumav3 = funcionMultiplesParamatros(1,2,3,4,5,6,7,8,9)

print("2 parametros (1,2): " + str(sumav1))
print("4 parametros (1,2,3,4): " + str(sumav2))
print("9 parametros (1,2,3,4,5,6,7,8,9): " + str(sumav3))

lista1 = cargaLi()
print(lista1)