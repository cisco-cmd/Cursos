#Introducida una frase, determine el número de letras introducidas en mayúscula, el número
#de letras introducidas en minúscula y los caracteres numéricos (Números) que aparecen en ella.
frase = str(input("Introduzca una frase: "))
dif=frase.split()
num=dif.isdigit()

print (num)