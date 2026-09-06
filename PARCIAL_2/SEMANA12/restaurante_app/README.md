# Restaurante App — Semana 12

**Estudiante:** Reyes Dayana  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 12 — Utilización de colecciones para la mejora de rendimiento

---

## Descripción del sistema

`restaurante_app` es una aplicación de consola desarrollada en Python que permite gestionar productos, usuarios y ventas de un restaurante. Esta versión corresponde a la **Semana 12** y evoluciona el proyecto de la Semana 11 incorporando **mejoras internas de rendimiento** mediante el uso de colecciones auxiliares (`dict` y `set`) que reducen recorridos innecesarios en búsquedas, consultas y validaciones.

No se agregaron funcionalidades nuevas ni entidades adicionales. El enfoque de esta semana es exclusivamente **optimizar la forma en que el programa localiza, consulta y valida información**.

---

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json       # Persistencia de productos con stock
│   ├── usuarios.json        # Persistencia de usuarios registrados
│   └── ventas.json          # Persistencia de ventas realizadas
├── modelos/
│   ├── __init__.py           # Paquete de modelos
│   ├── producto.py           # Clase Producto con stock y validaciones
│   ├── usuario.py            # Clase Usuario con validaciones
│   └── venta.py              # Clase Venta (relación Usuario-Producto)
├── servicios/
│   ├── __init__.py           # Paquete de servicios
│   ├── archivo_servicio.py   # Lectura/escritura JSON de las 3 colecciones
│   └── restaurante.py        # Lógica de negocio con índices auxiliares
├── main.py                   # Punto de entrada y menú interactivo
└── README.md                 # Documentación del proyecto
```

---

## Mejoras de rendimiento implementadas en la Semana 12

### 1. Índice de productos por código (`dict`)

| Aspecto | Semana 11 | Semana 12 |
|---------|-----------|-----------|
| Estructura | Solo `list[Producto]` | `list[Producto]` + `dict[str, Producto]` |
| Búsqueda por código | Recorrido lineal O(n) con `for` | Acceso directo O(1) con `dict.get()` |
| Validación de existencia | Recorrido lineal O(n) | O(1) con `set` auxiliar |

**Atributo:** `_indice_productos: dict[str, Producto]`  
**Métodos mejorados:** `buscar_producto()`, `registrar_producto()`, `eliminar_producto()`, `actualizar_producto()`

### 2. Índice de usuarios por identificación (`dict`)

| Aspecto | Semana 11 | Semana 12 |
|---------|-----------|-----------|
| Estructura | Solo `list[Usuario]` | `list[Usuario]` + `dict[str, Usuario]` |
| Búsqueda por identificación | Recorrido lineal O(n) con `for` | Acceso directo O(1) con `dict.get()` |

**Atributo:** `_indice_usuarios: dict[str, Usuario]`  
**Métodos mejorados:** `buscar_usuario()`, `registrar_usuario()`

### 3. Ventas agrupadas por usuario (`dict` de listas)

| Aspecto | Semana 11 | Semana 12 |
|---------|-----------|-----------|
| Estructura | Solo `list[Venta]` | `list[Venta]` + `dict[str, list[Venta]]` |
| Consulta por usuario | Recorrido lineal O(n) de todas las ventas | Acceso directo O(1) a la lista del usuario |

**Atributo:** `_ventas_por_usuario: dict[str, list[Venta]]`  
**Método mejorado:** `consultar_ventas_por_usuario()`

### 4. Set de códigos de producto (`set`)

| Aspecto | Semana 11 | Semana 12 |
|---------|-----------|-----------|
| Validación de código existente | Búsqueda lineal O(n) mediante `buscar_producto()` | Verificación O(1) con operador `in` sobre `set` |

**Atributo:** `_codigos_productos: set[str]`  
**Método mejorado:** `registrar_producto()`

---

## Colecciones utilizadas y su justificación

| Colección | Tipo | Propósito |
|-----------|------|-----------|
| `_productos` | `list` | Almacenar, recorrer, listar y persistir productos. Se conserva como colección principal. |
| `_usuarios` | `list` | Almacenar, recorrer, listar y persistir usuarios. Se conserva como colección principal. |
| `_ventas` | `list` | Almacenar, recorrer, listar y persistir ventas. Se conserva como colección principal. |
| `_indice_productos` | `dict` | Índice auxiliar para búsqueda de productos por código en O(1). |
| `_indice_usuarios` | `dict` | Índice auxiliar para búsqueda de usuarios por identificación en O(1). |
| `_ventas_por_usuario` | `dict` | Índice auxiliar para consulta de ventas agrupadas por usuario en O(1). |
| `_codigos_productos` | `set` | Validación rápida de pertenencia de códigos de producto en O(1). |

---

## Sincronización de estructuras auxiliares

Las estructuras auxiliares se mantienen coherentes con las listas principales en todo momento:

| Operación | Estructuras actualizadas |
|-----------|--------------------------|
| Registrar producto | `_productos` (lista) + `_indice_productos` (dict) + `_codigos_productos` (set) |
| Eliminar producto | `_productos` (lista) + `_indice_productos` (dict) + `_codigos_productos` (set) |
| Actualizar producto | El objeto se modifica en su lugar; lista e índice apuntan al mismo objeto |
| Registrar usuario | `_usuarios` (lista) + `_indice_usuarios` (dict) |
| Registrar venta | `_ventas` (lista) + `_ventas_por_usuario` (dict) |
| Cargar desde JSON | Se reconstruyen todos los índices mediante métodos `_reconstruir_indice_*()` |

---

## Reconstrucción de índices al iniciar

Al ejecutar la aplicación, después de cargar los datos desde los archivos JSON, los índices se reconstruyen automáticamente:

```
cargar_productos_iniciales(productos) → _reconstruir_indice_productos()
cargar_usuarios_iniciales(usuarios)   → _reconstruir_indice_usuarios()
cargar_ventas_iniciales(ventas)       → _reconstruir_indice_ventas()
```

Esto garantiza que los índices sean coherentes con los datos recuperados del almacenamiento persistente.

---

## Forma de ejecución

```bash
cd restaurante_app
python main.py
```

---

## Menú del sistema

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
----------------------------------------
6. Registrar usuario
7. Listar usuarios
----------------------------------------
8. Vender producto
9. Consultar ventas de un usuario
10. Listar todas las ventas
----------------------------------------
11. Mostrar categorías
12. Salir
========================================
```

