from operaciones_matematicas import *

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == "+":
    resultado = sumar(num1, num2)
elif operacion == "-":
    resultado = restar(num1, num2)
elif operacion == "*":
    resultado = multiplicar(num1, num2)
elif operacion == "/":
    resultado = dividir(num1, num2)
else:
    print("Operación inválida")

print("Resultado:", resultado)