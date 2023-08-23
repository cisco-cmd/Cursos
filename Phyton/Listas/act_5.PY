#Loteria
import random
boleto=[]
premio=[]
aciertos=[]
errores=[]
loteria=input("\nIntroduce seis números separados por espacios: ")
lista_lot=loteria.split(" ")
for b in lista_lot:
    boleto0=int(b)
    boleto.append(boleto0)
    boleto_ord=sorted(boleto)
print (f"\nTu boleto es: {boleto_ord}\n")
for i in range (1,7):
    premio0= random.randint(1, 49)
    premio.append(premio0)
    premio_ord=sorted(premio)
print(f"Los números ganadores son: {premio_ord}")
for a in boleto_ord:
    if a in premio_ord:
        aciertos.append(a)
    else:
        errores.append(a)
long_ac=len(aciertos)
long_er=len(errores)
print (f"\nTus aciertos han sido {long_ac}, los números acertados son: {aciertos}\n")
print (f"Tus errores han sido {long_er}, los números errados son: {errores}\n")