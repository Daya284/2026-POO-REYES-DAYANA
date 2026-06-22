# Sistema de Gestión de Restaurante

## Descripción

Sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). Demuestra la organización de un proyecto en módulos, separación de responsabilidades e integración de archivos mediante importaciones.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante
├── main.py                  # Punto de entrada del programa
└── README.md                # Documentación del proyecto
```

## Descripción de Clases

### Clase `Producto` (modelos/producto.py)

Representa un producto disponible en el menú del restaurante.

**Atributos:**

- `nombre`: nombre del producto
- `precio`: precio del producto
- `tipo`: categoría (plato, bebida, postre)
- `descripcion`: descripción adicional del producto

**Métodos principales:**

- `__init__()`: constructor de la clase
- `obtener_informacion()`: retorna información del producto
- `aplicar_descuento(porcentaje)`: aplica un descuento al precio
- `__str__()`: representación en texto del producto

### Clase `Cliente` (modelos/cliente.py)

Representa a un cliente del restaurante.

**Atributos:**

- `nombre`: nombre del cliente
- `correo`: correo electrónico
- `telefono`: número telefónico
- `pedidos_realizados`: contador de pedidos realizados

**Métodos principales:**

- `__init__()`: constructor de la clase
- `registrar_pedido()`: incrementa el contador de pedidos
- `obtener_informacion()`: retorna información completa del cliente
- `__str__()`: representación en texto del cliente

### Clase `Restaurante` (servicios/restaurante.py)

Gestiona todos los productos y clientes del restaurante.

**Atributos:**

- `nombre`: nombre del restaurante
- `ubicacion`: ubicación física del restaurante
- `productos`: lista de productos disponibles
- `clientes`: lista de clientes registrados

**Métodos principales:**

- `__init__()`: constructor de la clase
- `registrar_producto(producto)`: agrega un producto al menú
- `registrar_cliente(cliente)`: registra un nuevo cliente
- `mostrar_menu()`: muestra todos los productos organizados por tipo
- `mostrar_clientes_registrados()`: muestra información de todos los clientes
- `registrar_pedido_cliente(nombre)`: registra un pedido para un cliente
- `obtener_estadisticas()`: retorna estadísticas del restaurante
- `__str__()`: representación en texto del restaurante

## Funcionalidades Principales

✓ Crear y registrar productos en el menú  
✓ Registrar clientes en el sistema  
✓ Realizar seguimiento de pedidos por cliente  
✓ Ver menú organizado por categorías  
✓ Consultar información de clientes  
✓ Obtener estadísticas del restaurante  
✓ Aplicar descuentos a productos

## Cómo Ejecutar el Programa

1. Navega a la carpeta del proyecto:

   ```bash
   cd restaurante_app
   ```

2. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

## Requisitos Cumplidos

- ✓ Estructura de carpetas obligatoria creada
- ✓ Dos clases en modelos/ (Producto y Cliente)
- ✓ Una clase en servicios/ (Restaurante)
- ✓ Constructores **init**() en todas las clases
- ✓ Atributos pertinentes en cada clase
- ✓ Métodos para gestionar la información
- ✓ Método especial **str**() en las clases
- ✓ Importaciones correctas entre archivos
- ✓ Objetos creados y utilizados desde main.py
- ✓ Agregación de objetos al servicio principal
- ✓ Información mostrada de forma organizada
- ✓ Comentarios explicativos en el código

## Notas de Diseño

Este sistema demuestra:

- **Separación de responsabilidades**: cada clase tiene una responsabilidad clara
- **Modularidad**: el código está organizado en módulos independientes
- **Reutilización**: las clases pueden ser utilizadas en diferentes contextos
- **Encapsulación**: los datos se agrupan con los métodos que los manipulan
- **Importaciones**: uso correcto de importaciones entre módulos
