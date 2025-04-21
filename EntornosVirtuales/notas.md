## Crando un entorno virual

Un entorno virtual nos es util para cuando queremos separar o aislar las dependencias
de un proyecto y no queremos instalarlas en nuestra computadora.

Para poder crear un entrono vitual en Python podemos usar venv y aqui te explico como hacerlo.

1- Crear la carpeta del proyecto y nacagar hasta ella en la consola.

2- Estando en la terminal y posicionados en la ubicacion de la carpeta del proyecto corremos el
siquiente comando:

'''
(para Linux/MacOs)
python3 -m venv nombre_del_entorno

(Para windows)
python - venv nombre_del_entorno
'''

3- Ahora debemos activar el entorno

'''
Para Linux/Mac
    source nombre_del_entorno/bin/activate

Para windows
    nombre_del_entorno\Scripts\activate
'''

en la terminal veras algo como 

(nombre_del_entorno) usuario@equipo:~$

En caso de no verlo probablemente sea el tema que estes utilizando pero puedes verificarlo con 

'''
echo $VIRTUAL_ENV
'''

4- Para desactivar el entorno solo usa

'''
deactivate
'''