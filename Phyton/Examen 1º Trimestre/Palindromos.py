#Diseña un programa en Python llamado “Palindromos” que:
#Determine si una palabra o número introducida por teclado es un palíndromo, o no.
print ("----------------------------------------------------------------")
print ("-------------------Palabras y números capicuas------------------")
print ("----------------------------------------------------------------")
print ("")
#Creo una variable True para poder continuar o dejar el programa cuando el usuario lo desee
si= True
while si == True:
#Preguntaremos si un número es capicúa:
    wrd=str(input("Introduce una palabra y comprobaré si es capicua: "))
#Crearemos una variable que invierta la palabra introducida
    cap=wrd[::-1]
#Daremos una condición que diga si la palabra introducida es igual al revés,
#le porndremos lower para que en el caso de que hayan escrito alguna mayúsucua, no afecte al resultado.
    if wrd.lower() == cap.lower():
        print (f"\nLa palabra o el número {wrd} es capicua, al revés es {cap}\n")
    else:
        print (f"\nLa palabara o el número {wrd} no es capicúa\n")
#Por último estableceremos si el usuario quiere cerrar o abrir el programa 
    resp = input("Quieres seguir S/N: ")
    print ("")
#Si la respuesta es N la variable se volverá falsa, por lo que se cerrará el bucle.    
    if resp == "N":
        si=False

