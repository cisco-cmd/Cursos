#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o
#no, y en función de su respuesta le muestre un menú con los ingredientes
#disponibles para que elija. Solo se puede eligir un ingrediente además de la
#mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
#por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que
#lleva.
print ("----------------------------------------------------------------")
print ("------------------------------Pizzas----------------------------")
print ("----------------------------------------------------------------")
print ("")
men=input("¿Quiere pizza vegetariana s/n?: ")
print ("")
if men == "s":
    print ("Los ingredientes vegetarianos son: pimiento y tofu")
    print ("")
    veg=input("Que ingrediente quiere (solo uno): ")
    print ("")
    print ("Los ingredientes de la pizza serán: tomate, mozzarella y",veg)
    print ("")
if men == "n":
    print ("Los ingredientes no vegetarianos son: peperoni, jamón y salmón")
    print ("")
    nveg=input("Que ingrediente quiere (solo uno): ")
    print ("")
    print ("Los ingredientes de la pizza serán: tomate, mozzarella y",nveg)
print ("")