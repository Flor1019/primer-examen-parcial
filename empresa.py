# En este caso, inicio creando una clase base llamada Empleado que representará a cualquier empleado en la empresa.
# Luego, crearé dos clases derivadas: EmpleadoPlazaFija y EmpleadoPorHoras.
# Implementaré los cálculos de la planilla de pago, incluyendo un bono adicional para empleados con más de 5 años de servicio.
# Finalmente, se creará un bucle para manejar múltiples empleados y calcular sus pagos.

class Empleado:
    def __init__(self, nombre, años_trabajados):  # Corregido el nombre del constructor
        self.nombre = nombre
        self.años_trabajados = años_trabajados

    def calcular_bono_antigüedad(self):
        if self.años_trabajados > 5:
            return 100  # Bono fijo de 100 unidades monetarias para empleados con más de 5 años
        return 0

    def calcular_pago(self):
        pass  # Este método será implementado por las clases derivadas

    def tipo_empleado(self):
        pass  # Este método será implementado por las clases derivadas

class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, años_trabajados, salario_base, comisiones):  # Corregido el nombre del constructor
        super().__init__(nombre, años_trabajados)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_pago(self):
        pago_base = self.salario_base + self.comisiones
        bono = self.calcular_bono_antigüedad()
        return pago_base + bono

    def tipo_empleado(self):
        return "Empleado de Plaza Fija"

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, años_trabajados, horas_trabajadas, tarifa_por_hora):  # Corregido el nombre del constructor
        super().__init__(nombre, años_trabajados)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self):
        pago_base = self.horas_trabajadas * self.tarifa_por_hora
        bono = self.calcular_bono_antigüedad()
        return pago_base + bono

    def tipo_empleado(self):
        return "Empleado por Horas"

# Función para solicitar los datos de un empleado y crear el objeto correspondiente
def solicitar_datos_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    años_trabajados = int(input("Ingrese los años trabajados: "))
    tipo_empleado = input("¿Es un empleado de plaza fija o por horas? (fija/horas): ").strip().lower()

    if tipo_empleado == "fija":
        salario_base = float(input("Ingrese el salario base: "))
        comisiones = float(input("Ingrese las comisiones: "))
        return EmpleadoPlazaFija(nombre, años_trabajados, salario_base, comisiones)
    elif tipo_empleado == "horas":
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
        tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
        return EmpleadoPorHoras(nombre, años_trabajados, horas_trabajadas, tarifa_por_hora)
    else:
        print("Tipo de empleado no reconocido.")
        return None

# Función que ejecuta el proceso de cálculo de planilla en un bucle
def calcular_planilla():
    empleados = []

    while True:
        empleado = solicitar_datos_empleado()
        if empleado:
            empleados.append(empleado)
            pago = empleado.calcular_pago()
            print(f"\nPago para {empleado.nombre} ({empleado.tipo_empleado()}): ${pago:.2f}")
        
        continuar = input("\n¿Desea registrar a otro empleado? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    # Mostrar todos los pagos al final
    print("\nPagos Completos:")
    for i, empleado in enumerate(empleados, start=1):
        pago = empleado.calcular_pago()
        print(f"\nEmpleado {i}:")
        print(f"Nombre: {empleado.nombre}")
        print(f"Tipo: {empleado.tipo_empleado()}")
        print(f"Pago Total: ${pago:.2f}")

# Ejecutar la función de cálculo de planilla
if __name__ == "__main__":
    calcular_planilla()
