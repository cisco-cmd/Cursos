s=True
print ("------------------------")
print ("----------Menú----------")
print ("------------------------")
print ("1) Decir el número de letras y vocales de una palabra y multiplicarla")
print ("2) Decir si un número es par o impar")
print ("3) Introducir un número y te diremos todos todos los multiplos de 5 desde ese número hacia atrás")
print ("4) Salir")
opc = int (input ("Elija una opción: "))
while s:
    if opc == 1:
        wrd = str (input ("Introduce una palabra:"))
        nwrd = len(wrd)
        a = wrd.count("a")
        e = wrd.count("e")
        i = wrd.count("i")
        o = wrd.count("o")
        u = wrd.count("u")
        voc = a+e+i+o+u
        mul = nwrd*voc
        print (f"El numero de letras es {nwrd} y el número de vocales es {voc}, {nwrd}x{voc} es igual a {voc*nwrd}")
    elif opc == 2:
        num= int(input("Introduce un número: "))
        if num % 2 == 0:
            print (f"El número {num} es par")
        else:
            print (f"El número {num} es impar")
    elif opc == 4:
        s=False
    else:
        print ("Elija una opción del 1 al 4: ")