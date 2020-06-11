import random
from math import sqrt, pow

def cargarNumerosRandom():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista
def ingNumero():
    nume = int(input("ingrese Numero : "))
    return nume

def mostrarLista(lista):
    print(lista)

def mostrarListaMezclada(lista):
    random.shuffle(lista)

lista=cargarNumerosRandom()

mostrarLista(lista)

mostrarListaMezclada(lista)

mostrarLista(lista)

numero = ingNumero()
raiz = sqrt(numero)
elevar = pow(numero, 3)

print("Raiz : ", raiz)
print("Cubo : ", elevar)