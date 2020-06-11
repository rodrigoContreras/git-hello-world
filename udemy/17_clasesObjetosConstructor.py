class Alumno:
    #inicializar atributos CONSTRUCTOR
    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.curso=""

    def declarar(self, nombre, apellido, curso):
        self.nombre=nombre
        self.apellido=apellido
        self.curso=curso

    def mostrar(self):
       print("MOSTRAR DATOS INGRESADOS")
       print("nombre : ", self.nombre)
       print("apellido : ", self.apellido)
       print("curso : ", self.curso)

    def mostrarCurso(self):
        print("")
        print("SOLO MUESTRA CURSO")
        print("curso : ", self.curso)

#llamada a metodos propios dentro de la clase
    def main(self):
        self.mostrar()
        self.mostrarCurso()

menu = '''
1._ esta 
2._ es una
3._ variable
4._ multilinea
'''

print(menu)

alumno1 = Alumno()
alumno1.declarar("Rodrigo","Contreras","8vo")
alumno1.main()

