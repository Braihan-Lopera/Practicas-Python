bandera = True

def calculadora(a, b):
        operador = str(input("Operacion a realizar:"))
        if operador  == "+":
            return print("Resultado:", a + b)
        elif operador == "*":
            return print("Resultado:", a * b)
        elif operador == "-":
            return print("Resultado:", a - b)
        elif operador == "/":
            return print("Resultado:", a / b)
        elif operador == "%":
            return print("Resultado:", a % b)
        else:
            return print("Operacion invalida!")

while bandera:
    num1 = float(input("Ingrese el numero: "))
    num2 = float(input("ingrese el otro numero: "))
    user = calculadora(num1, num2)
    salida = str(input("Desea salir? (SI/NO): ")).lower()
    print(salida)
    if salida == "si":
            bandera = False
    elif salida == "no":
            continue
    else:
        print("Valor incorrecto")
