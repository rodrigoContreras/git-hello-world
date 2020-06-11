
def presentacion():
    print ("funciones")
    print("-----------")

def ingresoDatos():
    global num1
    global num2
    num1 = int(input("Numero 1 : "))
    num2 = int(input("Numero 2 : "))

def suma():
    suma = num1 + num2
    print("suma : "+  str(suma))

presentacion()
ingresoDatos()
suma()
