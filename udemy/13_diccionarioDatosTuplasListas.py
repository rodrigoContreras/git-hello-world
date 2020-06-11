def cargar():
    productos = {}
    continua="s"
    while continua == "s":
        codigoProd= input("ingrese codigo producto : ")
        descripcion= input("descripcion : ")
        precio= input("precio : ")
        stock= input("stok : ")
        productos[codigoProd]=(descripcion,precio,stock)
        continua= input("continua ? : ")
    return productos

def mostrar(productos):
    print("Muestra diccionario total")
    for codigo in productos:
        print (codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

def consultaProductos(productos):
    print("consulta diccionario ")
    codigo = input ("codigo a consultar: ")
    if codigo in productos:
        print (codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])
    else:
        print("no existe")

def listadoStockCero(productos):
    print("stock a 0 : ")
    for codigo in productos:
        if productos[codigo][2] == "0":
            print (codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])
    
diccionario = cargar()
mostrar(diccionario)
consultaProductos(diccionario)
listadoStockCero(diccionario)





