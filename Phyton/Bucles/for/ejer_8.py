primos=0
n=int(input("\nIntroduzca números y te diré cuantos primos hay: "))
while n!=0:
 primo=True
 for i in range(2,n):
   if n%i==0:
     primo=False
     break
 if primo:
   primos+=1
 n=int(input("\nOtro número (Introduzca 0 para finalizar): "))
print(f"\nprimos: {primos}\n")