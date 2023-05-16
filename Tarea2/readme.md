Tarea 2 Joel Riquelme 20.499.444-7

Que hace mi tarea?

Parte 1. (Realizada) 
Utilice de base la mariposa de la tarea 1 y le di un 3ra dimension dandole un ancho diferente segun fue necesario para cada seccion de las alas utilizando grafos de escena como fue pedido en el enunciado.

Parte 2. (Realizada)

Para mover la mariposa se utilizaron los grafos de escena para diferenciar el movimiento de la mariposa en total y el movimiento de las alas.

Parte 3. (Realizada)

Se utilizo la modalidad de camara fija que apunta hacia la mariposa, para cambiar de camara se utlizan los numeros (no los del teclado numerico). Existen 4 camaras diferentes:

Cam 1: Plano general.
Cam 2: Plano lateral.
Cam 3: Plano general desde más abajo.
Cam 4: Plano cenital.

Parte 4. (Realizada)

Para generar un ambiente se modelaron arboles basicos uniendo un cubo deformado y una piramide de base cuadrada. Para cear el bosque se reutilizó ese modelo instanciandolo varias veces con diferentes tamaños y posiciones.

Parte 5. (Realizada)

Se importó un modelo de tipo .stl en formato ASCII. El formato de los archivos stl ASCII viene de la sgte forma:

solid name
facet normal ni nj nk
    outer loop
        vertex v1x v1y v1z
        vertex v2x v2y v2z
        vertex v3x v3y v3z
    endloop
endfacet
endsolid name

El problema inicial fue que el modelo encontrado de la mariposa estaba en binario, por lo que tuve que buscar un script para transformalo a ASCII, dentro de la carpeta butterfly esta el archivo script.py con el que transforme de binario a ASCII.
Dicho script lo saqué de la siguiente fuente: https://github.com/IsseiMori/binary-stl-toASCII
El script no agrega el ensolid final, por lo que tuve que modificar el archivo de forma manual (no quería modificar un script que ya funcionaba).

Luego de obtener el stl en ASCII, cree una funcion llamada readerStl en readStl.py:

a readStl( filename, r, g, b):

se le entrega un nombre de archivo y el rgb en %, es decir de 0 a 1.

Se crean listas para los vertices e indices.

Luego se abre el archivo en modo lectura, y se lee linea por linea hasta llegar al endsolid del final del archivo.

Para cada linea se hace un split por los espacios, y se comprueba si el primer elemento de la lista creada coinscide con el nombre 'vertex'. Si este es el caso, se le añaden a la lista vertices los elementos 1, 2 y 3 de la linea además de el rgb indicado al llamar a la función. Finalmente se le agrega el indice i de la iteración a la lista de indices. Quedando las listas para cada loop de la siguiente forma:

vertices == [v1x, v1y, v1z, r, g, b
             v2x, v2y, v2z, r, g, b
             v3x, v3y, v3z, r, g, b   
                                    ]
indices == [0,1,2]

Por ultimo se retorna la lista de vertices e indices.

Cabe aclarar que en cada loop se siguen agregando elementos a la misma lista de vertices e indices, siendo esto un poco ineficiente ya que se repiten un monton de puntos e indices. Siendo esto no una limitación ya que los archivos a importar no son de gran tamaño.

Fuente del stl de la maripos: https://www.printables.com/es/model/11126-butterfly

Parte EXTRA. (Realizada)

Para el extra se creo una nueva camara:

Camara 5: Camara SUS

esta ultima camara se invoca presionando la tecla 5, que muestra el "detras de escena". Aqui se puede apreciar un AMONGUS gigante de color rojo importado en formato stl (ya procesado para que esté en formato ASCII).

Para esto se creo un nuevo grafo de escena para el modelo y una nueva camara que apunta al AMONGUS, tambien se tuvo que detectar el caso de presionar la tecla 5 para hacer el cambio de camara.



