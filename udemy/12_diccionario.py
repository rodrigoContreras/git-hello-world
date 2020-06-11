def cargar():
    diccionario = {}
    continua="s"
    while continua == "s":
        castellano= input("ingrese palabra en castellano : ")
        ingles= input("ingrese palabra en ingles : ")
        diccionario[castellano]=ingles
        continua= input("continua ? : ")
    return diccionario

def mostrar(diccionario):
    print("Muestra diccionario toal")
    for i in diccionario:
        print (i,diccionario[i])

def buscarPalabra(diccionario):
    palabra =  input("palabra a buscar : ")
    if palabra in diccionario:
        print ("en ingles es : ", diccionario[palabra])
    
diccionario = cargar()
mostrar(diccionario)
buscarPalabra(diccionario)





