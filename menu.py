#Calculadora github


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