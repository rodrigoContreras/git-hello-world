valorr=0
def cargaLi(lista):
    valorr=0
    for i in range(len(lista)):
         valorr = valorr + lista[i]
    return valorr

def cargaLiMenor(lista):
    menor=lista[0]
    for i in range(1,len(lista)):
        if lista[i] < menor:
         menor =  lista[i]
    return menor


#LLAMADA A FUNCIONES
lista = [1,2,3,4,5,6,7,8,9,0]
valorSumaLista = cargaLi(lista)

print("La suma de la lista es : " , str(valorSumaLista))
print("menor de la lista es : " , cargaLiMenor(lista))