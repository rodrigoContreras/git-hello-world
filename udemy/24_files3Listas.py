# ABRE ARCHIVO EN MODO ESCRITURA LECTURA , SOBREECRIBE EL ARCHIVO SI EXISTE, CREA ARCHIVO SI NO EXISTE
archivo = open("arhivo.txt", "r+") 
contenido  = archivo.read() # LEE ARCHIVO POR COMPLETO
finalDeArchivo = archivo.tell() # RETORNA POSICION ACTUAL DEL PUNTERO
lista=["linea1\n", "linea2"]

archivo.writelines(lista) #ESCRIBE CADENA DENTRO DEL ARCHIVO
archivo.seek(finalDeArchivo) # MUEVE PUNTERO A POSICION INDICADA

print (archivo.readline())

print (archivo.readline())


