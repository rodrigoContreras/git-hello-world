class Clientes():
    suspendidos=[]
    def __init__(self, codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def impirmir(self):
        print("Codigo : ", self.codigo)
        print("nombre : ", self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Clientes.suspendidos:
            print("Esta suspendido")
        else:
            print("Esta OK")
    
    def suspender(self):
        Clientes.suspendidos.append(self.codigo)

           
    


cliente1 = Clientes(1,"juan")
cliente2 = Clientes(2,"Manuel")
cliente3 = Clientes(3,"David")
cliente4 = Clientes(4,"Marcelo")

cliente3.suspender()
cliente4.suspender()

cliente1.impirmir()
cliente2.impirmir()
cliente3.impirmir()
cliente4.impirmir()


print(Clientes.suspendidos)
