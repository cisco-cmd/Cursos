frase=input("\nIntroduzca una frase: ")
l=input("\nLetra para buscar su posición: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print(f"\nNo se encontró en la posición {i}")
        i+=1
        continue
    print(f"\nSe encontró en la posición {i}\n")
    break