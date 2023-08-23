suma=0
var=True
while var == True:
    print("")
    n=int(input("Introduzca un número positivo con mínimo tres digitos: "))
    print("")
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("La suma de los dígitos es igual a: ", suma)
    print("")
    ext=input("Quieres continuar (S/N): ")
    if ext == "S":
        print("")
        suma=0
        print=("")
    elif ext == "N":
        exit()
