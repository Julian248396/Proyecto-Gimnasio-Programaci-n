"""
Sistema de Gestión de Usuarios - PowerZone Gym
Primer avance: esqueleto del programa usando diccionarios, funciones,
condicionales y bucles.

Cada usuario se guarda en un diccionario principal, usando la cédula
como clave. El valor de cada cédula es otro diccionario con los datos:
{"nombre", "edad", "telefono", "membresia", "mensualidad", "activo"}

"""


def registrar_usuario(usuarios_gimnasio):
    """
    Solicita al usuario los datos de un nuevo cliente del gimnasio
    y los agrega como un nuevo diccionario al diccionario principal.

    Parámetros:
        usuarios_gimnasio (dict): Diccionario principal con todos los usuarios.

    Retorna:
        None.
    """
    cedula = input("  Cédula: ")
    nombre = input("  Nombre: ")
    edad = int(input("  Edad: "))
    telefono = input("  Teléfono: ")
    membresia = input("  Membresía (Básica / Premium / VIP): ")
    mensualidad = int(input("  Mensualidad: "))

    usuarios_gimnasio[cedula] = {
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
        "membresia": membresia,
        "mensualidad": mensualidad,
        "activo": True
    }

    print("  Usuario registrado correctamente.")


def mostrar_usuarios(usuarios_gimnasio):
    """
    Muestra en consola todos los usuarios registrados con sus datos básicos.

    Parámetros:
        usuarios_gimnasio (dict): Diccionario principal con todos los usuarios.

    Retorna:
        None.
    """
    for cedula in usuarios_gimnasio:
        usuario = usuarios_gimnasio[cedula]
        print("  Cédula:", cedula)
        print("  Nombre:", usuario["nombre"])
        print("  Edad:", usuario["edad"])
        print("  Teléfono:", usuario["telefono"])
        print("  Membresía:", usuario["membresia"])
        print("  Mensualidad:", usuario["mensualidad"])
        print("  Activo:", usuario["activo"])


def buscar_usuario(usuarios_gimnasio):
    """
    Pide una cédula y busca al usuario correspondiente en el diccionario
    principal, mostrando toda su información si lo encuentra.

    Parámetros:
        usuarios_gimnasio (dict): Diccionario principal con todos los usuarios.

    Retorna:
        None.
    """
    cedula = input("  Cédula a buscar: ")

    if cedula in usuarios_gimnasio:
        usuario = usuarios_gimnasio[cedula]
        print("  Cédula:", cedula)
        print("  Nombre:", usuario["nombre"])
        print("  Edad:", usuario["edad"])
        print("  Teléfono:", usuario["telefono"])
        print("  Membresía:", usuario["membresia"])
        print("  Mensualidad:", usuario["mensualidad"])
        print("  Activo:", usuario["activo"])
    else:
        print("  No se encontró un usuario con esa cédula.")


def actualizar_usuario(usuarios_gimnasio):
    """
    Busca a un usuario por cédula y permite modificar su teléfono,
    plan, precio o estado (activo/inactivo).

    Parámetros:
        usuarios_gimnasio (dict): Diccionario principal con todos los usuarios.

    Retorna:
        None.
    """
    cedula = input("  Cédula del usuario a actualizar: ")

    if cedula in usuarios_gimnasio:
        print("  1. Teléfono")
        print("  2. Plan")
        print("  3. Precio")
        print("  4. Estado (activo/inactivo)")
        opcion = input("  ¿Qué desea modificar?: ")

        if opcion == "1":
            usuarios_gimnasio[cedula]["telefono"] = input("  Nuevo teléfono: ")
        elif opcion == "2":
            usuarios_gimnasio[cedula]["membresia"] = input("  Nuevo plan: ")
        elif opcion == "3":
            usuarios_gimnasio[cedula]["mensualidad"] = int(input("  Nuevo precio: "))
        elif opcion == "4":
            usuarios_gimnasio[cedula]["activo"] = not usuarios_gimnasio[cedula]["activo"]
        print("  Usuario actualizado.")
    else:
        print("  No se encontró un usuario con esa cédula.")


def eliminar_usuario(usuarios_gimnasio):
    """
    Busca a un usuario por cédula y, tras confirmación, lo elimina
    del diccionario principal.

    Parámetros:
        usuarios_gimnasio (dict): Diccionario principal con todos los usuarios.

    Retorna:
        None.
    """
    cedula = input("  Cédula del usuario a eliminar: ")

    if cedula in usuarios_gimnasio:
        confirmacion = input("  ¿Seguro que desea eliminarlo? (s/n): ")
        if confirmacion == "s":
            del usuarios_gimnasio[cedula]
            print("  Usuario eliminado.")
        else:
            print("  No se eliminó el usuario.")
    else:
        print("  No se encontró un usuario con esa cédula.")


