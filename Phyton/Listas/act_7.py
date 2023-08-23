import random
var=True
suma0=0
promedio=0
while var == True:
    print ("-----------------------Menú-------------------------")
    print ("")
    print ("1. Crea una lista con números aleatorios")
    print ("2. Imprimir la lista creada")
    print ("3. Mostrar mayor número")
    print ("4. Mostrar menor número")
    print ("5. Sumar los números")
    print ("6. Promedio")
    print ("7. Salir")
    print ("")
    print ("-----------------------------------------------------------")
    print ("")
    opc=int(input("Que operación quieres realizar?: "))
    print("")
    var=True
    while var != False:
        if opc > 7:
            print ("El opción introducida es incorrecta")
            print ("")
            ext=input("Quieres continuar (S/N): ")
            if ext == "S":
                print("")
                break
            else:
                exit()
        elif opc==1:
            lista0=[]
            for i in range(1, 6):
                rnd = random.randint(1, 20)
                lista0.append(rnd)
            ext=input("Quieres continuar (S/N): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==2:
            print (lista0)
            print("")
            print ("")
            print("")
            ext=input("Quieres continuar (S/N): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==3:
            lista_ord=sorted(lista0)
            lista_ord.reverse()
            print (f"El mayor número de la lista es: {lista_ord[0]}")
            print ("")
            ext=input("Quieres continuar (S/N) o quieres seguir en esta opción(A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==4:
            lista_ord=sorted(lista0)
            print (f"El menor número de la lista es: {lista_ord[0]}")
            print ("")
            ext=input("Quieres continuar (S/N) o quieres seguir en esta opción(A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==5:
            for i in lista0:
                suma0+=i
            print (f"{suma0}")
            ext=input("Quieres continuar (S/N) o quieres seguir en esta opción(A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==6:
            long=len(lista0)
            for i in lista0:
                promedio+=i/long
            print (f"{promedio:.2f}\n")
            ext=input("Quieres continuar (S/N) o quieres seguir en esta opción(A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==7:
            print ("")
            ext=input("Estás seguro de que no quieres continuar (S/N): ")
            if ext == "S":
                var=False
            else:
                break
