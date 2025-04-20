'''
En python podemos definicar clases abstractas pero a diferencia de Java debemos de importar
una dependencia donde nos ayudar indicar que son clases abstractas, metodos abstractos
asi como metodos de clase.
'''
from abc import ABC, abstractmethod

# pasamos la importacion ABC para indicar que es una  clase abstracta
class Animal(ABC):
    
    total_animals = 0

    def __init__(self, name):
        self.name = name
        Animal.total_animals += 1

    # para declarar un metodo abstracto
    # por medio de esta linea de codigo nos obliga a sobreescribir el metodo en nuestras clases hijas
    @abstractmethod
    def make_sound(self) -> str:
        pass
    
    # ahora definimos un metodo de clase
    # asi como self hace referencia a la instancia de la clase
    # cls hace referencia en general a la Clase
    # para asimilarlo es un pooco parecido al static en Java
    @classmethod
    def get_total_animals(cls) -> int:
        return cls.total_animals
    
# Ahora solo queda crear las clases hijas

class Cat(Animal):

    # override
    def make_sound(self):
        return "El gatito hace Miau Miau!"
    

class Dog(Animal):

    # override
    def make_sound(self):
        return "El perrito hace Woof Woof!"
    
pisosin = Cat("pisosin")
chio = Dog("Chio")

print(pisosin.make_sound())
print(chio.make_sound())

print(f"El total de las instancias de la clase Animal son: {Animal.get_total_animals()}")