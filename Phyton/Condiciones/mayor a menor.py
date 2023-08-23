num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
num3=int(input("Introduce el tercer número: "))
if num1==num2 or num1==num3 or num2==num3:
    print("Se ingresaron dos números iguales")
if num1==num2 and num1==num3 and num2==num3:
    print("Se ingresaron tres números iguales")
if num1>num2 and num1>num3:
    print("",num1,">",num2,">",num3)
elif num1>num3 and num3>num2:
    print("",num1,">",num3,">",num2)
elif num2>num1 and num1>num3:
    print("",num2,">",num1,">",num3)
elif num3>num1 and num1>num2:
    print("",num3,">",num1,">",num2)
elif num3>num2 and num2>num1:
    print("",num3,">",num2,">",num1)
elif num2>num3 and num3>num1:
    print("",num2,">",num3,">",num1)
