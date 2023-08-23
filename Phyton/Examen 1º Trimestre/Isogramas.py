#Determine si una cadena de texto introducida por teclado es un isograma, o no, es decir, una
#palabra en la que no se repite ninguna letra.
print ("------------------------------------------------------------------------")
print ("Un isograma es una palabra en la que no se repite ninguna letra.\nEste programa nos indica si la palabra introducida es un isograma o no.")
print ("------------------------------------------------------------------------")
print ("")
#Creo una variable True para poder continuar o dejar el programa cuando el usuario lo desee
si= True
while si == True:
#Preguntaremos la palabra que queremos comprobar:
    wrd=str(input("Introduce la palabra a comprobar: "))
#Contaré el número de letras que tiene la palabra
    long=len(wrd)
#Diré que diga el número de letras contando con un rango desde la primera letra, hasta la última con la variable creada anteriormente:
    for i in range (0,long):
#Con [] listaremos cada una de las letras:
        ln=wrd[i]
#Y con count, no saldrá si alguna de esas letras está repetida y lo sabremos si su valor es mayor a uno:
        cnt=wrd.count(ln)
#Ahora estableceré la condición dicha anteriormente:
    if cnt > 1:
        print ("\nNo es un isograma\n")
    else:
        print ("\nEs un isograma\n")
#Por último estableceremos si el usuario quiere cerrar o abrir el programa
    resp = input("Quieres seguir S/N: ")
    print ("")
#Si la respuesta es N la variable se volverá falsa, por lo que se cerrará el bucle.    
    if resp == "N":
        si=False
