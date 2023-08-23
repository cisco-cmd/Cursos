num = int(input("Escriba un numero: "));
num2=num 
if num < 0: 
    print("No existe factorial de un número negativo")    
else: 
    fact = 1
    while(num > 1): 
        fact *= num 
        num -= 1
    print ("") 

print("El factorial de ",num2," es ", fact) 