wrd = input ("Escriba una palabra: ")
letras=wrd.count("")
cont_vocales=0
vocales=["a","e","i","o","u"]
for i in wrd:
    if i in vocales:
        cont_vocales+=1
print (f"Hay {letras} letras y {cont_vocales} vocales")