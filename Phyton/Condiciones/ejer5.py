#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
#sexo y el nombre. El grupo A esta formado por las mujeres con un nombre
#anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
#resto. Escribir un programa que pregunte al usuario su nombre y sexo, y
#muestre por pantalla el grupo que le corresponde.
print ("----------------------------------------------------------------")
print ("-----------------------------Clases-----------------------------")
print ("----------------------------------------------------------------")
print ("")
nom=input("Introduzca su nombre: ")
print ("")
gen=input("Introduzca su género h/m: ")
print ("")

if (gen == "m" and nom < 'm') or (gen == "h" and nom > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es el:",group)
print ("")
