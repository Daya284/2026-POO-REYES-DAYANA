# 🍽️ Restaurante App - Semana 15

## Conceptos fundamentales de manejo de eventos

**Asignatura:** Programación Orientada a Objetos  
**Semana:** 15  
**Tema:** Conceptos fundamentales de manejo de eventos  
**Estudiante:** Dayana Reyes

---

## 📋 Propósito de la Semana 15

La presente actividad aborda los **conceptos fundamentales de manejo de eventos** en una aplicación gráfica con Tkinter. Se utiliza una operación de **venta** como contexto práctico para demostrar cómo una acción del usuario (clic en un botón) inicia una respuesta coordinada en la aplicación.

El objetivo central es comprender el flujo:

```
USUARIO (acción)
    ↓
BOTÓN (command=)
    ↓
CALLBACK (_callback_registrar_venta)
    ↓
RestauranteServicio (validar y registrar)
    ↓
PERSISTENCIA (ventas.json)
    ↓
RESPUESTA VISUAL (tabla actualizada + mensaje)
```

## 🔄 Evolución desde la Semana 14

El proyecto **restaurante_app** continúa su evolución progresiva:

- **Semana 14:** Se implementaron componentes y contenedores de Tkinter, operaciones CRUD sobre productos con `Entry`, `Combobox`, `Spinbox`, botones con `command=`, `Treeview` y persistencia en `productos.json`.
- **Semana 15:** Se incorpora la **sección de Ventas** para registrar operaciones que relacionan un usuario con un producto. Se añade el modelo `Venta`, la persistencia en `ventas.json`, el uso de `command=` con un callback que delega la lógica al servicio, y el uso obligatorio de la carpeta `assets/` con íconos y logotipo del sistema.

Se conservan todas las funcionalidades anteriores: inicio de sesión, navegación, gestión de productos y consulta de usuarios.

## 📁 Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          # Datos de productos del restaurante
│   ├── usuarios.json           # Datos de usuarios del sistema
│   └── ventas.json             # Registro de ventas (Semana 15)
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Modelo Producto
│   ├── usuario.py              # Modelo Usuario
│   └── venta.py                # Modelo Venta (Semana 15)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Lectura/escritura de archivos JSON
│   └── restaurante_servicio.py # Lógica de negocio y validaciones
├── ui/
│   ├── __init__.py
│   ├── login_view.py           # Vista de inicio de sesión
│   └── main_view.py            # Vista principal con secciones
├── assets/
│   ├── logo.png                # Logotipo del sistema
│   ├── icono_productos.png     # Ícono para el botón Productos
│   ├── icono_usuarios.png      # Ícono para el botón Usuarios
│   ├── icono_ventas.png        # Ícono para el botón Ventas
│   ├── icono_inicio.png        # Ícono para el botón Inicio
│   └── icono_cerrar_sesion.png # Ícono para el botón Cerrar Sesión
├── main.py                     # Punto de entrada de la aplicación
└── README.md
```

## 🧾 Gestión de Ventas (Semana 15)

### Modelo Venta

La clase `Venta` representa una relación sencilla entre un **usuario** y un **producto**, con los siguientes atributos:

- `id`: Identificador único de la venta (generado automáticamente).
- `id_usuario`: ID del usuario que realiza la compra.
- `nombre_usuario`: Nombre completo del usuario.
- `id_producto`: ID del producto vendido.
- `nombre_producto`: Nombre del producto.
- `precio_producto`: Precio del producto al momento de la venta.
- `fecha`: Fecha y hora del registro (generada automáticamente).

### Flujo de registro de venta

1. El usuario navega a la sección **🧾 Ventas**.
2. Selecciona un **usuario** del Combobox (datos cargados desde el servicio).
3. Selecciona un **producto** del Combobox (datos cargados desde el servicio).
4. Presiona el botón **🛒 Registrar Venta**.
5. El botón tiene `command=self._callback_registrar_venta` (sin paréntesis).
6. El **callback** obtiene las selecciones de la interfaz.
7. El callback **delega** la operación a `RestauranteServicio.registrar_venta()`.
8. El servicio **valida** que el usuario y producto existan, y que haya stock.
9. El servicio **registra** la venta y la **persiste** en `ventas.json`.
10. La **tabla de ventas** se actualiza inmediatamente.
11. Se muestra un **mensaje** al usuario confirmando el resultado.

### Uso de `command=` y callbacks

```python
# En main_view.py - El botón usa command= para asociar el callback
tk.Button(
    frame_boton_venta,
    text="🛒 Registrar Venta",
    command=self._callback_registrar_venta  # SIN paréntesis
).pack(...)
```

El callback `_callback_registrar_venta` coordina la interacción pero **no contiene la lógica de negocio**. Toda la validación y persistencia se realiza dentro de `RestauranteServicio`.

### Persistencia en `ventas.json`

Las ventas se almacenan automáticamente en `datos/ventas.json` a través de `ArchivoServicio.escribir_json()`. Al cerrar y volver a abrir la aplicación, las ventas registradas se recuperan correctamente.

## 🖼️ Carpeta `assets/`

Se utiliza la carpeta `assets/` de manera obligatoria para integrar:

- **`logo.png`**: Logotipo del sistema, mostrado en la pantalla de login y en la barra superior de la vista principal.
- **`icono_productos.png`**: Ícono del botón de navegación a Productos.
- **`icono_usuarios.png`**: Ícono del botón de navegación a Usuarios.
- **`icono_ventas.png`**: Ícono del botón de navegación a Ventas.
- **`icono_inicio.png`**: Ícono del botón de navegación a Inicio.
- **`icono_cerrar_sesion.png`**: Ícono del botón de Cerrar Sesión.
- El ícono de la ventana se carga desde `assets/logo.png`.

Todos los íconos se cargan dinámicamente mediante `tk.PhotoImage` y se integran en los botones usando la propiedad `compound="left"` para mostrar imagen + texto.

## 🚀 Pasos para ejecutar la aplicación

1. Asegúrese de tener **Python 3.x** instalado.
2. Abra una terminal en la carpeta `restaurante_app/`.
3. Ejecute:

```bash
python main.py
```

4. Inicie sesión con uno de los usuarios de prueba:

| Usuario    | Contraseña   | Rol           |
|------------|-------------|---------------|
| admin      | admin123    | Administrador |
| cajero1    | cajero123   | Cajero        |
| mesero1    | mesero123   | Mesero        |
| cocinero1  | cocinero123 | Cocinero      |

5. Navegue por las secciones: **Productos**, **Usuarios**, **Ventas** e **Inicio**.
6. En la sección de **Ventas**, seleccione un usuario y un producto, y presione **Registrar Venta**.

## ✅ Comprobación de funcionamiento

- [x] La aplicación inicia sin errores con `python main.py`.
- [x] El inicio de sesión y la navegación existente continúan funcionando.
- [x] Las secciones de Usuarios y Productos mantienen las funciones previas.
- [x] Existe una sección visible de Ventas con formulario y tabla.
- [x] Se puede seleccionar un usuario y un producto registrados.
- [x] El botón "Registrar Venta" utiliza `command=` para ejecutar el callback.
- [x] El callback delega el registro a `RestauranteServicio`.
- [x] La nueva venta se almacena en `ventas.json`.
- [x] La venta aparece en la tabla Treeview inmediatamente.
- [x] Al cerrar y reabrir, las ventas registradas se recuperan correctamente.
- [x] No existen referencias a "libros" o "biblioteca".
- [x] La interfaz mantiene una apariencia clara, consistente y estilizada.
- [x] Se utilizan íconos y logotipo desde la carpeta `assets/`.
