# ====================================================
# SECCIÓN 1: FUNCIONES REUTILIZABLES
# ====================================================


# 1. Función de presentación del menú
def mostrar_menu():
    """Muestra las opciones del sistema en pantalla."""
    print("\n" + "="*40)
    print(" Sistema de gestión básica de productos ")
    print("="*40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("="*40)



#=======================================================================================================================
# 2. Funciones de validación de entradas

def validacion_ingreso_texto(texto_ingresado):
    """Pide un texto y asegura que no quede vacío ni con solo espacios."""

    texto = input(texto_ingresado).strip()

    while texto == "":

        print("Error: este campo no puede estar vacío.")
        texto = input(texto_ingresado).strip()
    return texto


def validacion_ingreso_numeros_positivo(numero_ingresado):
    """Pide un número y asegura que sea entero y mayor a 0."""
    numero = input(numero_ingresado).strip()

    while not numero.isdigit() or int(numero) <= 0:
        print("Error: debés ingresar un número entero mayor a 0.")
        numero = input(numero_ingresado).strip()  # Actualizamos la misma variable

    return int(numero)



#=======================================================================================================================
# 3. Función para buscar productos por nombre 
def buscar_producto(lista_productos):
    """Busca productos por nombre y muestra las coincidencias."""
    print("\n--- Buscar producto ---")

    # 1. Verificamos si la lista está vacía
    if not lista_productos:
        print("Todavía no hay productos cargados para buscar.")
        return

    # 2. Pedimos el término de búsqueda (usando nuestra función de validación)
    termino = validacion_ingreso_texto("Nombre del producto a buscar: ").lower()

    encontrados = 0

    # 3. Recorremos la lista buscando coincidencias
    for i, producto in enumerate(lista_productos, start=1):
        # producto[0] es el nombre del producto
        if termino in producto[0].lower():
            print(f"Coincidencia #{i} -> Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")

            encontrados += 1

    # 4. Informamos el resultado
    if encontrados == 0:
        print("No se encontraron resultados que coincidan con la búsqueda.")
    else:
        print(f"✓ Se encontraron {encontrados} producto(s).")



#=======================================================================================================================
# 4. Función para eliminar productos por número de lista

def eliminar_producto(lista_productos):
    """Muestra los productos cargados y elimina el seleccionado por el usuario."""
    print("\n--- Eliminar producto ---")

    # 1. Verificamos si la lista está vacía
    if not lista_productos:
        print("Todavía no hay productos cargados para eliminar.")
        return

    # 2. Mostramos los productos numerados para que el usuario elija cuál borrar
    print("Seleccioná el número del producto que deseas eliminar:\n")
    for i, producto in enumerate(lista_productos, start=1):
        print(f"{i}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")

    # 3. Pedimos el número usando la función de validación que ya creaste
    numero_opcion = validacion_ingreso_numeros_positivo("\n Ingresá el número del producto a eliminar: ")

    # 4. Validamos que el número ingresado esté dentro del rango existente
    while numero_opcion > len(lista_productos):
        print(f"Error: El número debe estar entre 1 y {len(lista_productos)}.")
        numero_opcion = validacion_ingreso_numeros_positivo("Ingresá el número del producto a eliminar: ")

    # 5. Convertimos la opción (1-based) al índice real de Python (0-based)
    indice = numero_opcion - 1

    # 6. Eliminamos el producto de la lista con .pop() y guardamos la sublista eliminada para avisarle al usuario
    producto_eliminado = lista_productos.pop(indice)

    print(f"✓ El producto '{producto_eliminado[0]}' fue eliminado exitosamente.")



#=======================================================================================================================
# PROGRAMA PRINCIPAL
#=======================================================================================================================

# Lista vacía para almacenar los productos
productos = []

while True:
    mostrar_menu()
    opcion = input("Elegí una opción (1-5): ").strip()

    # Opción 1: Agregar productos
    if opcion == "1":
        print("\n--- Agregar producto ---")
        nombre = validacion_ingreso_texto("Nombre del producto: ")
        categoria = validacion_ingreso_texto("Categoría del producto: ")
        precio = validacion_ingreso_numeros_positivo("Precio (sin centavos): ")

        productos.append([nombre, categoria, precio])
        print(f"✓ Producto '{nombre}' agregado exitosamente.")


    # Opción 2: Mostrar productos
    elif opcion == "2":

        if not productos:
            print("Todavía no hay productos cargados.")
        else:
            print("\n--- Lista de productos registrados ---")
            for i, producto in enumerate(productos, start=1):
                print(f"{i}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")


    # Opción 3: Buscar producto
    elif opcion == "3":
        buscar_producto(productos)


    # Opción 4: Eliminar producto
    elif opcion == "4":
        eliminar_producto(productos)


    # Opción 5: Salir del programa
    elif opcion == "5":
        print("¡Gracias por usar nuestro sistema!")
        break


    # Opción inválida    
    else:
        print("Opción inválida. Por favor, elegí una opción del 1 al 5.")
