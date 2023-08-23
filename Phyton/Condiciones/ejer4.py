#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener
#unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa
#que pregunte al usuario su edad y sus ingresos mensuales y muestre por
#pantalla si el usuario tiene que tributar o no.
print ("----------------------------------------------------------------")
print ("----------------------------Tributar----------------------------")
print ("----------------------------------------------------------------")
print ("")
edad=int(input("Introduzca su edad: "))
print ("")
ing=int(input("Introduzca sus ingresos mensuales: "))
print ("")
if edad>=16 and ing>=1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")
print ("")