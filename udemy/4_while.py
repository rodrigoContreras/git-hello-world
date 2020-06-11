x=0
suma =0
cant =0
nota =0
while nota <= 7 :
    nota= int(input("nota : "))
    suma = suma + nota
    cant = cant + 1 

promedio = suma / cant
print ("promedio :" + str(promedio))

