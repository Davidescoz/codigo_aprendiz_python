"""

for contador in iterador:
    #Ejecuta bloque de instrucciones hasta que contador sea igual al rango del iterador (listas,rangos,etc)

"""

contador=0
resultado=0

for contador in range(0,10):
    print("Va por el numero: "+str(contador))
    resultado+=contador



print(f"el resultado es: {resultado}")


#Ejemplo tablas de multiplicar

print("------------------------EJEMPLO---------------------")


numero_usuario=int(input("¿De que numero quieres ver la tabla?: "))
numero_tablas=0

if numero_usuario < 1:
    numero_usuario=1
    
    
    print(f"### Tabla de multiplicar del numero {numero_usuario} ###")


for numero_tablas in range(1,11):

        if numero_usuario==45:
            print("No se pueden mostrar numeros prohibidos")
            break ##Finalizar una instruccion 

        print(f"{numero_usuario} x {numero_tablas} = {numero_usuario*numero_tablas}")
 
else:
    print("Tabla finalizada")




