numero=int(input("\nIntroduzca un número entero positivo: "))
tPares=0
tImpares=0
while numero!=0:
   pares=0
   impares=0
   while numero!=0:   
     ultimodigito=numero%10
     if ultimodigito%2==0:
       pares+=1
       tPares+=1
     else:
       impares+=1
       tImpares+=1
     numero=numero//10
   print(f"\nEl número ingresado tiene {pares} digitos pares y {impares} digitos impares\n")
   numero=int(input("Siguiente número (Introduzca 0 para finalizar): "))
