# 🍽️ Restaurante App - Semana 14: Componentes y Contenedores

## Propósito

La Semana 14 de Programación Orientada a Objetos aborda el tema **Componentes y Contenedores**. A partir de la base gráfica construida en la Semana 13, se evoluciona la interfaz de `restaurante_app` mediante el uso adecuado de componentes, contenedores y gestores de geometría de Tkinter, manteniendo la arquitectura modular, la persistencia en archivos JSON y la separación de responsabilidades.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          # Datos persistentes de productos
│   └── usuarios.json           # Datos de usuarios del sistema
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Modelo Producto (con método a_diccionario)
│   └── usuario.py              # Modelo Usuario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Lectura y escritura de archivos JSON
│   └── restaurante_servicio.py # Lógica de negocio y operaciones CRUD
├── ui/
│   ├── __init__.py
│   ├── login_view.py           # Vista de inicio de sesión
│   └── main_view.py            # Vista principal con formularios y tablas
└── main.py                     # Punto de entrada de la aplicación
```

## Componentes y Contenedores Utilizados

### Contenedores
| Contenedor | Uso en la aplicación |
|---|---|
| `tk.Frame` | Barra superior, panel de navegación, área de contenido, contenedor de acciones |
| `tk.LabelFrame` | Formulario de datos del producto, tabla de productos registrados, tabla de usuarios |

### Componentes
| Componente | Uso en la aplicación |
|---|---|
| `tk.Label` | Títulos, etiquetas de campos, mensajes de estado, información del usuario |
| `tk.Entry` | Campos de texto para ID, nombre y precio del producto |
| `tk.Button` | Navegación entre secciones, acciones CRUD (Registrar, Consultar, Actualizar, Eliminar, Limpiar), cerrar sesión |
| `tk.Spinbox` | Selección numérica de la cantidad de producto |
| `ttk.Combobox` | Selección de categoría del producto con opciones predefinidas |
| `ttk.Treeview` | Tabla para visualizar productos y usuarios registrados |
| `ttk.Scrollbar` | Desplazamiento vertical en las tablas |
| `ttk.Style` | Personalización visual de la tabla Treeview |

### Gestores de Geometría
| Gestor | Uso en la aplicación |
|---|---|
| `pack()` | Disposición vertical de contenedores principales, barra superior, botones de navegación |
| `grid()` | Organización del formulario de productos en filas y columnas |
| `place()` | Centrado del contenedor de login |

## Mejoras Realizadas respecto a la Semana 13

1. **Formulario de productos**: Se incorporó un formulario organizado con `LabelFrame` y `grid()` que permite capturar los datos de un producto (ID, nombre, categoría, precio, cantidad).
2. **Botones CRUD con `command=`**: Se agregaron botones para Registrar, Consultar, Actualizar, Eliminar y Limpiar, todos conectados mediante `command=` a métodos de la vista.
3. **Componentes especializados**: Se utilizan `ttk.Combobox` para categorías y `tk.Spinbox` para la cantidad, mejorando la experiencia del usuario.
4. **Tabla estilizada**: La tabla `Treeview` se personalizó con `ttk.Style` para una apariencia más coherente con el diseño oscuro de la aplicación.
5. **Persistencia de escritura**: `ArchivoServicio` ahora incluye el método `escribir_json()` para guardar los cambios en `productos.json`.
6. **Servicio CRUD completo**: `RestauranteServicio` incorpora los métodos `registrar_producto()`, `buscar_producto_por_id()`, `actualizar_producto()` y `eliminar_producto()` con validaciones de negocio centralizadas.
7. **Modelo con serialización**: `Producto` incluye el método `a_diccionario()` para convertir el objeto a diccionario, facilitando la persistencia en JSON.
8. **Barra de estado**: Se agregó retroalimentación visual en la parte inferior de la sección de productos para informar al usuario del resultado de cada operación.
9. **Navegación mejorada**: Se agregó un botón de Inicio para regresar a la pantalla de bienvenida.

## Operaciones Implementadas sobre Productos

| Operación | Descripción |
|---|---|
| **Registrar** | Crea un nuevo producto con ID automático. Valida nombre, categoría, precio y cantidad. |
| **Consultar** | Busca un producto por ID y carga sus datos en el formulario para visualización. |
| **Actualizar** | Modifica los datos de un producto existente identificado por su ID. |
| **Eliminar** | Elimina un producto del sistema con confirmación previa. |
| **Limpiar** | Limpia todos los campos del formulario. |

## Persistencia

Los productos se almacenan en `datos/productos.json`. Cada operación de registro, actualización o eliminación persiste automáticamente los cambios en el archivo JSON a través del servicio correspondiente (`ArchivoServicio.escribir_json()`). Los datos se conservan al cerrar y volver a ejecutar la aplicación.

## Flujo Funcional

```
Inicio de la aplicación (main.py)
        ↓
LoginView → Validación mediante RestauranteServicio
        ↓
MainView → Navegación por secciones
        ↓
├── Inicio: Resumen de datos
├── Usuarios: Consulta en tabla
└── Productos: Formulario + Acciones CRUD + Tabla
        ↓
RestauranteServicio procesa la operación
        ↓
Persistencia en productos.json
        ↓
Actualización automática de la interfaz
```

## Cómo Ejecutar

1. Asegúrese de tener **Python 3.x** instalado con soporte para Tkinter.
2. Navegue hasta el directorio `restaurante_app/`.
3. Ejecute el archivo principal:
   ```bash
   python main.py
   ```
4. Inicie sesión con alguno de los usuarios de prueba:
   - `admin` / `admin123`
   - `cajero1` / `cajero123`
   - `mesero1` / `mesero123`
   - `cocinero1` / `cocinero123`

## Autora

**Dayana Reyes** - Programación Orientada a Objetos 2026
