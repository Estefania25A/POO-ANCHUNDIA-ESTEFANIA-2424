# Clase Cliente que representa a un cliente del hotel
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f'Cliente: {self.nombre}, Email: {self.email}'

# Clase Habitacion que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        self.ocupada = True

    def liberar(self):
        self.ocupada = False

    def __str__(self):
        estado = 'Ocupada' if self.ocupada else 'Disponible'
        return f'Habitación {self.numero} ({self.tipo}) - {estado}'

# Clase Reserva que representa una reserva en el hotel
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def costo_total(self):
        return self.dias * self.habitacion.precio

    def __str__(self):
        return f'Reserva de {self.cliente.nombre} en {self.habitacion.tipo} por {self.dias} días. Costo total: ${self.costo_total()}'

# Crear clientes
cliente1 = Cliente('Juan Pérez', 'juan@example.com')
cliente2 = Cliente('Ana García', 'ana@example.com')

# Crear habitaciones
habitacion1 = Habitacion(101, 'Individual', 50)
habitacion2 = Habitacion(102, 'Doble', 75)

# Realizar reservas
reserva1 = Reserva(cliente1, habitacion1, 3)
reserva2 = Reserva(cliente2, habitacion2, 2)

# Mostrar detalles de las reservas
print(reserva1)
print(reserva2)

# Marcar las habitaciones como ocupadas
habitacion1.reservar()
habitacion2.reservar()

# Mostrar el estado de las habitaciones
print(habitacion1)
print(habitacion2)
