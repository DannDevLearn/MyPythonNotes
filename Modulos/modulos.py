# Tenemos un archivo matematica con la funcion suma asi que lo importamos
import matematicas # de esta manera importamos todo el modulo

print(matematicas.suma(7, 9))

# si queremos imnportar coas especificas, en este caso information tiene dos funciones
# pero solo queremos impotar la informacion del clima
from informatio import weather

print(weather())

# solo para importar el contenido de todo el modulo 
from songs import *

print(country())
print(rock())

'''
Cuando se crean paquetes completos se ve algo asi

proyecto/
│
├── main.py
└── operaciones/
    ├── __init__.py
    ├── matematicas.py
    └── estadisticas.py

y se mandan a llamar en el main.py

from operaciones.matematicas import suma
from operaciones.estadisticas import promedio

print(suma(5, 5))  
print(promedio([1, 2]))  
'''