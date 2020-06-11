import insert
import delete
import update
import read

class Programa():
    def __init__(self):
        self.dato=1
    
    def menu(self):
        while self.dato:
            menu='''
            1._Insertar
            2._Actualizar
            3._Eliminar
            4._Consultar
            5._ Salir'''
            print(menu)
            selection = input("Ingrese Opcion : ")
            if selection == '1' :
                insert.insert()
            elif selection=='2' :
                update.update()
            elif selection =='3' :
                delete.delete()
            elif selection == '4' :
                read.read()
            elif selection == '5' :
                exit()
            else:
                print("Opcion Invalida")

persona = Programa()
persona.menu()





