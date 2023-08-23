#Adivina
#Importamos la variable aleatoria
import random
from tracemalloc import stop
#Creo un contador desde 10 que va a ir restando cada vez que falles, una vez llegué a 0, tendrás que volver a empezar.
cont=10
#Creo el número aleatorio
num0=random.randint(1, 1000)
num1=int(input(f"Introduce un número (1-1000): "))
print("")
#Creo el bucle para que pregunte hasta que aciertes o el contador llegue a 0
if num1 > 1000:
    print ("El número introducido es mayor a mil\n")
while cont != 1 and num1 < 1001:
    if num1 != num0:
        cont-=1
        num1=int(input(f"Introduce un número (Te quedan {cont} intentos): "))
        if num1 > 1000:
            print ("\nEl número introducido es mayor a mil\n")
            break
        print("")
        #Si se acierta, te saldrá el mensaje de que has acertado
    elif num1 == num0:
        print (f"Has acertado, el número ganador era {num0}\n")
        break
#Si fallas todos los intentos, te dirá cual era el número ganador
if num1 != num0:
    print (f"El número ganador era {num0}\n")