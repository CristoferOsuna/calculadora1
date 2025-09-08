#Calculadora github

#Suma y Resta 

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")

while True:
    menu()
    opcion = input("Elige una opción (1-2): ")

    if opcion == "1":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"Resultado:= {sumar(num1, num2)}")

    elif opcion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"Resultado:= {restar(num1, num2)}")


        #Multiplicacion y Division 

def multiplicacion (num1, num2):
    return num1*num2

def division (num1, num2):
    if num2 != 0:
        return num1/num2 
    else:
        return "No es posible dividir por 0"
    
print("Elija la operacion que desea hacer:suma, resta, multiplicacion, division")

operacion=input("Que operacion desea hacer")

num1=float(input("Digite su primer numero: "))
num2=float(input("Digite su segundo numero: "))

if operacion == "multiplicacion":
    print("El resultado de su multiplicacion es: ",multiplicacion(num1 , num2))

elif operacion == "division":
    print("El resultado de su division es:",division(num1,num2))

else:
    print("Su operacion no es valida")