# Programa para calcular el área de diferentes figuras geométricas

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    pi = 3.1416
    return pi * radio * radio


def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el lado.
    :param lado: Lado del cuadrado (float)
    :return: Área del cuadrado (float)
    """
    return lado * lado


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    :param base: Base del triángulo (float)
    :param altura: Altura del triángulo (float)
    :return: Área del triángulo (float)
    """
    return (base * altura) / 2


def main():
    """
    Función principal que gestiona la interacción con el usuario y llama a las funciones
    para calcular el área de las figuras geométricas.
    """
    while True:
        print("Elige la figura geométrica para calcular el área:")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Triángulo")
        print("4. Salir")

        opcion = int(input("Introduce el número de la opción: "))

        if opcion == 1:
            radio = float(input("Introduce el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo con radio {radio} es {area}")

        elif opcion == 2:
            lado = float(input("Introduce el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado con lado {lado} es {area}")

        elif opcion == 3:
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo con base {base} y altura {altura} es {area}")

        elif opcion == 4:
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor elige nuevamente.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
