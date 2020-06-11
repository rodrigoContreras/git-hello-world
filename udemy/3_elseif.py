nota1 = int(input("ingrese nota 1 : "))
nota2 = int(input("ingrese nota 2 : "))
nota3 = int(input("ingrese nota 3 : "))

promedio = (nota1+ nota2+nota3)/3

print(promedio)

if promedio >= 7 :
    print("excelente")
elif promedio > 4 and promedio < 7:
    print("Regular a bueno")
elif promedio < 4 :
    print("malisimo")

