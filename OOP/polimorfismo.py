class Animal:

    def hablar(self) -> str:
        return "Este animal hace un sonido"
    
    def otra_cosa(self) -> None:
        print("Este metodo es de la clase padre Animal")

class Perro(Animal):
    
    # override
    def hablar(self)-> str:
        return "El perro hace Woof!"
    
    

class Gato(Animal):

    #override
    def hablar(self)-> str:
        return "El gato hace Miau!"
    
    def ronrronear(self) -> None:
        print("El gato esta ronrroneado")
# Aqui esta un funcion que hace uso de polimorfismo

def hacer_hablar(animal: Animal) -> None:
    print(animal.hablar())

pelusin: Animal = Gato()
makita: Animal = Perro()

print(pelusin.hablar())
pelusin.otra_cosa()
pelusin.ronrronear()

hacer_hablar(makita)
makita.otra_cosa()

'''
Duck Typing ("Si camina como un pato y grazna como un pato, entonces es un pato")
Python sigue el principio de duck typing , que significa que el tipo o la clase de un objeto 
es menos importante que los métodos o atributos que posee. Si un objeto tiene los métodos o 
atributos necesarios, se puede usar en un contexto específico, independientemente de su tipo.

Tenemos las siguientes Avion y Duck; ambos implementan un metodo llamado volar()
'''

class Duck:
    def volar(self) -> str:
        return "El pato esta volando"
    
class Avion:
    def volar(self) -> str:
        return "El avion esta volando"
    

pato = Duck()
avion = Avion()

# Aqui tenemos una funcion que recibe cualquier tipo de objeto siempre y cuando
# tenga un metodo volar

def hacer_volar(objeto)-> None:
    print(objeto.volar())


hacer_volar(pato)
hacer_volar(avion)

# Tenemos funciones polimorficas que sin importar el objeto te manda el resultado

texto = "Hello, World!!"
arr = [1,2,3,4,5,6,7,8,9,0]
mapa = {"a": 1, "b": 2}

print(len(texto))
print(len(arr))
print(len(mapa))

