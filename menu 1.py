
import math
def porcentaje(num1 , num2):
    return num1*num2

def procentaje (num1, num2):
    if num2 != 0:
        return num1/num2 
    else:
        return "No es posible dividir por 0"
    
print("Elija la operacion que desea hacer:suma, resta, multiplicacion, division, raiz cuadrada, porcentajeqw")

operacion=input("Que operacion desea hacer")

num1=float(input("Digite su primer numero: "))
num2=float(input("Digite su segundo numero: "))

if operacion == "multiplicacion":
    print("El resultado de su multiplicacion es: ",multiplicacion(num1 , num2))

elif operacion == "division":
    print("El resultado de su division es:",division(num1,num2))

else:

