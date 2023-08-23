#Letras_5

cadena=input("Introduce una cadena de palabras separadas por espacios: ")

lista=cadena.split(" ")

listav=[]

contador=0

for i in lista:
    cont=i.count("")-1
    if cont > 5:
        contador+=1
        listav.append(i)    
print (f"Hay {contador} palabras de más de cinco letras" )
print (f"Las palabras de más de cinco letras son: {listav}" )