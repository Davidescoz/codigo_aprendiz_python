






print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
calculadora=int(input("Ingrese el numero de la operacion: "))

numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese el otro numero: "))
total=0

if calculadora==1:
    total=numero1+numero2
    print(f"La suma es: {int(total)}")

elif calculadora==2:
    total=numero1-numero2
    print(f"La resta es: {int(total)}")

elif calculadora==3:
    total=numero1*numero2
    print(f"La multiplicacion es: {int(total)}")

elif calculadora==4:
    total=numero1/numero2
    print(f"La division es: {int(total)}")    

else:
    print("El numero que usted no ha ingresado es valido por favor vuelva a intentarlo")   