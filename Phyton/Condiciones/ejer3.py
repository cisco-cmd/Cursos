#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es par o impar.
print ("----------------------------------------------------------------")
print ("----------------------Número par o impar------------------------")
print ("----------------------------------------------------------------")
print ("")
num=int(input("Introduzca un número: "))
print ("")
div=num/2
if div % 2 == 0:
    print ("El número es par")
else:
    print ("El número es impar")
print ("")