año=int(input("Introduce el año que quieres comprobar: "))

if ((año % 4 == 0) and (año % 100 != 0)) or (año % 400 == 0):
    print( "El año",año,"es bisiesto" )
else:
    print( "El año",año,"no es bisiesto" )