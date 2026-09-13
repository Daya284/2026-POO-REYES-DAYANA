# Restaurante App - Interfaz Gráfica con Tkinter

## Descripción

**Restaurante App** es una aplicación de escritorio desarrollada con **Python** y **Tkinter** como parte de la Semana 13 de la asignatura **Programación Orientada a Objetos**. Representa la transición del proyecto desde una aplicación basada en consola hacia una aplicación con **interfaz gráfica de usuario (GUI)**.

Esta versión constituye la **base estructural y funcional** sobre la cual se continuarán incorporando las funcionalidades del restaurante de manera progresiva en las siguientes semanas.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          # Datos de productos del restaurante
│   └── usuarios.json           # Datos de usuarios del sistema
├── modelos/
│   ├── __init__.py             # Inicialización del paquete de modelos
│   ├── producto.py             # Modelo Producto (id, nombre, categoría, precio, cantidad)
│   └── usuario.py              # Modelo Usuario (id, nombre_usuario, contraseña, nombre_completo, rol)
├── servicios/
│   ├── __init__.py             # Inicialización del paquete de servicios
│   ├── archivo_servicio.py     # Lectura de archivos JSON
│   └── restaurante_servicio.py # Lógica del restaurante (validación, listados, consultas)
├── ui/
│   ├── __init__.py             # Inicialización del paquete de vistas
│   ├── login_view.py           # Vista de acceso (login)
│   └── main_view.py            # Vista principal del sistema
└── main.py                     # Punto de entrada de la aplicación
```

## Componentes

### Modelos
- **Producto**: Representa un producto del restaurante con atributos: `id`, `nombre`, `categoria`, `precio` y `cantidad`.
- **Usuario**: Representa un usuario del sistema con atributos: `id`, `nombre_usuario`, `contrasena`, `nombre_completo` y `rol`.

### Servicios
- **ArchivoServicio**: Se encarga de leer los datos locales almacenados en archivos JSON. Centraliza el acceso a datos para que las vistas no lean directamente los archivos.
- **RestauranteServicio**: Recibe los datos cargados, los convierte en objetos del modelo y proporciona operaciones para validar acceso, listar usuarios, listar productos y consultar cantidades.

### Vistas (UI)
- **LoginView**: Pantalla de acceso simulada con campos para usuario y contraseña, validación visual de campos vacíos y credenciales incorrectas.
- **MainView**: Panel principal del restaurante que permite visualizar productos y usuarios registrados. Incluye la opción de Ventas como funcionalidad pendiente.

### main.py
Crea una **única ventana principal** de Tkinter, prepara los servicios con los datos cargados, entrega las dependencias a las vistas y controla el cambio entre login y vista principal.

## Flujo de la Aplicación

```
Inicio de la aplicación
        ↓
main.py prepara Tkinter y los servicios
        ↓
LoginView (pantalla de acceso)
        ↓
Ingreso de usuario y contraseña
        ↓
RestauranteServicio valida el acceso
        ↓
MainView (interfaz principal)
        ↓
Productos registrados | Usuarios registrados | Ventas (pendiente)
        ↓
Cerrar sesión → regresa a LoginView
```

## Usuarios de Prueba

| Usuario    | Contraseña   | Rol            |
|------------|-------------|----------------|
| admin      | admin123    | Administrador  |
| cajero1    | cajero123   | Cajero         |
| mesero1    | mesero123   | Mesero         |
| cocinero1  | cocinero123 | Cocinero       |

## Cómo Ejecutar

1. Asegúrese de tener **Python 3** instalado en su sistema.
2. Tkinter viene incluido con la instalación estándar de Python.
3. Navegue hasta la carpeta del proyecto:
   ```bash
   cd restaurante_app
   ```
4. Ejecute el archivo principal:
   ```bash
   python main.py
   ```

## Funcionalidades Implementadas

- ✅ Pantalla de acceso con validación de credenciales
- ✅ Retroalimentación visual para campos vacíos y credenciales incorrectas
- ✅ Visualización de productos desde la interfaz gráfica
- ✅ Visualización de usuarios desde la interfaz gráfica
- ✅ Cierre de sesión con regreso al login (misma ventana)
- ✅ Separación de responsabilidades: modelos, servicios, vistas y punto de entrada

## Funcionalidades Pendientes

- 🔲 Módulo de Ventas (interfaz gráfica)
- 🔲 Formularios avanzados de gestión
- 🔲 Funcionalidades adicionales de la versión de consola

## Tecnologías Utilizadas

- **Python 3**
- **Tkinter** (interfaz gráfica)
- **JSON** (almacenamiento local de datos)

## Autor

Dayana Reyes - Programación Orientada a Objetos - Semana 13
