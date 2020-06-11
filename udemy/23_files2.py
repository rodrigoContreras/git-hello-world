# ABRE ARCHIVO EN MODO ESCRITURA LECTURA , SOBREECRIBE EL ARCHIVO SI EXISTE, CREA ARCHIVO SI NO EXISTE
archivo = open("arhivo.txt", "w+") 
agregar = input("Agregar a archivo")
contenido  = archivo.read() # LEE ARCHIVO POR COMPLETO
finalDeArchivo = archivo.tell() # RETORNA POSICION ACTUAL DEL PUNTERO

archivo.write(agregar) #ESCRIBE CADENA DENTRO DEL ARCHIVO
archivo.seek(finalDeArchivo) # MUEVE PUNTERO A POSICION INDICADA
nuevoContenido = archivo.read()

archivo.close()
print ("Nuevo contenido", nuevoContenido)
