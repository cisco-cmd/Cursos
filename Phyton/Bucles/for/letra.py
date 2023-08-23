from operator import index


frase = input ("Introduzca una frase: ") 
repletras = dict()  
tletras = 0

contfrase= len(frase.replace(" ", ""))

for letra in frase.replace (" ",""): 
    if letra in repletras: 
        if repletras[letra] >= 1: 
            tletras += 1 
        repletras[letra] += 1
    else:
        repletras[letra] = 1 
    
print(f"\nLa frase tiene {contfrase} letras")
print(f"\nLas letras son: {repletras}")
print(f"\nSe repiten {tletras} letras\n")
