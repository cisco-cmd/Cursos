#Escribir un programa que lea la puntuación del usuario e indique su nivel de
#rendimiento, así como la cantidad de dinero que recibirá el usuario.
print ("----------------------------------------------------------------")
print ("---------------------------Rendimiento--------------------------")
print ("----------------------------------------------------------------")
print ("")
print ("La puntuación posible es 0.0, 0.4, 0.6 o más")
print ("")
punt=float(input("Escriba su puntuación: "))
print ("")
cob=int(2400*punt)
if punt == 0.0:
    print ("Su puntuación es inaceptable")
    print ("")
    print ("La cantidad de dinero que cobrará es:",cob,"€")
elif punt == 0.4:
    print ("Su puntuación es aceptable")
    print ("")
    print ("La cantidad de dinero que cobrará es:",cob,"€")
elif punt >= 0.6:
    print ("Su nivel es meritorio")
    print ("")
    print ("La cantidad de dinero que cobrará es:",cob,"€")
else:
    print ("Su puntuación no es válida")
print ("")