def estadisticas_usuarios(usuarios_gimnasio):
    """
    Calcula y muestra estadísticas generales de los usuarios:
    total registrados, activos, inactivos y precio promedio de membresía.

    Parámetros:
        usuarios_gimnasio (dict): Diccionario principal con todos los usuarios.

    Retorna:
        None.
    """
    total = 0
    activos = 0
    inactivos = 0
    suma_precios = 0

    for cedula in usuarios_gimnasio:
        usuario = usuarios_gimnasio[cedula]
        total = total + 1
        suma_precios = suma_precios + usuario["mensualidad"]
        if usuario["activo"]:
            activos = activos + 1
        else:
            inactivos = inactivos + 1

    promedio = suma_precios / total

    print("  Total registrados:", total)
    print("  Activos:", activos)
    print("  Inactivos:", inactivos)
    print("  Precio promedio:", promedio)


def informacion_servicios_gimnasio():
    """
    Muestra la información de servicios del gimnasio: spa, cardio rumba, etc...

    Parámetros:
        Ninguno.

    Retorna:
        None.
    """
    print("  Servicios de PowerZone Gym:")
    print("  - Zona de pesas")
    print("  - Cardio rumba")
    print("  - Spinning")
    print("  - Crossfit")
    print("  - Yoga")
    print("  - Spa")


def main():
    """
    Función principal del sistema. Inicializa el diccionario de usuarios
    con datos de ejemplo y lanza el menú principal en un bucle hasta
    que el usuario elija salir.

    Retorna:
        None.
    """
    usuarios_gimnasio = {
        "1234567": {
            "nombre": "Carlos Pérez",
            "edad": 24,
            "telefono": "3011234567",
            "membresia": "Premium",
            "mensualidad": 90000,
            "activo": True
        },
        "7654321": {
            "nombre": "Laura Ramírez",
            "edad": 30,
            "telefono": "3187654321",
            "membresia": "Básica",
            "mensualidad": 60000,
            "activo": True
        },
        "1122334": {
            "nombre": "Andrés Torres",
            "edad": 27,
            "telefono": "3159871234",
            "membresia": "Premium",
            "mensualidad": 90000,
            "activo": False
        },
        "9988776": {
            "nombre": "Mariana Gómez",
            "edad": 22,
            "telefono": "3104567890",
            "membresia": "VIP",
            "mensualidad": 120000,
            "activo": True
        },
        "5544332": {
            "nombre": "Diego Martínez",
            "edad": 35,
            "telefono": "3206549871",
            "membresia": "Básica",
            "mensualidad": 60000,
            "activo": True
        },
        "3344556": {
            "nombre": "Sofia Castro",
            "edad": 29,
            "telefono": "3023456789",
            "membresia": "Premium",
            "mensualidad": 90000,
            "activo": False
        },
        "8877665": {
            "nombre": "Camilo Morales",
            "edad": 40,
            "telefono": "3178901234",
            "membresia": "VIP",
            "mensualidad": 120000,
            "activo": True
        },
        "4433221": {
            "nombre": "Valentina Rojas",
            "edad": 26,
            "telefono": "3167894512",
            "membresia": "Básica",
            "mensualidad": 60000,
            "activo": True
        }
    }

    while True:
        print("\n" + "=" * 45)
        print("SISTEMA DE GESTIÓN - POWERZONE GYM".center(45))
        print("=" * 45)
        print("  1. Registrar usuario")
        print("  2. Ver todos los usuarios")
        print("  3. Buscar usuario")
        print("  4. Actualizar usuario")
        print("  5. Eliminar usuario")
        print("  6. Ver estadísticas")
        print("  7. Información de servicios del gimnasio")
        print("  8. Salir")
        print("=" * 45)
        opcion = input("  Seleccione: ")
        
        match opcion:
            case "1":
                registrar_usuario(usuarios_gimnasio)
            case "2":
                mostrar_usuarios(usuarios_gimnasio)
            case "3":
                buscar_usuario(usuarios_gimnasio)
            case "4":
                actualizar_usuario(usuarios_gimnasio)
            case "5":
                eliminar_usuario(usuarios_gimnasio)
            case "6":
                estadisticas_usuarios(usuarios_gimnasio)
            case "7":
                informacion_servicios_gimnasio()
            case "8":
                print("Fin del programa.")
                break
            case _:
                print("OpciÃ³n no vÃ¡lida.")



if __name__ == "__main__":
    main()
