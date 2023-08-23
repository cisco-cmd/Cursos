#Imprimir las tablas de multiplicar del 1 al 10 con bucles
i=1
j=1
while i <= 10:
    while j <= 10: 
        print (f"{i} x {j} = {i*j}")
        j +=1
    j=1
    i+=1
