dia=input("Introduzca el día: ")
mes=input("\nIntroduzca el mes: ")
año=input("\nIntroduzca el año: ")

lista0=[]
fechal=lista0.insert(0,dia)
fechal=lista0.insert(1,mes)
fechal=lista0.insert(2,año)

lista0[0] = mes
lista0[1] = dia
lista0[2] = año

ing=("/".join(lista0))

lista0[0]=dia
lista0[1]=mes
lista0[2]="20"+año

esp=("-".join(lista0))

print (f"\nLa fecha inglesa sería: {ing}\n")
print (f"La fecha española sería: {esp}\n")
