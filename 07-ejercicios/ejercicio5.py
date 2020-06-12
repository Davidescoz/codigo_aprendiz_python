

numero1=int(input("¿Ingrese un numero?: "))
numero2=int(input("¿Ingrese otro numero?: "))
contador=0


if numero1 < numero2:

    for contador in range(numero1,(numero2 +1)):
        print(str(contador))

else:
    print("El numero 1 debe ser menor que el numero 2")