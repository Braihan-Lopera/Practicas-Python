bandera = False  # CAMBIO: Inicialmente falsa para demo de conflictos


def calculadora(a, b):
    operador = str(input("Elija operación (+, -, *, /, %): "))  # MODIFICADO: Prompt más claro
    if operador == "+":
        print(f"Resultado de suma: {a + b}")  # AGREGADO: f-string y mensaje específico
        return a + b
    elif operador == "-":
        return print("Resultado resta:", a - b)  # MODIFICADO: Orden de if cambiado
    elif operador == "*":
        return print("Resultado:", a * b)
    elif operador == "/":
        if b != 0:  # AGREGADO: Validación de división por cero
            return print("Resultado:", a / b)
        else:
            return print("Error: División por cero!")
    elif operador == "%":
        return print(f"Residuo: {a % b}")  # MODIFICADO: Mensaje y f-string
    else:
        print("¡Operación inválida! Intente nuevamente.")  # MODIFICADO: Mensaje mejorado
        return None  # AGREGADO: Return explícito


while bandera:
    try:  # AGREGADO: Manejo de errores en inputs
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))
    except ValueError:
        print("¡Ingrese números válidos!")
        continue
    
    resultado = calculadora(num1, num2)  # MODIFICADO: Captura return
    if resultado is None:
        continue
    
    while True:  # MODIFICADO: Loop interno para validación
        salida = input("Continuar? (si/no): ").lower().strip()
        if salida in ["si", "sí"]:
            break
        elif salida == "no":
            bandera = False
            break
        else:
            print("Responda 'si' o 'no'")
    
    print("¡Gracias por usar la calculadora mejorada!")  # AGREGADO: Mensaje final
