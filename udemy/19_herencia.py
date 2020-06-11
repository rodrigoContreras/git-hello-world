class Operacion():
    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0
    
    def cargar(self):
        self.valor1=int(input("VAlor 1: "))
        self.valor2=int(input("VAlor 2: "))
    
    def mostrarResultado(self):
        return self.resultado

class Suma(Operacion): # OBtiENE HERENCI DE Operacion
    def operar(self):
        self.resultado=self.valor1 + self.valor2

class Resta(Operacion):
    def resta(self):
        self.resultado=self.valor1 - self.valor2


suma1 = Suma()
suma1.cargar()
suma1.operar()
sumaValores = suma1.mostrarResultado()
print("La suma de los valores e : ", str(sumaValores))

resta1 = Resta()
resta1.cargar()
resta1.resta()
restaValores = resta1.mostrarResultado()
print("La resta de los valores e : ", str(restaValores))