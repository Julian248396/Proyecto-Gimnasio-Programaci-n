"""
Sistema de Gestión de Usuarios - PowerZone Gym
Primer avance: esqueleto del programa usando listas, funciones,
condicionales y bucles.

Cada usuario se guarda como una sublista dentro de la lista principal,
con el siguiente orden de datos:
[cedula, nombre, edad, telefono, plan, precio, activo]

"""


def mostrar_menu():
    """
    Imprime en consola el menú principal con las opciones numeradas.

    Parámetros:
        Ninguno.

    Retorna:
        None.
    """
    print("\n" + "=" * 45)
    print("SISTEMA DE GESTIÓN - POWERZONE GYM".center(45))
    print("=" * 45)
    print("  1. Registrar usuario")
    print("  2. Ver todos los usuarios")
    print("  3. Buscar usuario")
    print("  4. Actualizar usuario")
    print("  5. Eliminar usuario")
    print("  6. Ver estadísticas")
    print("  7. Información del gimnasio")
    print("  8. Salir")
    print("=" * 45)


def registrar_usuario(usuarios_gimnasio):
    """
    Solicita al usuario los datos de un nuevo cliente del gimnasio
    y los agrega como una nueva sublista a la lista principal.

    Parámetros:
        usuarios_gimnasio (list): Lista principal con todos los usuarios.

    Retorna:
        None.
    """
    pass


def mostrar_usuarios(usuarios_gimnasio):
    """
    Muestra en consola todos los usuarios registrados con sus datos básicos.

    Parámetros:
        usuarios_gimnasio (list): Lista principal con todos los usuarios.

    Retorna:
        None.
    """
    
    pass


def buscar_usuario(usuarios_gimnasio):
    """
    Pide una cédula y busca al usuario correspondiente en la lista
    principal, mostrando toda su información si lo encuentra.

    Parámetros:
        usuarios_gimnasio (list): Lista principal con todos los usuarios.

    Retorna:
        None.
    """
    
    pass


def actualizar_usuario(usuarios_gimnasio):
    """
    Busca a un usuario por cédula y permite modificar su teléfono,
    plan, precio o estado (activo/inactivo).

    Parámetros:
        usuarios_gimnasio (list): Lista principal con todos los usuarios.

    Retorna:
        None.
    """

    pass


def eliminar_usuario(usuarios_gimnasio):
    """
    Busca a un usuario por cédula y, tras confirmación, lo elimina
    de la lista principal.

    Parámetros:
        usuarios_gimnasio (list): Lista principal con todos los usuarios.

    Retorna:
        None.
    """
    
    pass


def estadisticas_usuarios(usuarios_gimnasio):
    """
    Calcula y muestra estadísticas generales de los usuarios:
    total registrados, activos, inactivos y precio promedio de membresía.

    Parámetros:
        usuarios_gimnasio (list): Lista principal con todos los usuarios.

    Retorna:
        None.
    """
    
    pass


def informacion_gimnasio():
    """
    Muestra la información general del gimnasio: nombre, dirección,
    horario de atención y año de fundación.

    Parámetros:
        Ninguno.

    Retorna:
        None.
    """
    pass


def main():
    """
    Función principal del sistema. Inicializa la lista de usuarios
    con datos de ejemplo y lanza el menú principal en un bucle hasta
    que el usuario elija salir.

    Retorna:
        None.
    """
    usuarios_gimnasio = [
        ["1234567", "Carlos Pérez", 24, "3011234567", "Premium", 90000, True],
        ["7654321", "Laura Ramírez", 30, "3187654321", "Básica", 60000, True],
        ["1122334", "Andrés Torres", 27, "3159871234", "Premium", 90000, False],
    ]

    while True:
        mostrar_menu()
        opcion = input("  Seleccione: ")

        if opcion == "1":
            registrar_usuario(usuarios_gimnasio)
        elif opcion == "2":
            mostrar_usuarios(usuarios_gimnasio)
        elif opcion == "3":
            buscar_usuario(usuarios_gimnasio)
        elif opcion == "4":
            actualizar_usuario(usuarios_gimnasio)
        elif opcion == "5":
            eliminar_usuario(usuarios_gimnasio)
        elif opcion == "6":
            estadisticas_usuarios(usuarios_gimnasio)
        elif opcion == "7":
            informacion_gimnasio()
        elif opcion == "8":
            print("\n  ¡Hasta pronto! - PowerZone Gym\n")
            break
        else:
            print("  Opción inválida.")


if __name__ == "__main__":
    main()