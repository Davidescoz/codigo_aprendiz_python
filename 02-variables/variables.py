"""
Una variables es un contenedor de informacion en la cual podemos almacenar un dato, se pueden crear multitud de variables
y contener distintos tipos de datos e informacion

"""

texto="Master en Python"
texto2= "Con Victor Robles"
numero= 45
decimal=6.7

## Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("---------------------------------")

#Cambiando el valor de las variables 
numero=77
decimal=8.9
print(numero)
print(decimal)

print("---------------------------------")


#Concatenacion


nombre= "Juan David"
apellidos="Zuleta Escobar"
web="techwebsite.online"


print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola a todos me llamo {} {} y mi web es:{}".format(nombre,apellidos,web))
