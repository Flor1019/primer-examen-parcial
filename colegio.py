# Para este algoritmo me basé en crear la Clase que representa la asistencia de un estudiante,
# así como las acciones de asistir, mostrar información, etc. y para finalizar ejecutarlo todo en una función 
# que funcionará como bucle y almacén de información.

class AsistenciaEstudiantes:
    def __init__(self, nombre, estado_asistencia):  # Corregido el nombre del constructor
        self.nombre = nombre
        self.estado_asistencia = estado_asistencia  # 'asistido', 'permiso', 'inasistencia'
        self.fecha = None
        self.razon_permiso = None

    def asignar_fecha(self, fecha):
        self.fecha = fecha

    def asignar_razon_permiso(self, razon):
        if self.estado_asistencia == "permiso":
            self.razon_permiso = razon

    def mostrar_info_asistencia(self):
        info = (f"Nombre: {self.nombre}\n"
                f"Estado de Asistencia: {self.estado_asistencia}\n"
                f"Fecha: {self.fecha if self.fecha else 'No asignada'}\n")
        if self.estado_asistencia == "permiso":
            info += f"Razón del Permiso: {self.razon_permiso if self.razon_permiso else 'No proporcionada'}\n"
        return info

# Función para solicitar los datos de asistencia de un estudiante
def solicitar_datos_asistencia():
    nombre = input("Ingrese el nombre del estudiante: ")
    estado_asistencia = input("Ingrese el estado de asistencia ('asistido', 'permiso', 'inasistencia'): ").strip().lower()
    return AsistenciaEstudiantes(nombre, estado_asistencia)

# Función que ejecuta el proceso de registro de asistencia en un bucle
def solicitud_while():
    registros_asistencia = []

    while True:
        estudiante = solicitar_datos_asistencia()
        
        # Asignar fecha a la asistencia
        fecha = input("Ingrese la fecha de asistencia (dd/mm/aaaa): ")
        estudiante.asignar_fecha(fecha)
        
        # Si el estado es "permiso", solicitar la razón
        if estudiante.estado_asistencia == "permiso":
            razon = input("Ingrese la razón del permiso: ")
            estudiante.asignar_razon_permiso(razon)

        registros_asistencia.append(estudiante)
        
        # Mostrar la información registrada
        print("\nInformación de Asistencia Registrada:")
        print(estudiante.mostrar_info_asistencia())
        
        continuar = input("\n¿Desea registrar la asistencia de otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    # Mostrar todos los registros al final
    print("\nRegistros de Asistencia Completos:")
    for i, estudiante in enumerate(registros_asistencia, start=1):
        print(f"\nRegistro {i}:")
        print(estudiante.mostrar_info_asistencia())

# Ejecutar la función de registro de asistencia
if __name__ == "__main__":  # Corregido el nombre del método de ejecución
    solicitud_while()
