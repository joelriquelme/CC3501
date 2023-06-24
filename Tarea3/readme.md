# Tarea 2 Joel Riquelme 20.499.444-7

# ¿Que hace mi tarea?

## Parte 1. (Realizada)

La base de mi tarea 3 es la tarea 2, tienen todos los elementos de la 2da entrega.

## Parte 2. (Realizada)

Hay tres modelos de iluminación diferencte, para cambiar entre cada uno se utiliza el input del usuario. Presionando las teclas Q, W o E se puede cambiar del modelo *Flat*, *Gouraud* o *Phong* correspondientemente.

## Parte 3. (Realizada)

Se puede cambiar de texturas a la mariposa con el input del usuario. Se puede cambiar entre 3 opciones con las teclas A, S, D. Puede que en primera instancia se vea que solo cambia el color pero hay una textura, solamente que por el tamaño de la mariposa no se aprecia de manera correcta, pero hay una imagen que le da esa textura.

## Parte EXTRA. (Realizada)

Como extra se creo un "sol" que se puede mover con el input del usuario, para moverlo es necesario apretar las flechas izquierda o derecha, se detectará cuando se preciona y cuando se deja de presionar. Con esto se quería emular hasta cierto punto un ciclo de dia y noche.

## Informacion extra:

Se transformaron los objetos de stl a obj para que tuvieran normales, para esto se utilizó un [esta aplicación web](https://products.aspose.app/3d/es/conversion/stl-to-obj).

De manera totalmente analoga a la tarea 2, se creo una lector de archivos obj. Esta funcion se encuentra en el archivo readerObj.py y readerObj2.py, ambas son iguales salvo por una pequeña diferencia.

Fuente del stl de la mariposa: https://www.printables.com/es/model/11126-butterfly

# Inputs funcionales:

## Camara:
Numeros del 1 al 5 (numeros normales, no del teclado numerico).

## Luz:

Q: Modelo Flat.

W: Modelo Gouraud.

E: Modelo Phong.

## Texturas de la mariposa:

A: Textura 1 (color principal rosado).

S: Textura 2 (color principal calipso).

D: Textura 3 (color principal rojo).

## Mov. del Sol:

Flecha Izquierda: Mover el sol en sentido anti horario.

Flecha Derecha: Mover el sol en sentido horario.


