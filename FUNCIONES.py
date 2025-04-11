# Definir funciones para las operaciones básicas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"

# Función principal de la calculadora
def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    # Solicitar al usuario la operación
    opcion = int(input("Ingresa el número de la operación (1-4): "))
    
    # Pedir números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Realizar la operación seleccionada
    if opcion == 1:
        print("Resultado:", sumar(num1, num2))
    elif opcion == 2:
        print("Resultado:", restar(num1, num2))
    elif opcion == 3:
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == 4:
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida")

# Ejecutar la calculadora
calculadora()
