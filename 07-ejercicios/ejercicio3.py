"""
    Ejercicio 3
        -Imprimir los cuadrados de los primeros 60 numeros naturales
        -
"""        



print("----------------------------BUCLE HECHO CON WHILE---------------------\n")

contador=1

while contador <= 60:
    contador=contador+1
    cuadrado=contador*contador
    print(f"{contador} al cuadrado es = {cuadrado}")
    

print("\n----------------------------BUCLE HECHO CON FOR---------------------\n")

contador2=1
cuadrado2=1

for contador2 in range(1,60):
    print(f"{str(contador2)} al cuadrado es = {contador2*contador2}")
