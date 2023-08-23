lin=0
digitos="0123456789"
dig=0
tit=input("\nIntroduce un título: ")
while tit!="*":
    for caracter in tit:
        if caracter in digitos:
            dig+=1
    if tit=="/":
        lin+=1
        print(f"\nAparecen {dig} dígitos en la cadena\n")
        dig=0
    tit=input("\nIntroduzca otro título (Introduzca * para finalizar o / para terminar la cadena): ")
print(f"\nSe leyeron {lin} líneas completas\n")