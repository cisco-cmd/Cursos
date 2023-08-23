#Pares_Impares
pares=[]
impares=[]
ask=input("Introduce una lista de números separados por espacios: ")
lista=ask.split(" ")

for i in lista:
    if int(i) % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

ord_pares=sorted(pares)
ord_impares=sorted(impares)
print (f"\nLos números pares son: {ord_pares}")
print (f"\nLos números impares son: {ord_impares}\n")
