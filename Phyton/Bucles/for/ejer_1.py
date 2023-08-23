var=True
while var == True:
    print ("-----------------------Menú-------------------------")
    print ("")
    print ("1. Sumatoria")
    print ("2. Sumatoria de todos los números positivos")
    print ("3. Mayor número")
    print ("4. Salir")
    print ("")
    print ("-----------------------------------------------------------")
    print ("")
    opc=int(input("Que operación quieres realizar?: "))
    print("")
    var=True
    while var != False:
        if opc==1:
            total=0
            nro=int(input("Número: "))
            while nro != 0:
                total+=1
                nro=int(input("Número: "))
                print("")
            print("Cantidad de números introducidos: ", total)
            print("")
            ext=input("Quieres continuar (S/N) o quieres continuar en esta opción (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==2:
            positivos=0
            n=int(input("Número (0 para terminar): "))
            while n!=0:
                if n>0:
                    positivos+=1
                n=int(input("Número (0 para terminar): "))
            print("Cantidad de positivos:", positivos)
            ext=input("Quieres continuar (S/N) o quieres continuar en esta opción (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==3:
            mayor=-1
            n=int(input("Número positivo:"))
            while n!=0:
                if n>mayor:
                    mayor=n
                n=int(input("Número positivo:"))
            print("Mayor número ingresado:", mayor)
            ext=input("Quieres continuar (S/N) o quieres continuar en esta opción (A): ")
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