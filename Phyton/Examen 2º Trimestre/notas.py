#Notas
asignaturas=["Matemáticas","Física","Química","Historia","Lengua","Biología"]
var=True
#Creo una lista vacia para las notas
notas=[]
nombre0=[]
#Creo el menú
while var == True:
    print ("-----------------------Menú-------------------------")
    print ("")
    print ("1. Introduce el nombre del alumno y sus notas")
    print ("2. Mostrar las notas por pantalla")
    print ("3. Mostrar asignaturas pendientes")
    print ("4. Salir")
    print ("")
    print ("-----------------------------------------------------------")
    print ("")
    opc=int(input("Que operación quieres realizar?: "))
    print("")
    var=True
    #Si se introduce un número mayor a cuatro nos dará error
    while var != False:
        if opc > 4:
            print ("El opción introducida es incorrecta")
            print ("")
            ext=input("Quieres continuar (S/N): ")
            opc=ext.upper()
            if opc == "S":
                print("")
                break
            else:
                exit()
        elif opc==1:
            #Guardará el nombre del alumno y guardará las notas
            nombre=input("Introduce tu nombre: ")
            nombre0.append(f"{nombre}")
            for i in asignaturas:
                nota=float(input(f"\nIntroduce la nota de la asignatura {i}: "))
                print("")
                notas.append(nota)
            print("")
            ext=input("Quieres continuar (S/N): ")
            opc=ext.upper()
            if opc == "S":
                print("")
                break
            elif opc == "N":
                exit()
        elif opc==2:
            print (f"Tu nombre es {nombre} y tus notas son: \n")
            #Unimos las dos listas para que devuelva la nota de cada asignatura
            for lista1,lista2 in zip (asignaturas, notas):
                print (f"En la asignatura {lista1} tienes un: {lista2}")
                print("")
            ext=input("Quieres continuar (S/N): ")
            opc=ext.upper()
            if opc == "S":
                print("")
                break
            elif opc == "N":
                exit()
        elif opc==3:
            #Toda nota que sea menor a cinco, saldrá como suspensa
            for lista1,lista2 in zip (asignaturas, notas):
                if lista2 < 5:
                    print(f"{nombre}, la asignatura {lista1} está suspensa con un {lista2}\n")
            ext=input("Quieres continuar (S/N): ")
            opc=ext.upper()
            if opc == "S":
                print("")
                break
            elif opc == "N":
                exit()
        elif opc==4:
            print ("")
            ext=input("Estás seguro de que no quieres continuar (S/N): ")
            opc=ext.upper()
            if opc == "S":
                var=False
            else:
                break