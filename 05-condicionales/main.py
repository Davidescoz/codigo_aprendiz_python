"""
Operadores de comparacion

== igual
=! diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que


Operadores Logicos

and y
or o
! negacion
not no

"""

#Ejemplo 1 


print("----------------PRIMER EJEMPLO -------------")



color="rojo"

#color=input("Adivina cual es mi color favorito: ")


if color == "rojo":
    print("Enhorabuena")
    print("El color es rojo ")

else:
    print("El color no es mi color favorito ")

#Ejemplo 3
print("\n----------------SEGUNDO EJEMPLO -------------")


#year=int(input("¿En que año estamos?: "))
year=2020

if year < 2021:
    print("Estamos antes del 2021")
else:
    print("Es un año posterior a 2021")

print("\n----------------TERCER EJEMPLO -------------")


nombre="Juan David"
ciudad="Medellin"
continente="Latinoamerica"
edad=18
mayoriaedad=18

if edad >= mayoriaedad:
   
    #Instrucciones
    print(f"{nombre} Es mayor de edad y esta listo pa la farra ome")

    if continente!="Latinoamerica":
        print(f"{nombre} no es Latino")

    else:
        print(f"{nombre} es Latino y de {ciudad} hpta")

else:
    print=f"{nombre} No es mayor de edad"
   



#Ejemplo 4
print("\n----------------CUARTO EJEMPLO -------------")



selectDia=1


"""
if selectDia==1:
    print("Lunes")

else:
    if selectDia==2:
        print("Martes")

    else:
        if selectDia==3:
            print("Miercoles")

        else:
            if selectDia==4:
                 print("Jueves")

            else:
                if selectDia==5:
                    print("Viernes")
                else:
                    print("Es fin de semana")
"""

if selectDia==1:
    print("Lunes")

elif selectDia==2:
    print("Martes") 

elif selectDia==3:
    print("Miercoles")

elif selectDia==2:
    print("Jueves") 

elif selectDia==2:
    print("Viernes")     

else:
    print("Es fin de semana")




#Ejemplo 5
print("\n----------------QUINTO EJEMPLO -------------") 



edad_minima=18
edad_maxima=65
edad_oficial=18

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Esta en edad de trabajar")

else: print("No esta en edad de trabajar")



#Ejemplo 6
print("\n----------------SEXTO EJEMPLO -------------") 


pais="España"

if pais=="Mexico" or pais=="España" or pais=="Colombia":
        print(f"{pais} es un pais de habla hispana")

else:
    print(f"{pais} no es de habla hispana")        


#Ejemplo 7
print("\n----------------SEPTIMO EJEMPLO -------------")     

pais="España"

if not (pais=="Mexico" or pais=="España" or pais=="Colombia"):
        print(f"{pais} no es un pais de habla hispana")

else:
    print(f"{pais} si es de habla hispana")  


#Ejemplo 8
print("\n----------------SEPTIMO EJEMPLO -------------")     

pais="Colombia"

if pais!="Mexico" and pais!="España" and pais!="Colombia":
        print(f"{pais} no es un pais de habla hispana")

else:
    print(f"{pais} si es de habla hispana")            