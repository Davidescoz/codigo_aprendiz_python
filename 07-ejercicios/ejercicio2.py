"""
Ejercicio 2
    -Escribir un script que ejecute todos los numeros pares de 1 al 120

"""

contador=0



for contador in range(1,121):
    if contador%2==0:
        print(f"{contador} es par")
    else:
        print(f"{contador} es impar")    
   

#Comprobar si un numero es primo o es par


numero_usuario=int(input("¿Que numero desea verificar si es primo o es par?: "))
 
if numero_usuario%2==0:
    print(f"El numero {numero_usuario} es par")

elif numero_usuario%2!=0:
    print(f"El numero {numero_usuario} no es par")     
