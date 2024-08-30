# En este caso, inicio creando la clase que representa una reserva en el hotel.
# La clase Reserva tiene métodos para agregar servicios extra, calcular el total y mostrar la factura.
# Los servicios extra se almacenan como una lista de tuplas (servicio, costo).
# El costo total se calcula sumando el costo de los servicios extra y el costo de la habitación por noche.
# Los tipos de habitación y servicios extra deben ser definidos al inicio del programa.

class Reserva:
    def __init__(self, nombre_cliente, tipo_habitacion, numero_noches):
        self.nombre_cliente = nombre_cliente
        self.tipo_habitacion = tipo_habitacion
        self.numero_noches = numero_noches
        self.servicios_extra = []
        self.total_gastos = 0

    def agregar_servicio_extra(self, servicio, costo):
        self.servicios_extra.append((servicio, costo))
        self.total_gastos += costo

    def calcular_total(self, costo_habitacion):
        self.total_gastos += costo_habitacion * self.numero_noches

    def mostrar_factura(self):
        factura = (f"Cliente: {self.nombre_cliente}\n"
                   f"Habitación: {self.tipo_habitacion}\n"
                   f"Noches: {self.numero_noches}\n"
                   f"Servicios Extra:\n")
        for servicio, costo in self.servicios_extra:
            factura += f"- {servicio}: ${costo:.2f}\n"
        factura += f"Total a Pagar: ${self.total_gastos:.2f}\n"
        return factura

# Función para solicitar los datos de la reserva
def solicitar_datos_reserva():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    tipo_habitacion = input("Ingrese el tipo de habitación seleccionada (Ej. Sencilla, Doble, Suite): ")
    numero_noches = int(input("Ingrese el número de noches: "))
    return Reserva(nombre_cliente, tipo_habitacion, numero_noches)

# Función para mostrar y seleccionar servicios extra
def seleccionar_servicios_extra(reserva):
    servicios_disponibles = {
        "piscina": 20.0,   # Costo adicional por usar la piscina
        "cancha de golf": 50.0  # Costo adicional por usar la cancha de golf
    }
    
    while True:
        print("\nServicios Extra Disponibles:")
        for servicio, costo in servicios_disponibles.items():
            print(f"- {servicio.capitalize()}: ${costo:.2f}")
        
        agregar_servicio = input("¿Desea agregar un servicio extra? (s/n): ").strip().lower()
        if agregar_servicio == 's':
            servicio = input("Ingrese el nombre del servicio extra (Ej. Piscina, Cancha de golf): ").strip().lower()
            if servicio in servicios_disponibles:
                costo = servicios_disponibles[servicio]
                reserva.agregar_servicio_extra(servicio.capitalize(), costo)
            else:
                print("Servicio no disponible.")
        else:
            break

# Función que ejecuta el proceso de reserva en un bucle
def repetir_reservacion():
    reservas = []

    while True:
        reserva = solicitar_datos_reserva()
        
        costo_habitacion = float(input("Ingrese el costo de la habitación por noche: "))
        reserva.calcular_total(costo_habitacion)

        seleccionar_servicios_extra(reserva)

        reservas.append(reserva)
        
        # Mostrar la factura
        print("\nFactura Generada:")
        print(reserva.mostrar_factura())
        
        continuar = input("\n¿Desea realizar otra reserva? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    # Mostrar todas las reservas al final
    print("\nReservas Completas:")
    for i, reserva in enumerate(reservas, start=1):
        print(f"\nReserva {i}:")
        print(reserva.mostrar_factura())

# Ejecutar la función de reserva
if __name__ == "__main__":  # Corregido el nombre del método de ejecución
    repetir_reservacion()
