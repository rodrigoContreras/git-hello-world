
def ingresoPaisHabit():
    lista =[]
    for i in range(3):
        pais=input("Ingrese pais : ")
        hab=int(input("Ingrese habitante : "))
        lista.append((pais, hab))
    return lista

def mostrarPaisesHabit(paises):
    for i in range(3):
        print(paises[i][0], paises[i][1])
lista = ingresoPaisHabit()
mostrarPaisesHabit(lista)