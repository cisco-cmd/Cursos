#Escribir un programa que pregunte al usuario su renta anual y muestre por
#pantalla el tipo impositivo que le corresponde.
print ("----------------------------------------------------------------")
print ("---------------------------Impositivo---------------------------")
print ("----------------------------------------------------------------")
print ("")
rent=int(input("Escriba su renta anual: "))
print ("")
if rent < 10000:
    print ("Su tipo de impositivo es 5%")
elif rent >=10000 and rent<=20000:
    print ("Su tipo de impositivo es de 15%")
elif rent >=20000 and rent<=35000:
    print ("Su tipo de impositivo es de 20%")
elif rent >=35000 and rent<=60000:
    print ("Su tipo de impositivo es de 30%")
elif rent > 60000:
    print ("Su tipo de impositivo es 45%")
print ("")