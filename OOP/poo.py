class Robot:
    # Poner un constructor en python
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo

    def saludar(self) -> str:
        return f"Hola mi nombre es {self.nombre} y soy una IA"

    def truco(slef) -> str:
        return "Estoy haciendo el paso del robot"

robotin = Robot("Robotin", "Humanoide")

print(robotin.nombre)
print(robotin.tipo)
print(robotin.saludar())
print(robotin.truco())