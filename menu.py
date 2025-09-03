#Calculadora
import math

operacion=str(input("¿Que operacion quiere? suma, resta, multiplicacion, division: "))
#suma
def suma(num1,num2):
        num1=(float(input("Digite un numero: ")))
        num2=(float(input("Digite un numero: ")))
        suma= num1+num2
        
        if operacion == suma:
            print ("Su refultado fue: ",suma)
def resta(num1,num2):
        num1=(float(input("Digite un numero: ")))
        num2=(float(input("Digite un numero: ")))
        resta= num1-num2


if operacion == resta: 
    print ("Su resultado fue: ",resta)








































num1=(float(input("Digite un numero: ")))
num2=(float(input("Digite un numero: ")))
suma= num1+num2

print("Su suma fue: ",suma)