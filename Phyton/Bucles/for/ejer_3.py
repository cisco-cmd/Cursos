par=0
n=int(input("\nIntroduzca un número de dos o más dígitos: "))
while n!=-1:
    if n%2 == 0:
        par+=1
    suma=0
    while n!=0:
        dig=n%10
        suma+=dig
        n=n//10
    print(f"\nSuma de sus dígitos: {suma}\n")
    n=int(input("Introduzca un número de dos o más dígitos (-1 para terminar el programa): "))
print("Se ingresaron", par, "números pares")
        
