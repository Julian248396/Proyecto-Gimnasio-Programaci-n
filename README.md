# Sistema de Gestión de Usuarios — PowerZone Gym
PowerZone Gym es un sistema de gestión de usuarios para un gimnasio, desarrollado en Python. Permite registrar clientes, consultar información, actualizar datos, generar estadísticas y ver la información general del sitio, todo desde la consola.

![image alt](https://github.com/Julian248396/Proyecto-Gimnasio-Programaci-n/blob/0edd889756a6b02b2deed4211de342ca01e8593d/menu%20gym.PNG)
---

## Requisitos

- Python 3.10 o superior (se utiliza `match` / `case`)

---

## Cómo ejecutar

```bash
python Sistema_de_gestion_PowerZone_Gym.py
```

Al ejecutar, se abrirá el menú principal desde el cual se accede a todos los módulos.

---

## Módulos del sistema

### 1. Registrar Usuario
Solicita los datos de un nuevo cliente (cédula, nombre, edad, teléfono, membresía y mensualidad) y lo agrega al sistema como usuario activo.

### 2. Ver Todos los Usuarios
Muestra todos los usuarios registrados con su cédula, nombre, edad, teléfono, membresía, mensualidad y estado (activo / inactivo).

### 3. Buscar Usuario
Busca a un cliente por su cédula y muestra toda su información. Si no existe, informa que no se encontró.

### 4. Actualizar Usuario
Permite modificar el teléfono, el plan de membresía, el precio de la mensualidad o el estado (activo / inactivo) de un usuario.

### 5. Eliminar Usuario
Elimina a un usuario del sistema tras pedir confirmación.

### 6. Ver Estadísticas
Calcula y muestra el total de usuarios registrados, cuántos están activos e inactivos, y el precio promedio de la mensualidad.

### 7. Información de Servicios del Gimnasio
Muestra los servicios que ofrece PowerZone Gym: zona de pesas, cardio rumba, spinning, crossfit, yoga y spa.

---

## Estructura de un Usuario

Los usuarios se guardan en un diccionario principal que usa la **cédula** como clave. El valor de cada cédula es otro diccionario con los siguientes datos:

| Campo         | Tipo   | Descripción                                    |
|---------------|--------|------------------------------------------------|
| `nombre`      | `str`  | Nombre completo del cliente                    |
| `edad`        | `int`  | Edad del cliente                               |
| `telefono`    | `str`  | Número de teléfono de contacto                 |
| `membresia`   | `str`  | Tipo de plan (Básica / Premium / VIP)          |
| `mensualidad` | `int`  | Valor de la mensualidad                        |
| `activo`      | `bool` | Estado del usuario (`True` activo, `False` inactivo) |

---

## Funciones del sistema

| Función                              | Tipo      | Descripción                                                  |
|--------------------------------------|-----------|--------------------------------------------------------------|
| `registrar_usuario()`                | CRUD      | Solicita los datos y agrega un nuevo usuario                 |
| `mostrar_usuarios()`                 | CRUD      | Lista todos los usuarios con sus datos                       |
| `buscar_usuario()`                   | CRUD      | Busca un usuario por cédula y muestra su información         |
| `actualizar_usuario()`               | CRUD      | Modifica teléfono, plan, precio o estado de un usuario       |
| `eliminar_usuario()`                 | CRUD      | Elimina un usuario con confirmación                          |
| `estadisticas_usuarios()`            | Principal | Calcula totales, activos, inactivos y precio promedio        |
| `informacion_servicios_gimnasio()`   | Principal | Muestra los servicios del gimnasio                           |
| `main()`                             | Entrada   | Inicializa los usuarios de ejemplo y lanza el menú principal |

---

## Planes de Membresía

| Plan     | Mensualidad de ejemplo |
|----------|------------------------|
| Básica   | $60.000                |
| Premium  | $90.000                |
| VIP      | $120.000               |

---

## Autores

Proyecto desarrollado para la asignatura de **Programación de Computadores**.
