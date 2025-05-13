# 🛍️ Gestión de Inventario de Tienda 🚀

¡Bienvenido al sistema de gestión de inventario de tu tienda! 📦 Este programa en Python te permite llevar un control detallado de tus productos, desde añadirlos hasta calcular el valor total de tu stock. ¡Manos a la obra!

## 📘 Version Ingles
[Click here to see English version](README_English.md)

## ⚙️ Instrucciones de Ejecución

Para poner en marcha este sistema, sigue estos sencillos pasos:

1.  **💾 Guarda el código:** Asegúrate de haber guardado el código Python en un archivo. Puedes llamarlo, por ejemplo, `inventario.py`.
2.  **🐍 Abre tu terminal o línea de comandos:** Navega hasta el directorio donde guardaste el archivo `inventario.py`.
3.  **🚀 Ejecuta el programa:** Escribe el siguiente comando y presiona Enter:

    ```bash
    python inventario.py
    ```

    ¡Verás aparecer el menú principal! 🎉

## 📝 Ejemplo de Datos de Entrada y Salida

Aquí tienes un vistazo de cómo interactúa el programa:

**Añadir un nuevo producto:**

--- [ Añade un Nuevo Producto al Inventario ]---
Ingresa el nombre del producto: Nuevo Producto
Ingresa el precio del producto: 25.99
Ingresa la cantidad disponible: 50
El producto 'Nuevo Producto' ha sido añadido al inventario.


**Consultar un producto:**

--- [ Consultar Producto ] ---
Ingresa el nombre del producto que deseas buscar: tenis
nombre: tenis
Precio: $20.50
Cantidad disponible: 10


**Actualizar el precio de un producto:**

--- [ Actualizar Precio del Producto ] ---
Ingresa el nombre del producto cuyo precio deseas actualizar: Camisetas
Ingresa el nuevo precio del producto: 19.99
El precio de 'Camisetas' ha sido actualizado a $19.99.


**Eliminar un producto:**

--- [ Eliminar producto del Inventario ] ---
Ingresa el nombre del producto que deseas eliminar: Billeteras
¿Estás seguro de que deseas eliminar 'Billeteras'? (si/no): si
El producto 'Billeteras' ha sido eliminado del inventario.


**Calcular el valor total del inventario:**

--- [ Gestión de Inventario de la Tienda ] ---
Selecciona una opción:
5. Calcular el valor total del inventario

El valor total del inventario es: $1735.70


**Salir del programa:**

--- [ Gestión de Inventario de la Tienda ] ---
Selecciona una opción:
6. Salir
¡Gracias por Visitarnos, Vuelve Pronto!


## ✨ Funcionalidades Principales

Este sistema de gestión de inventario ofrece las siguientes funcionalidades esenciales:

1.  **➕ Añadir Producto:** Permite agregar nuevos artículos al inventario, solicitando su nombre, precio y cantidad disponible. ¡Tu catálogo siempre actualizado! 🆕
2.  **🔍 Consultar Producto:** Busca un producto por su nombre y muestra sus detalles: nombre, precio y cantidad en stock. ¡Encuentra la información al instante! 🔎
3.  **💰 Actualizar Precio:** Modifica el precio de un producto existente en el inventario. ¡Mantén tus precios al día! 🏷️
4.  **🗑️ Eliminar Producto:** Remueve un producto del inventario. ¡Cuando un artículo ya no esté disponible! 💨
5.  **📊 Calcular Valor Total:** Calcula el valor económico total de todos los productos en el inventario. ¡Una visión clara de tu capital! 📈
6.  **🚪 Salir:** Cierra el programa de forma segura. ¡Hasta la próxima gestión! 👋

## 🧱 Estructura del Programa

El programa se organiza de la siguiente manera:

* **`inventario` (lista):** Una lista que actúa como la base de datos de nuestros productos. Cada producto se almacena como un diccionario. 📒
* **Diccionarios de Producto:** Cada producto en la lista `inventario` es un diccionario con las siguientes claves:
    * `"nombre"` (str): El nombre del producto.
    * `"precio"` (float): El precio unitario del producto.
    * `"cantidad"` (int): La cantidad disponible en stock.
* **Funciones:** El programa se divide en funciones para modularizar las diferentes acciones:
    * `agregar_producto()`: Añade un nuevo producto al inventario.
    * `consultar_producto()`: Busca y muestra la información de un producto.
    * `actualizar_precio()`: Modifica el precio de un producto.
    * `eliminar_producto()`: Elimina un producto del inventario.
    * `calcular_valor_total()`: Calcula el valor total del inventario.
    * `main()`: La función principal que contiene el menú de interacción con el usuario y llama a las demás funciones.
     

## 🧠 Lógica y Funcionamiento

La lógica del programa se centra en la manipulación de la lista `inventario`.

* **Añadir:** Se crea un nuevo diccionario con la información proporcionada por el usuario y se añade a la lista `inventario` usando `.append()`.
* **Consultar:** Se itera sobre la lista `inventario`. Para cada producto, se compara (ignorando mayúsculas) el nombre ingresado por el usuario con el nombre del producto actual. Si coinciden, se muestra la información.
* **Actualizar:** Similar a la consulta, se busca el producto por nombre. Una vez encontrado, se solicita el nuevo precio y se actualiza el valor en el diccionario del producto.
* **Eliminar:** Se busca el producto por nombre y se guarda su índice en la lista. Se pide confirmación al usuario antes de eliminar el elemento de la lista usando `.pop()` con el índice guardado.
* **Calcular Valor Total:** Se recorre la lista `inventario`. Para cada producto, se multiplica su precio por su cantidad y se suma a un acumulador. Finalmente, se muestra el total.
* **Menú Principal:** La función `main()` presenta un bucle `while` que muestra las opciones al usuario y ejecuta la función correspondiente según su elección. El bucle se rompe cuando el usuario elige la opción de salir.

¡Espero que este README te guie y sea de gran utilidad para comprender las funciones y estructura de la tienda! 😊
