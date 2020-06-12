"""

BUCLE WHILE 
    ES UNA ESTRUCTURA DE CONTROL QUE REPITE UNA SERIE DE INSTRUCCIONES TANTAS VECES COMO SEA NECESARIO HASTA QUE DEJE 
    DE CUMPLIRSE LA CONDICION


    while condicion:
        bloque de instrucciones
        actualizacion del contador

"""


contador=1

while contador <=100:
    print(f"Estoy en el numero {contador}")
    contador+=1

print("----------------------------------------------------------------")

contador=1
muestrame=str(0)

while contador <=100:
    
    muestrame=muestrame+ ", " + str(contador)
    contador+=1

print(muestrame)

print("----------------------------------------------------------------")

numero_usuario=int(input("¿Que tabla de multiplicar deseas ver?: "))


if numero_usuario < 1:
    numero_usuario=1

print(f"#### Tabla del {numero_usuario} ####")  
    
numero_tablas=1
while numero_tablas <=11:
    print(f"{numero_usuario} x {numero_tablas} = {numero_usuario*numero_tablas}")
    numero_tablas+=1
else:
    print("Tabla finalizada")    
