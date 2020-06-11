import random
seleccion = random.randint(0,100)

for i in range(0,100):
    if i == seleccion:
        print ("el numero elegido al azar es : " + str(i))
        break
