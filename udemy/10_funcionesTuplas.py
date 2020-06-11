
def ingresoFecha():
    dd=int(input("Ingrese dia : "))
    mm=int(input("Ingrese mes : "))
    aa=int(input("Ingrese año : "))
    tupla = (dd,mm,aa)
    return tupla

def mostrarFecha(fecha):
    print(fecha[0], fecha[1], fecha[2],sep="/")

fecha = ingresoFecha()
mostrarFecha(fecha)