var=True
while var == True:
    while True:
        print("Opción 1 - comenzar programa")
        print("Opción 2 - imprimir listado")
        print("Opción 3 - finalizar programa\n")
        opcion=int(input("Opción elegida: "))
        if opcion==1:
            print("\nHola, el programa se va a iniciar\n")
            ext=input("Quieres continuar (S/N) o quieres continuar en esta opción (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opcion==2:
            print("Listado:")
            lst=input("\nIntroducer nombres separados por comas: ")
            len(lst)
            ext=input("Quieres continuar (S/N) o quieres continuar en esta opción (A): ")
            if ext == "S":
                print("")
                break
            elif ext == "N":
                exit()
            elif ext == "A":
                print ("")
        elif opcion==3:
            print("\nHasta la próxima...\n")
            break
        else:
            print("Opción incorrecta. Debe ingresar 1, 2 o 3")