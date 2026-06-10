# Programa de Programación Tradicional
# Registro y visualización de información de mascotas

mascotas = []


def registrar_mascota():
    """
    Función para registrar una nueva mascota solicitando datos por teclado
    """
    print("\n" + "="*50)
    print("REGISTRO DE NUEVA MASCOTA")
    print("="*50)
    
    # Solicitar datos por teclado
    nombre = input("Ingrese el nombre de la mascota: ").strip()
    tipo = input("Ingrese el tipo de mascota (perro, gato, pájaro, etc.): ").strip()
    edad = input("Ingrese la edad de la mascota: ").strip()
    color = input("Ingrese el color de la mascota: ").strip()
    raza = input("Ingrese la raza de la mascota: ").strip()
    dueno = input("Ingrese el nombre del dueño: ").strip()
    
    # Crear un diccionario con la información de la mascota
    mascota = {
        "nombre": nombre,
        "tipo": tipo,
        "edad": edad,
        "color": color,
        "raza": raza,
        "dueno": dueno
    }
    
    # Agregar la mascota a la lista
    mascotas.append(mascota)
    print("\n✓ Mascota registrada exitosamente!")


def mostrar_todas_mascotas():
    """
    Función para mostrar la información de todas las mascotas registradas
    """
    if len(mascotas) == 0:
        print("\n" + "="*50)
        print("No hay mascotas registradas")
        print("="*50)
        return
    
    print("\n" + "="*50)
    print("MASCOTAS REGISTRADAS")
    print("="*50)
    
    for indice, mascota in enumerate(mascotas, 1):
        mostrar_mascota_individual(mascota, indice)


def mostrar_mascota_individual(mascota, numero=None):
    """
    Función para mostrar la información de una mascota de forma organizada
    """
    if numero:
        print(f"\n--- Mascota #{numero} ---")
    else:
        print("\n" + "-"*40)
    
    print(f"Nombre:     {mascota['nombre']}")
    print(f"Tipo:       {mascota['tipo']}")
    print(f"Edad:       {mascota['edad']}")
    print(f"Color:      {mascota['color']}")
    print(f"Raza:       {mascota['raza']}")
    print(f"Dueño:      {mascota['dueno']}")
    print("-"*40)


def buscar_mascota_por_nombre(nombre_buscado):
    """
    Función para buscar una mascota por su nombre
    """
    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_buscado.lower():
            print("\n" + "="*50)
            print("MASCOTA ENCONTRADA")
            print("="*50)
            mostrar_mascota_individual(mascota)
            return True
    
    print(f"\n✗ No se encontró una mascota con el nombre '{nombre_buscado}'")
    return False


def eliminar_mascota(nombre_eliminar):
    """
    Función para eliminar una mascota por su nombre
    """
    for i, mascota in enumerate(mascotas):
        if mascota['nombre'].lower() == nombre_eliminar.lower():
            nombre_mascota = mascotas[i]['nombre']
            mascotas.pop(i)
            print(f"\n✓ Mascota '{nombre_mascota}' eliminada exitosamente!")
            return True
    
    print(f"\n✗ No se encontró una mascota con el nombre '{nombre_eliminar}'")
    return False


def contar_mascotas():
    """
    Función para contar el total de mascotas registradas
    """
    return len(mascotas)


def menu_principal():
    """
    Función para mostrar el menú principal y gestionar la navegación
    """
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE REGISTRO DE MASCOTAS")
        print("="*50)
        print("1. Registrar nueva mascota")
        print("2. Mostrar todas las mascotas")
        print("3. Buscar mascota por nombre")
        print("4. Eliminar mascota")
        print("5. Ver total de mascotas registradas")
        print("6. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            mostrar_todas_mascotas()
        elif opcion == "3":
            nombre = input("Ingrese el nombre de la mascota a buscar: ").strip()
            buscar_mascota_por_nombre(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre de la mascota a eliminar: ").strip()
            eliminar_mascota(nombre)
        elif opcion == "5":
            total = contar_mascotas()
            print(f"\n✓ Total de mascotas registradas: {total}")
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema! ¡Hasta luego!")
            break
        else:
            print("\n✗ Opción no válida. Por favor, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()

