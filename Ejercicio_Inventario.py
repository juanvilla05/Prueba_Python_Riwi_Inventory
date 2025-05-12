# Vamos a empezar creando una lista para guardar la información de nuestros productos.
# Cada producto será un "diccionario", donde guardamos información con etiquetas (claves) y su valor (nombre,precio,cantidad)
inventario = []

# Ahora, vamos a crear 5 productos iniciales en el inventario, según se indica en el ejercicio.
# Usaremos la misma estructura de diccionario con las claves 'titulo', 'precio' y 'cantidad'.
product_1 = {"nombre": "tenis", "precio": 20.50, "cantidad": 10}
product_2 = {"nombre": "Camisetas", "precio": 18.50, "cantidad": 5}
product_3 = {"nombre": "Billeteras", "precio": 35.50, "cantidad": 3}
product_4 = {"nombre": "Gorras", "precio": 20.20, "cantidad": 8}
product_5 = {"nombre": "Jeans", "precio": 55.20, "cantidad": 12}

# Con .append Agregamos estos productos iniciales a nuestra lista de inventario.
inventario.append(product_1)
inventario.append(product_2)
inventario.append(product_3)
inventario.append(product_4)
inventario.append(product_5)

# --------------------------------------------------------------------------
# 1. Función para añadir un nuevo Producto al inventario.
# --------------------------------------------------------------------------
def agregar_producto() -> None: 
    """
    Esta función permite añadir un nuevo producto al inventario.
    Pide al usuario el nombre (str), precio (float) y cantidad (int) del producto,
    """
    print("\n--- [ Añade un Nuevo Producto al Inventario ]---")
    # Pedimos al usuario que ingrese el nombre del nuevo producto.
    nombre_nuevo_producto: str = input("Ingresa el nombre del producto: ") 
    # Vamos a asegurarnos de que el precio sea un número positivo.
    while True:
        try:
            nuevo_precio_str: str = input("Ingresa el precio del producto: ")
            nuevo_precio: float = float(nuevo_precio_str)
            if nuevo_precio > 0:
                break
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido para el precio.")

    # También nos aseguramos de que la cantidad sea un número entero positivo.
    while True:
        try:
            nueva_cantidad_str: str = input("Ingresa la cantidad disponible: ")
            nueva_cantidad: int = int(nueva_cantidad_str)
            if nueva_cantidad >= 0:
                break
            else:
                print("La cantidad debe ser un número positivo o cero.")
        except ValueError:
            print("Por favor, ingresa un número entero válido para la cantidad.")

    # Creamos un nuevo diccionario {} con la información del producto.
    nuevo_producto = {"nombre": nombre_nuevo_producto, "precio": nuevo_precio, "cantidad": nueva_cantidad}
    # Añadimos este nuevo diccionario a nuestra lista de inventario.
    inventario.append(nuevo_producto)
    print(f"El producto '{nombre_nuevo_producto}' ha sido añadido al inventario.")

# --------------------------------------------------------------------------
# 2. Función para consultar un producto en el inventario por su nombre.
# --------------------------------------------------------------------------
def consultar_producto() -> None:
    """
    Esta función permite consultar los detalles de un producto en el inventario por su nombre (str).
    Recorre la lista 'inventario' y muestra el nombre (str),
    precio (float) y cantidad (int) del producto si se encuentra.
    """
    print("\n--- [ Consultar Producto ] ---")
    nombre_buscar: str = input("Ingresa el nombre del producto que deseas buscar: ")
    encontrado: bool = False
    # Recorremos cada producto en nuestra lista de inventario.
    for producto in inventario:
        # Comparamos el nombre (str) que ingresó el usuario con el nombre (str) del producto actual.
        if producto["nombre"].lower() == nombre_buscar.lower():
            # Si los nombres coinciden (ignorando si son mayúsculas o minúsculas), mostramos la información del producto.
            print(f"nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}") # El :.2f es para mostrar el precio con dos decimales.
            print(f"Cantidad disponible: {producto['cantidad']}")
            encontrado = True
            break # Si encontramos el producto, no necesitamos seguir buscando.
    # Si después de revisar todos los producto no encontramos el nombre, mostramos un mensaje.
    if not encontrado:
        print(f"El producto '{nombre_buscar}' no se encuentra en el inventario.")

