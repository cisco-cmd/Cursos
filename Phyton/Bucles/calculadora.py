var=True
while var == True:
    print ("-----------------------Calculadora-------------------------")
    print ("")
    print ("1. Suma")
    print ("2. Diferencia")
    print ("3. Multiplicación")
    print ("4. División")
    print ("5. Salir")
    print ("")
    print ("-----------------------------------------------------------")
    print ("")
    opc=int(input("Que operación quieres realizar?: "))
    print("")
    var=True
    while var != False:
        if opc > 5:
            print ("El número introducido es incorrecto")
            print ("")
            ext=input("Quieres continuar (S/N): ")
            if ext == "S":
                print("")
                break
            else:
                exit()
        elif opc==1:
            num1=int(input("Introduce el primer número para la suma: "))
            num2=int(input("Introduce el segundo número para la suma: "))
            sum=(num1+num2)
            print("")
            print ("La suma entre",num1,"y",num2,"es igual a:",sum)
            print("")
            ext=input("Quieres continuar (S/N) o quieres continuar sumando (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==2:
            num1=int(input("Introduce el primer número para la resta: "))
            num2=int(input("Introduce el segundo número para la resta: "))
            dif=(num1-num2)
            print("")
            print ("La resta entre",num1,"y",num2,"es igual a:",dif)
            print("")
            ext=input("Quieres continuar (S/N) o quieres continuar restando (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==3:
            num1=int(input("Introduce el primer número para la multiplicación: "))
            num2=int(input("Introduce el segundo número para la multipliación: "))
            mul=(num1*num2)
            print ("")
            print ("La multiplicación entre",num1,"y",num2,"es igual a:",mul)
            print ("")
            ext=input("Quieres continuar (S/N) o quieres continuar multiplicando (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==4:
            num1=int(input("Introduce el primer número para la división: "))
            num2=int(input("Introduce el segundo número para la división: "))
            div=float(num1/num2)
            print ("")
            print ("La división entre",num1,"y",num2,"es igual a:",div)
            print ("")
            ext=input("Quieres continuar (S/N) o quieres continuar dividiendo (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opc==5:
            print ("")
            ext=input("Estás seguro de que no quieres continuar (S/N): ")
            if ext == "S":
                var=False
            else:
                break
