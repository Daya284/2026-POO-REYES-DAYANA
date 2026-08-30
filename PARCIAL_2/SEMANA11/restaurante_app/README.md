# Restaurante App — Semana 11

**Estudiante:** Reyes Dayana  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 11 — Fundamentos de colecciones aplicados a relaciones, ventas y persistencia JSON

---

## Descripción del sistema

`restaurante_app` es una aplicación de consola desarrollada en Python que permite gestionar productos, usuarios y ventas de un restaurante. Esta versión corresponde a la **Semana 11** y evoluciona el proyecto de la Semana 10 incorporando:

- **Control de stock** en los productos.
- **Persistencia JSON** completa para productos, usuarios y ventas.
- **Operación de venta** que relaciona un usuario con un producto, valida stock y registra la transacción.
- **Consulta de ventas** por usuario mediante recorrido y filtrado de colecciones.

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
│   └── restaurante.py        # Lógica de negocio y reglas del sistema
├── main.py                   # Punto de entrada y menú interactivo
└── README.md                 # Documentación del proyecto
```

---

## Responsabilidad de cada componente

| Archivo | Responsabilidad |
|---------|----------------|
| `modelos/producto.py` | Define la clase `Producto` con atributos validados (`codigo`, `nombre`, `categoria`, `precio`, `stock`), método `vender()` para decrementar stock y `a_diccionario()` para serialización JSON. |
| `modelos/usuario.py` | Define la clase `Usuario` con atributos validados (`identificacion`, `nombre`, `correo`) y `a_diccionario()` para serialización JSON. |
| `modelos/venta.py` | Define la clase `Venta` que relaciona un usuario con un producto vendido (`usuario_id`, `producto_codigo`, `cantidad`) y `a_diccionario()` para serialización JSON. |
| `servicios/restaurante.py` | Administra las colecciones de productos, usuarios y ventas. Implementa búsquedas, registros, la operación `vender_producto()` con validaciones completas, y `consultar_ventas_por_usuario()` con filtrado de colecciones. |
| `servicios/archivo_servicio.py` | Centraliza la lectura y escritura de los tres archivos JSON (`productos.json`, `usuarios.json`, `ventas.json`) con manejo de excepciones específicas. |
| `main.py` | Coordina la interacción por consola mediante un menú de 12 opciones. Solicita datos al usuario y delega la lógica al servicio `Restaurante`. No modifica directamente las colecciones internas. |

---

## Funcionamiento del stock

Cada producto tiene un atributo `stock` que representa la cantidad disponible:

- Al **registrar** un producto se solicita el stock inicial.
- Al **actualizar** un producto se puede modificar el stock.
- Al **vender** un producto, el sistema valida que haya stock suficiente y lo decrementa.
- El stock **nunca puede ser negativo** (se valida tanto en el setter como en el método `vender()`).

### Ejemplo de venta:

```
Antes de vender:
  Producto: Hamburguesa | Stock: 10
  Cantidad solicitada: 2

Después de vender:
  Producto: Hamburguesa | Stock: 8
  Venta registrada correctamente
```

---

## Relación Usuario–Producto mediante Venta

La clase `Venta` representa la relación entre un usuario y un producto:

```
Usuario registrado → Producto existente → Validar cantidad → Validar stock
    → Crear Venta → Agregar a colección → Disminuir stock
    → Guardar ventas.json y productos.json
```

### Validaciones de `vender_producto()`:

1. El usuario debe existir en el sistema.
2. El producto debe existir en el sistema.
3. La cantidad debe ser mayor a cero.
4. El stock disponible debe ser suficiente.

---

## Persistencia JSON

Las tres colecciones se persisten automáticamente después de cada operación que las modifique:

| Operación | Archivos actualizados |
|-----------|----------------------|
| Registrar/Actualizar/Eliminar producto | `productos.json` |
| Registrar usuario | `usuarios.json` |
| Realizar una venta | `ventas.json` + `productos.json` |

### Flujo de persistencia:

```
OBJETOS → a_diccionario() → lista de diccionarios → json.dump() → archivo JSON
archivo JSON → json.load() → diccionarios → reconstrucción de objetos
```

Al iniciar la aplicación, las tres colecciones se recuperan automáticamente desde sus archivos JSON correspondientes.

---

## Excepciones controladas

| Excepción | Uso |
|-----------|-----|
| `FileNotFoundError` | Si un archivo JSON no existe, se inicia con colección vacía. |
| `json.JSONDecodeError` | Si el contenido JSON es inválido, se inicia con colección vacía. |
| `PermissionError` | Si no hay permisos de lectura/escritura sobre los archivos. |
| `KeyError` | Si un registro JSON no contiene una clave esperada. |
| `ValueError` | Para validaciones de datos en Producto, Usuario y Venta. |

No se utiliza `except: pass` ni capturas genéricas.

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

1. **Ejecutar** `main.py` — el sistema inicia correctamente y carga datos existentes.
2. **Registrar un usuario** — se guarda en `usuarios.json`.
3. **Registrar un producto con stock** — se guarda en `productos.json` con el stock indicado.
4. **Realizar una venta válida** — el stock disminuye, la venta se registra en `ventas.json` y el stock actualizado se guarda en `productos.json`.
5. **Consultar ventas de un usuario** — muestra correctamente las ventas filtradas.
6. **Cerrar y reiniciar el programa** — los productos, usuarios y ventas se recuperan desde los archivos JSON.
7. **Intentar vender con stock insuficiente** — la operación es rechazada sin alterar datos.
8. **Intentar vender con cantidad inválida (0 o negativa)** — la operación es rechazada.
9. **Intentar vender con usuario inexistente** — la operación es rechazada.
10. **Intentar vender con producto inexistente** — la operación es rechazada.

---

## Mejoras de la Semana 11 respecto a la Semana 10

- Se agregó el atributo `stock` a `Producto` con validación de no negatividad.
- Se implementó el método `vender()` en `Producto` para decrementar stock de forma segura.
- Se creó la clase `Venta` como nueva entidad del dominio.
- Se agregó `a_diccionario()` a `Usuario` para persistencia JSON.
- Se amplió `ArchivoServicio` para cargar y guardar las tres colecciones.
- Se implementó `vender_producto()` en `Restaurante` con validación completa.
- Se implementó `consultar_ventas_por_usuario()` con recorrido y filtrado de colecciones.
- Se actualizó `main.py` con nuevas opciones de menú (venta, consulta de ventas, listado de ventas).
- Se agregó persistencia de usuarios al registrarlos.
- Las tres colecciones se recuperan al iniciar la aplicación.
