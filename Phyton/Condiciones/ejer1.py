# Escribir un programa que almacene la cadena de caracteres contraseña en
# una variable, pregunte al usuario por la contraseña e imprima por pantalla si la
# contraseña introducida por el usuario coincide con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas.
print ("----------------------------------------------------------------")
print ("------------------Confirmación de contraseña--------------------")
print ("----------------------------------------------------------------")
print ("")
cont=input("Escriba la contraseña: ")
print ("")
cont1=input("Confirme la contraseña: ")
print ("")
if cont == cont1.lower():
    print ("La contraseña es correcta")
else:
    print ("La contraseña no coincide")
print ("")
