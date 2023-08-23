#Diseña un programa en Python llamado “num_primos” que muestre un menú por pantalla si un
#número es primo o no
print ("----------------------------------------------------------------")
print ("-------------------------Números Primos-------------------------")
print ("----------------------------------------------------------------")
print ("")
#Preguntaremos el número:
num = int(input("Introduce un número entero del 1 al 100 y te diré si es primo o no: "))
#Crearemos una variable para indicar que el primero número primo es 2, posteriormente,
#se le irá sumando 1 para comprobar todos los primos.
prim = 2
fin = True
#Crearemos el bucle con while para realizar lo anterior mencionado:
si= True
while si == True:
    while num % prim != 0 or num > 100 or fin == False:
        prim += 1
    if prim == num:
        print(f"\nEl número {num} es primo\n")
    else:
        print(f"\nEl número {num} no es primo\n")
#Por último estableceremos si el usuario quiere cerrar o abrir el programa
    resp= input ("Quieres continuar S/N?: ")
    print ("")
#Si la respuesta es N la variable se volverá falsa, por lo que se cerrará el bucle.    
    if resp == "N":
        si=False