---

## Pruebas realizadas

1. **Ejecutar** `main.py` — el sistema inicia correctamente, carga datos existentes y reconstruye los índices auxiliares.
2. **Registrar un producto** — se guarda en `productos.json` y se actualiza el índice y el set.
3. **Buscar un producto por código** — la búsqueda es inmediata mediante el índice (O(1)).
4. **Registrar un usuario** — se guarda en `usuarios.json` y se actualiza el índice.
5. **Buscar un usuario por identificación** — la búsqueda es inmediata mediante el índice (O(1)).
6. **Realizar una venta válida** — el stock disminuye, la venta se registra y el índice de ventas por usuario se actualiza.
7. **Consultar ventas de un usuario** — las ventas se obtienen directamente del índice agrupado (O(1)).
8. **Eliminar un producto** — se elimina de la lista, del índice y del set.
9. **Actualizar un producto** — el objeto se modifica en su lugar, lista e índice permanecen sincronizados.
10. **Cerrar y reiniciar el programa** — los datos JSON se recuperan y los índices se reconstruyen correctamente.
11. **Verificar coherencia** — después de registrar, eliminar o vender, los índices reflejan los datos actuales.

---

## Qué NO se modificó

- Los modelos (`Producto`, `Usuario`, `Venta`) permanecen idénticos a la Semana 11.
- El servicio `ArchivoServicio` permanece idéntico.
- El archivo `main.py` conserva la misma estructura y funcionalidades.
- No se agregaron nuevas funcionalidades, entidades ni interfaces.
- Las listas principales no fueron reemplazadas por diccionarios.
