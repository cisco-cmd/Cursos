#Escribir un programa que pida al usuario dos números y muestre por pantalla
#su división. Si el divisor es cero el programa debe mostrar un error.
print ("----------------------------------------------------------------")
print ("------------------------División entre 0------------------------")
print ("----------------------------------------------------------------")
print ("")
num1=int(input("Escriba el primer número: "))
print ("")
num2=int(input("Escriba el segundo número: "))
print ("")
if num2 == 0:
    print ("Error: la división no puede ser entre 0")
else:
    num3=(num1/num2)
    print ("El resultado de la división es: ",num3)
print ("")