#Más_larga
lista0=[]
pal=""
while pal != "-1":
    pal=input("Introduzca una palabra (-1 para parar): ")
    lista0.append(pal)
lista0.remove("-1")
lista_ord=sorted(lista0, key=len)
lista_ord.reverse()
print(f"La lista es: {lista0}")
print(f"La palabra más larga es: {lista_ord[0]}")