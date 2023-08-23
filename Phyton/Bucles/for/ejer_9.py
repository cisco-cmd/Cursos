var=True
while var == True:
    frs=input("\nIntroduzca una frase: ").strip()
    cnt=0
    wrd_lar=0
    while len(frs) != 0:
        cnt+=1
        i=frs.find(" ")
        if i != -1:
            palabra=frs[0:i]
            while i < len(frs) and frs[i] == " ":
                i=i+1
            frs=frs[i:]
        else:
            palabra=frs
            frs=""
        if len(palabra) > wrd_lar:
            wrd_lar=len(palabra)
            lwrd_lar=palabra
    if cnt > 0:
        print(f"\nPalabra más larga: {lwrd_lar}")
    print(f"\nCantidad de palabras: {cnt}\n")
    ext=input("Quieres continuar (S/N): ")
    if ext == "S":
        print("")
        break
    elif ext == "N":
        exit()