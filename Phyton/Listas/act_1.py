#Acumulado

ask = int (input("\nCuántos números quieres sumar: "))

lista=[]
lista2=[]
cont=0

for i in range (0,ask):

    opc=int(input("\nIntroduzca el número: "))
    lista.append(opc)
    
for e in lista:
    cont+=e
    lista2.append(cont)

print (f"\n{lista}")
print (f"\n{lista2}\n")
