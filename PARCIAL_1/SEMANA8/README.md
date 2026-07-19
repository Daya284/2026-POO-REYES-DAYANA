# Tarea Semana 8 — Principios SOLID en un Proyecto Python Modular

## Información del estudiante

| Campo              | Detalle                |
| ------------------ | ---------------------- |
| **Nombre completo** | Dayana Kristel Reyes Feijoo       |
| **Asignatura**      | Programación Orientada a Objetos |
| **Semana**          | 8                     |

---

## Descripción del sistema

**restaurante_app** es un sistema de gestión básica para un restaurante que permite registrar y listar productos, bebidas y clientes mediante un menú interactivo por consola. El proyecto fue desarrollado aplicando los principios SOLID (SRP, OCP y LSP) para demostrar cómo un diseño orientado a objetos bien organizado facilita la extensión y el mantenimiento del software.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase base Producto
│   ├── bebida.py         # Clase hija Bebida (hereda de Producto)
│   └── cliente.py        # Clase Cliente (independiente)
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    # Clase de servicio Restaurante
└── main.py               # Punto de arranque y menú interactivo
```

---

## Responsabilidad de cada clase

| Clase          | Archivo                    | Responsabilidad                                                                 |
| -------------- | -------------------------- | ------------------------------------------------------------------------------- |
| `Producto`     | `modelos/producto.py`      | Representar los datos comunes de un producto: código, nombre, categoría y precio. |
| `Bebida`       | `modelos/bebida.py`        | Especializar a `Producto` añadiendo atributos propios: tamaño y tipo de envase.  |
| `Cliente`      | `modelos/cliente.py`       | Representar la información de un cliente: identificación, nombre y correo.       |
| `Restaurante`  | `servicios/restaurante.py` | Administrar las colecciones de productos y clientes (registro, validación, listado). |
| `main.py`      | `main.py`                  | Coordinar la interacción por consola y delegar las operaciones al servicio.       |

---

## Relación entre Producto y Bebida

`Bebida` es una **clase hija** de `Producto` porque una bebida **es un tipo de producto** del restaurante. Esta relación se implementa mediante herencia:

- `Bebida` hereda los atributos `codigo`, `nombre`, `categoria` y `precio` de `Producto`.
- `Bebida` agrega atributos específicos: `tamanio` y `tipo_envase`.
- `Bebida` **sobrescribe** el método `mostrar_informacion()` para incluir su información adicional, reutilizando la implementación base con `super()`.

Ambas clases se almacenan en una **misma lista de productos** dentro del servicio `Restaurante`, sin necesidad de crear listas separadas.

---

## Principios SOLID aplicados

### S — Responsabilidad Única (SRP)

Cada clase tiene una única responsabilidad bien definida:

- **Producto** y **Bebida** → representar productos.
- **Cliente** → representar un cliente.
- **Restaurante** → administrar las colecciones y operaciones del sistema.
- **main.py** → coordinar la interacción por consola.

La lógica de gestión no se encuentra en `main.py`, y la interacción por consola no se encuentra en el servicio.

### O — Abierto/Cerrado (OCP)

El sistema fue **ampliado** al incorporar la clase `Bebida` sin necesidad de modificar:

- La clase `Producto` (se mantiene intacta).
- La clase `Restaurante` (acepta cualquier subclase de `Producto` gracias al polimorfismo).
- El método `listar_productos()` (invoca `mostrar_informacion()` sin distinguir tipos).

Si en el futuro se necesita agregar otra especialización (por ejemplo, `Postre`), bastará con crear una nueva clase hija de `Producto` sin tocar el servicio.

### L — Sustitución de Liskov (LSP)

Un objeto `Bebida` puede utilizarse en cualquier lugar donde se espere un `Producto`:

- Se almacena en la misma lista de productos.
- El método `mostrar_informacion()` se invoca de forma polimórfica.
- No se utilizan condicionales (`isinstance`, `type()`) para distinguir tipos durante el listado.
- No se genera ningún error ni se altera el comportamiento esperado.

---

## Instrucciones de ejecución

1. Abra una terminal en la carpeta `SEMANA8`.
2. Ejecute el siguiente comando:

```bash
python -m restaurante_app.main
```

O bien, navegue a la carpeta `restaurante_app` y ejecute:

```bash
cd restaurante_app
python main.py
```

3. Siga las opciones del menú interactivo:

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Salir
========================================
```

---

## Reflexión

Diseñar proyectos aplicando los principios SOLID permite que el código sea **mantenible**, **extensible** y **comprensible**. Al separar las responsabilidades entre clases y archivos, cada componente puede evolucionar de forma independiente sin afectar al resto del sistema. La herencia bien aplicada (como en Producto → Bebida) facilita la reutilización de código y el polimorfismo garantiza que nuevas especializaciones se integren sin esfuerzo. Un proyecto organizado desde el inicio reduce significativamente el costo de incorporar cambios futuros y disminuye la probabilidad de introducir errores al modificar funcionalidades existentes.
