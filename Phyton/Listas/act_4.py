#Duplicados
var=True
listav=[]
while var == True:
    print ("-----------------------Menú-------------------------")
    print ("")
    print ("1. Introducir lista")
    print ("2. Comprobar duplicados")
    print ("3. Eliminar duplicados")
    print ("4. Salir")
    print ("")
    print ("-----------------------------------------------------------")
    print ("")
    opc=int(input("Que operación quieres realizar?: "))
    print("")
    var=True
    while var != False:
        if opc > 4:
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
            pal=""
            while pal != "#":
                pal=input("Introduzca una palabra ( # para parar ): ")
                lista0.append(pal)
            lista0.remove("#")
            print(f"\nLa lista introducida es: {lista0}")
            print("")
            ext=input("Quieres continuar (S/N) o quieres seguir en esta opción(A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==2:
            cont=0
            for i in range (len(lista0)):
                for a in range (len(lista0)):
                    if i != a:
                        if lista0[i] == lista0[a] and lista0[i] not in listav:
                            cont+=1
                            listav.append(lista0[i])
            print(f"Hay {cont} palabras repetidas")
            print(f"\nLa\s palabra\s repetida\s es\son: {listav}")
            print("")
            ext=input("Quieres continuar (S/N) o quieres seguir en esta opción(A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==3:
            for i in listav:
                lista0.remove(f"{i}")
            print (f"La lista sin los elementos reptidos: {lista0}")
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
            print ("")
            ext=input("Estás seguro de que no quieres continuar (S/N): ")
            if ext == "S":
                var=False
            else:
                break
