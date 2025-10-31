

titulos = [""] * 20
ejemplares = [0] * 20
contador = 0

# Funciones

def cargar_titulos_y_ejemplares():
    global contador
    while contador < 20:
        titulo = input("Ingrese el título del libro (o 'fin' para terminar): ")
        if titulo == "fin":
            break
        cantidad = int(input(f"Ingrese cantidad de ejemplares para '{titulo}': "))
        titulos[contador] = titulo
        ejemplares[contador] = cantidad
        contador += 1
    print("Carga finalizada")

def mostrar_catalogo():
    print("Catalogo completo:")
    for i in range(contador):
        print(f"{titulos[i]} → {ejemplares[i]} copias")
    print()

def consultar_disponibilidad():
    busqueda = input("Ingrese el titulo a consultar: ")
    for i in range(contador):
        if titulos[i] == busqueda:
            print(f"'{titulos[i]}' tiene {ejemplares[i]} copias")
            return
    print("El libro no se encuentra en el catalogo")

def listar_titulos_agotados():
    print("Titulos agotados:")
    encontrados = False
    for i in range(contador):
        if ejemplares[i] == 0:
            print(titulos[i])
            encontrados = True
    if not encontrados:
        print("No hay titulos agotados.")
    print()

def agregar_nuevo_titulo():
    global contador
    if contador >= 20:
        print("No se pueden agregar mas libros, se alcanzo el limite de 20")
        return
    titulo = input("Ingrese el nuevo titulo: ")
    cantidad = int(input(f"Ingrese la cantidad de ejemplares para '{titulo}': "))
    titulos[contador] = titulo
    ejemplares[contador] = cantidad
    contador += 1
    print(f"'{titulo}' agregado correctamente")

def actualizar_ejemplares():
    titulo = input("Ingrese el titulo del libro a actualizar: ")
    for i in range(contador):
        if titulos[i] == titulo:
            cambio = int(input("Ingrese la cantidad a sumar (devolucion) o restar (prestamo): "))
            if ejemplares[i] + cambio < 0:
                print("No se puede tener menos de 0 ejemplares.\n")
                return
            ejemplares[i] += cambio
            print(f"Ejemplares actualizados. Ahora '{titulos[i]}' tiene {ejemplares[i]} copias.\n")
            return
    print("El libro no se encuentra en el catálogo")

# Menu

while True:
    print("=== Menú Biblioteca ===")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catálogo completo")
    print("3. Consultar disponibilidad")
    print("4. Listar títulos agotados")
    print("5. Agregar un nuevo título")
    print("6. Actualizar ejemplares (préstamo/devolución)")
    print("7. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        cargar_titulos_y_ejemplares()
    elif opcion == "2":
        mostrar_catalogo()
    elif opcion == "3":
        consultar_disponibilidad()
    elif opcion == "4":
        listar_titulos_agotados()
    elif opcion == "5":
        agregar_nuevo_titulo()
    elif opcion == "6":
        actualizar_ejemplares()
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intente de nuevo")
