



numero1=int(input("Ingrese un numero de: "))
numero2=int(input("Ingrese un numero hasta: "))
contador=0

if numero1 < numero2:

    for contador in range(numero1,(numero2 + 1)):
        if contador%2==0:
            print(f"{contador} - par")
        else:
            print(f"{contador} - inpar")    

else:
    print("El numero 1 debe ser mayor al numero 2")        