nums=input("Introduce tres números separados por un espacio: ")
lista=nums.split(" ")
lista_ord=sorted(lista)
lista_ord.reverse()
nums_ord="-".join(lista_ord)
print (nums_ord)
