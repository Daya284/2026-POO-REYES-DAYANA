class Estudiante:
    def __init__(self, nombre, edad, carrera, promedio):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.promedio = promedio

    def mostrar_informacion(self):
        print("Informacion del estudiante")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Promedio: {self.promedio}")

    def estudiar(self, materia):
        print(f"{self.nombre} esta estudiando {materia}.")

    def actualizar_promedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio
        print(f"El nuevo promedio de {self.nombre} es {self.promedio}.")


estudiante_1 = Estudiante("Dayana Reyes", 20, "Programacion", 9.2)

estudiante_1.mostrar_informacion()
estudiante_1.estudiar("Programacion Orientada a Objetos")
estudiante_1.actualizar_promedio(9.5)
