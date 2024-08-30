# Primero creamos una clase llamada productos y guardamos los datos como nombre, precio unitario y cantidad.
class Producto:
    def __init__(self, nombre, precio_unitario, cantidad):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    # usamos el metodo presente para presentar en una sola linea los datos 
    def __str__(self):
        return f"{self.nombre}: Precio Unitario: ${self.precio_unitario:.2f}, Cantidad: {self.cantidad}"


# Ahora creamos una Clase llamada Tienda y esta Maneja el inventario de productos y sus operaciones
class Tienda:
    def __init__(self):
        # Alamacenamos los datos de la insercion del mismo en una lista
        self.inventario = []

    # Agregamos un método para agregar productos al inventaro.
    def agregar_producto(self, producto):
        # Busca si el producto ya existe en el inventario.
        for p in self.inventario:
            if p.nombre == producto.nombre:
                # Si existe, aumenta la cantidad del producto.
                p.cantidad += producto.cantidad
                return
        # Si no existe, añade el producto al inventario.
        self.inventario.append(producto)

    # Creamos un metodo para mostrar todos los productos en el inventario.
    def mostrar_inventario(self):
        print("\nInventario de la Tienda:")
        for producto in self.inventario:
            print(producto)  # Muestra cada producto usando su representación en cadena.

    # y uno para registrar una venta de productos.
    def registrar_venta(self):
        print("\nRegistro de Venta:")
        total = 0  # Inicializa el total de la venta.
        while True:
            nombre_producto = input("Ingrese el nombre del producto vendido (o 'fin' para terminar): ")
            if nombre_producto.lower() == 'fin':
                break  # Finalizamos el registro de la venta si el usuario ingresa 'fin'.
            cantidad = self._obtener_cantidad("Ingrese la cantidad vendida: ")

            for producto in self.inventario:
                if producto.nombre == nombre_producto:
                    # y verifica si hay suficiente cantidad del producto.
                    if producto.cantidad >= cantidad:
                        producto.cantidad -= cantidad  # Reduce la cantidad en el inventario.
                        subtotal = producto.precio_unitario * cantidad
                        total += subtotal  # Suma al total de la venta.
                        print(f"Producto {nombre_producto} registrado. Subtotal: ${subtotal:.2f}")
                    else:
                        print(f"No hay suficiente cantidad de {nombre_producto}. Disponible: {producto.cantidad}.")
                        # Si no hay suficiente cantidad, permite ingresar una cantidad menor.
                        cantidad = self._obtener_cantidad("Ingrese una cantidad menor: ", max_valor=producto.cantidad)
                        producto.cantidad -= cantidad
                        subtotal = producto.precio_unitario * cantidad
                        total += subtotal
                        print(f"Producto {nombre_producto} registrado. Subtotal: ${subtotal:.2f}")
                    break
            else:
                # Informa si el producto no se encuentra en el inventario.
                print(f"Producto {nombre_producto} no encontrado en el inventario.")

        while True:
            vuelto = self._obtener_monto("Ingrese el monto entregado por el cliente: ")
            if vuelto < total:
                # Informa si el monto entregado es insuficiente y solicita volver a ingresarlo.
                print(f"El monto entregado es insuficiente. Total a pagar: ${total:.2f}. Vuelva a ingresar el monto.")
            else:
                print(f"Total: ${total:.2f}")
                print(f"Vuelto: ${vuelto - total:.2f}")
                break

    # este es un metodo para registrar productos recibidos de un proveedor.
    def registrar_proveedor(self):
        print("\nRegistro de Proveedor:")
        nombre_producto = input("Ingrese el nombre del producto recibido: ")
        precio_unitario = self._obtener_monto("Ingrese el precio sugerido de venta: ")
        cantidad = self._obtener_cantidad("Ingrese la cantidad recibida: ")

        # Crea un nuevo objeto Producto y lo agrega al inventario.
        producto = Producto(nombre_producto, precio_unitario, cantidad)
        self.agregar_producto(producto)

    # Método privado para obtener un monto válido del usuario.
    def _obtener_monto(self, mensaje):
        while True:
            try:
                monto = float(input(mensaje))
                if monto >= 0:
                    return monto  # Devuelve el monto si es un número positivo.
                else:
                    print("El monto debe ser un número positivo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    # Método privado para obtener una cantidad válida del usuario.
    def _obtener_cantidad(self, mensaje, max_valor=None):
        while True:
            try:
                cantidad = int(input(mensaje))
                if cantidad >= 0 and (max_valor is None or cantidad <= max_valor):
                    return cantidad  # Devuelve la cantidad si es un número positivo y no supera el máximo permitido.
                elif max_valor is not None:
                    print(f"La cantidad debe ser un número positivo y no mayor que {max_valor}.")
                else:
                    print("La cantidad debe ser un número positivo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")


# Función principal que ejecuta el programa.
def ventas_bucle():
    tienda = Tienda()  # Crea una instancia de la clase Tienda.

    while True:
        # Muestra un menú de opciones.
        print("\nOpciones:")
        print("1. Registrar producto de proveedor")
        print("2. Registrar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada: ").strip()

        # Ejecuta la acción correspondiente según la opción ingresada.
        if opcion == '1':
            tienda.registrar_proveedor()
        elif opcion == '2':
            tienda.registrar_venta()
        elif opcion == '3':
            tienda.mostrar_inventario()
        elif opcion == '4':
            print("¡Gracias por usar el sistema!")
            break  # Termina el programa si el usuario elige salir.
        else:
            print("Opción no válida. Intente de nuevo.")


# Mandamos a llamalar la clase ventas_bucle para que se encarge de cargar el resto de clases y de gestionar la salida de datos
if __name__ == "__main__":
    ventas_bucle()
