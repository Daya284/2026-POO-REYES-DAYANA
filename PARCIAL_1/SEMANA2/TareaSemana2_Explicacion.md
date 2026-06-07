# Explicación detallada del programa `TareaSemana2.py`

Este documento explica paso a paso el archivo `TareaSemana2.py` y los conceptos básicos de la programación orientada a objetos (POO) usados en él.

## 1. ¿Qué es la programación orientada a objetos?

La programación orientada a objetos (POO) se basa en crear elementos del mundo real como objetos en el código. Cada objeto tiene:

- Atributos: datos que describen al objeto.
- Métodos: acciones que el objeto puede realizar.

En este programa, usamos una clase llamada `CuentaBancaria` para representar una cuenta de banco.

## 2. La clase `CuentaBancaria`

```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self.saldo = float(saldo)
```

- `class CuentaBancaria:` crea una nueva clase llamada `CuentaBancaria`.
- `def __init__(self, titular: str, saldo: float = 0.0):` define el constructor.
- El constructor se ejecuta cuando creas un objeto de la clase.
- `self` es una referencia al propio objeto.
- `titular` y `saldo` son los datos que guardará cada cuenta.
- `self.titular = titular` y `self.saldo = float(saldo)` almacenan esos datos dentro del objeto.

## 3. Métodos de la clase

### `depositar`

```python
    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.saldo += monto
```

- Este método permite añadir dinero a la cuenta.
- `monto` es la cantidad a depositar.
- Si el monto es 0 o negativo, se lanza un error con `ValueError`.
- `self.saldo += monto` actualiza el saldo de la cuenta.

### `retirar`

```python
    def retirar(self, monto: float) -> bool:
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.saldo:
            return False
        self.saldo -= monto
        return True
```

- Este método quita dinero de la cuenta.
- Si el monto es negativo o cero, también lanza un error.
- Si no hay suficiente saldo, devuelve `False`.
- Si hay saldo suficiente, resta el monto y devuelve `True`.

### `transferir`

```python
    def transferir(self, destino: 'CuentaBancaria', monto: float) -> bool:
        if self.retirar(monto):
            destino.depositar(monto)
            return True
        return False
```

- Permite enviar dinero de una cuenta a otra.
- `destino` es otra instancia de `CuentaBancaria`.
- Reusa el método `retirar` para sacar dinero de la cuenta origen.
- Si la retirada es exitosa, usa `depositar` en la cuenta de destino.

### `mostrar_saldo`

```python
    def mostrar_saldo(self) -> str:
        return f"Titular: {self.titular} | Saldo: S/.{self.saldo:.2f}"
```

- Devuelve una cadena legible con el nombre del titular y el saldo.
- El formato `S/.{self.saldo:.2f}` muestra el saldo con dos decimales.

### `__str__`

```python
    def __str__(self) -> str:
        return self.mostrar_saldo()
```

- `__str__` define cómo se muestra el objeto cuando se imprime con `print(objeto)`.
- Aquí usamos `mostrar_saldo` para que la salida sea clara.

## 4. Uso del programa

```python
if __name__ == "__main__":
    _ejemplo_uso()
```

- Esta línea indica que el código dentro de este bloque solo se ejecuta si el archivo se ejecuta directamente.
- Si el archivo se importa desde otro módulo, no se ejecutará automáticamente.

### Función `_ejemplo_uso`

```python
def _ejemplo_uso() -> None:
    c1 = CuentaBancaria("Ana Pérez", 100.0)
    c2 = CuentaBancaria("Luis Gómez", 50.0)

    print("Saldos iniciales:")
    print(c1)
    print(c2)

    print("\nDepósito de 75 en la cuenta de Ana.")
    c1.depositar(75)
    print(c1)

    print("\nRetiro de 30 de la cuenta de Luis.")
    success = c2.retirar(30)
    print("Retiro exitoso." if success else "Fondos insuficientes.")
    print(c2)

    print("\nTransferir 50 de Ana a Luis.")
    if c1.transferir(c2, 50):
        print("Transferencia realizada.")
    else:
        print("Transferencia fallida.")
    print(c1)
    print(c2)
```

- Crea dos cuentas con titulares y saldo inicial.
- Muestra los saldos iniciales.
- Realiza un depósito en la primera cuenta.
- Retira dinero de la segunda cuenta.
- Transfiere dinero de la primera cuenta a la segunda.
- Imprime el resultado de cada acción.

## 5. Conceptos clave de POO en este ejemplo

- Clase: `CuentaBancaria` es la definición o plantilla.
- Objeto: `c1` y `c2` son objetos creados a partir de esa clase.
- Atributos: `titular` y `saldo` describen cada cuenta.
- Métodos: `depositar`, `retirar`, `transferir`, `mostrar_saldo` son acciones que puede ejecutar la cuenta.
- Encapsulamiento: cada cuenta guarda su propio estado (`saldo`) y solo cambia mediante métodos.

## 6. ¿Por qué usar clases?

- Organiza mejor el código cuando trabajas con entidades del mundo real.
- Permite reutilizar comportamiento en diferentes objetos.
- Hace más fácil entender y mantener el programa.

## 7. Cómo ejecutar el programa

Desde la terminal, ubícate en la carpeta `SEMANA2` y corre:

```bash
python TareaSemana2.py
```

Esto mostrará en pantalla las operaciones realizadas y los saldos de cada cuenta.

---

Si quieres, puedo también crear una versión con otra clase como `Libro` o `Estudiante` para comparar ejemplos de POO.
