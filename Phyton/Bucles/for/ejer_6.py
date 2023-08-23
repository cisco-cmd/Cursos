var=True
while var == True:
    total=0
    mon=float(input("\nIntroduzca el monto de una venta: "))
    while mon!=0:
        if mon<0:
            print("\nMonto incorrecto\n")
        else:
            total+=mon
        mon=float(input("\nIntroduzca el monto de una venta (Introduzca 0 para finalizar): "))
    if total>1000:
        total-=total*0.1
        print(f"\nMonto total a pagar: {total} €\n")
        ext=input("Quieres continuar (S/N): ")
        print("")
        if ext == "S":
            print("")
            break
        elif ext == "N":
            exit()