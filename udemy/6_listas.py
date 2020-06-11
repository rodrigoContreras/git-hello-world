lista=[]
for i in range(5):
    lista.append(input("Valor :"))

print("la lista es :" + str(lista))

espa=int(input("espacio a modificar : "))
num1=input("numero a ingresar")
lista[espa] = num1
print("la lista es :" + str(lista))

#INSERTAR VALOR
indice=int(input("donde insertar? : "))
num2=input("numero a inserta")
lista.insert(indice,num2)
print("la lista es :" + str(lista))

#REMOVER VALOR
num3=input("numero a eliminar")
lista.remove(num3)
print("la lista es :" + str(lista))

#BUSCAR NUMERO
num3=input("valor a buscar")
resultado= (num3 in lista)
if resultado:
    print("existe y su indice es : " + str(lista.index(num3)))
else:
    print("NO xiste")