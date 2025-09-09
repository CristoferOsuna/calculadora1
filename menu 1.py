

import math

def porcentaje(valor, porcentaje):
    if porcentaje >= 0:

        return (valor * porcentaje) / 100
    
    else:
        return "No es posible dividir por 0: "
    
print("Elija la operacion que desea hacer: suma, resta, multiplicacion, division, raiz cuadrada, porcentaje")

operacion=input("Que operacion desea hacer: ")

num1=float(input("Digite su primer numero: "))
num2=float(input("Digite su segundo numero: "))

if operacion == "porcentaje":
    print("El resultado de su porcentaje es: ", porcentaje(num1 , num2))

else:
    print("Su operacion no es valida")

