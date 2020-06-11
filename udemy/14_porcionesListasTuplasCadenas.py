def resto(numero):
    meses=('Enero','FebrerE','Marzo','Abril','Mayo','Junio','Julio','Agosto', 'Septiembre','Octubre','Noviembre', 'Diciembre')
    print("Mese restantes")
    print(meses[numero:])


def visualizarMeses(inicio, fin):
    meses=('Enero','FebrerE','Marzo','Abril','Mayo','Junio','Julio','Agosto', 'Septiembre','Octubre','Noviembre', 'Diciembre')
    print("Meses a mostrar")
    print(meses[inicio-1:fin])

numero = int(input("Numero de Mes en el que estamos : "))
resto(numero)

numero1 = int(input("Numero de Mes inicial : "))
numero2 = int(input("Numero de Mes Final : "))
visualizarMeses(numero1, numero2)