# --------------------------------------------------------------------------
# 3. Función para actualizar el precio de un producto
# --------------------------------------------------------------------------
def actualizar_precio() -> None:
    """
    Esta función permite actualizar el precio (float) de un producto en el inventario.
    Pide al usuario el nombre (str) del producto y el nuevo precio (float),
    valida el nuevo precio y actualiza el precio en el diccionario correspondiente
    dentro de la lista 'inventario'.
    """
    print("\n--- [ Actualizar Precio del Producto ] ---")
    producto_actualizar: str = input("Ingresa el nombre del producto cuyo precio deseas actualizar: ")
    encontrado: bool = False
    # Buscamos el producto por su nombre (str).
    for producto in inventario:
        if producto["nombre"].lower() == producto_actualizar.lower():
            encontrado = True
            # Si encontramos el producto, pedimos el nuevo precio (float).
            while True:
                try:
                    nuevo_precio_str: str = input("Ingresa el nuevo precio del producto: ")
                    nuevo_precio: float = float(nuevo_precio_str)
                    if nuevo_precio > 0:
                        # Actualizamos el precio (float) del producto en el diccionario.
                        producto["precio"] = nuevo_precio
                        print(f"El precio de '{producto['nombre']}' ha sido actualizado a ${nuevo_precio:.2f}.")
                        break # Salimos del bucle de validación del precio.
                    else:
                        print("El precio debe ser un número positivo.")
                except ValueError:
                    print("Por favor, ingresa un número válido para el precio.")
            break # Salimos del bucle de búsqueda del producto.
    # Si no encontramos el producto, mostramos un mensaje.
    if not encontrado:
        print(f"El producto '{producto_actualizar}' no se encuentra en el inventario.")

# --------------------------------------------------------------------------
# 4. Función para eliminar un producto del inventario
# --------------------------------------------------------------------------
def eliminar_producto() -> None:
    """
    Esta función permite eliminar un producto del inventario.
    Pide al usuario el nombre (str) del producto a eliminar, busca el producto en la lista 'inventario'
    y, tras confirmación (str), lo elimina.
    """
    print("\n--- [ Eliminar producto del Inventario ] ---")
    producto_eliminar: str = input("Ingresa el nombre del producto que deseas eliminar: ")
    encontrado_indice: int = -1 # Usaremos esto para recordar la posición del producto si lo encontramos.
    
    for indice, producto in enumerate(inventario):
        if producto["nombre"].lower() == producto_eliminar.lower():
            encontrado_indice = indice
            break # Encontramos el producto, no necesitamos seguir buscando.

    # Si encontramos el producto, pedimos confirmación (str) antes de eliminarlo.
    if encontrado_indice != -1:
        confirmacion: str = input(f"¿Estás seguro de que deseas eliminar '{inventario[encontrado_indice]['nombre']}'? (si/no): ")
        if confirmacion.lower() == 'si':
            # Eliminamos el producto de la lista usando el índice (int) que guardamos.
            producto_eliminado: str = inventario.pop(encontrado_indice)
            print(f"El producto '{producto_eliminado['nombre']}' ha sido eliminado del inventario.")
        else:
            print("No se ha eliminado el producto.")
    else: 
        print(f"El producto '{producto_eliminar}' no se encuentra en el inventario.")

# --------------------------------------------------------------------------
# 5. Función para calcular el valor total del inventario
# --------------------------------------------------------------------------
def calcular_valor_total() -> None:
    """
    Esta función calcula el valor total del inventario.
    Recorre cada producto en la lista 'inventario'
    multiplica su precio (float) por su cantidad (int) y suma al valor total (float).
    Finalmente, muestra el valor total.
    """
    valor_total: float = 0
    
    for producto in inventario:
        # Multiplicamos el precio (float) del producto por su cantidad (int) y sumamos al valor total (float).
        valor_total += producto["precio"] * producto["cantidad"]
    # Mostramos el valor total (float) con dos decimales.
    print(f"\nEl valor total del inventario es: ${valor_total:.2f}")

def main() -> None:
    """
    Función principal que ejecuta el menú de gestión de inventario de la tienda.
    Muestra las opciones al usuario y llama a las funciones correspondientes según su elección.
    El bucle principal continúa hasta que el usuario elige la opción de salir ('6').
    """
    while True:
        print("\n--- [ Gestión de Inventario de la Tienda ] ---")
        print("Selecciona una opción:")
        print("1. Añadir producto al inventario")
        print("2. Consultar producto en inventario")
        print("3. Actualizar precio del producto")
        print("4. Eliminar producto del inventario")
        print("5. Calcular el valor total del inventario")
        print("6. Salir")

        opcion: str = input("Ingresa el número de la opción deseada: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_producto()
        elif opcion == '3':
            actualizar_precio()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            calcular_valor_total()
        elif opcion == '6':
            print("¡Gracias por Visitarnos, Vuelve Pronto!")
            break # Salimos del bucle principal y el programa termina.
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Esta condición asegura que la función main() se ejecute solo cuando el script se ejecuta directamente.
if __name__ == "__main__":
    main()
