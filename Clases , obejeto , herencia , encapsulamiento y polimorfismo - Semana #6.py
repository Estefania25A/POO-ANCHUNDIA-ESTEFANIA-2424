# Definición de la clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad  # Atributo encapsulado

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases derivadas")

    def get_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

    def __str__(self):
        return self.get_info()


# Definición de la clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self._raza = raza  # Atributo específico de la clase derivada

    def hacer_sonido(self):
        return "Guau"

    def get_info(self):
        base_info = super().get_info()  # Llamada al método de la clase base
        return f"{base_info}, Raza: {self._raza}"


# Definición de otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self._color = color  # Atributo específico de la clase derivada

    def hacer_sonido(self):
        return "Miau"

    def get_info(self):
        base_info = super().get_info()  # Llamada al método de la clase base
        return f"{base_info}, Color: {self._color}"


# Demostración del uso de las clases
def main():
    # Creación de instancias de las clases derivadas
    perro = Perro("Max", 5, "Labrador")
    gato = Gato("Luna", 3, "Negro")

    # Uso de los métodos de las instancias
    print(perro)  # Demostración del uso del método __str__ sobrescrito
    print(perro.hacer_sonido())  # Demostración de polimorfismo
    print(gato)  # Demostración del uso del método __str__ sobrescrito
    print(gato.hacer_sonido())  # Demostración de polimorfismo


if __name__ == "__main__":
    main()
