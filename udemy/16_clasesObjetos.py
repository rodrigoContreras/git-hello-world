class Alumno:
    def declarar(self, nombre, apellido, curso):
        self.nombre=nombre
        self.apellido=apellido
        self.curso=curso
    def clase(self):
        print("Matematicas")

alumno1 = Alumno()
alumno1.declarar("Rodrigo","Contreras","8vo")
alumno1.clase()
print("nombre : ", alumno1.nombre)
print("apellido : ", alumno1.apellido)
