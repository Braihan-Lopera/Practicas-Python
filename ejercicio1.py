num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo numero: "))

operation = str(input("ingrese la operacion a realizar(+, -, *, /): "))

if operation == "+":
    sum = num1 + num2
    print("Resultado: " , sum)
elif operation == "-":
    rest = num1 - num2
    print("Resultado: " , rest)
elif operation == "*":
    mult = num1 * num2
    print("Resultado: " , mult)
elif operation == "/":
    div = num1 / num2
    print("Resultado: " , div)
else:
    print("Valor incorrecto")

