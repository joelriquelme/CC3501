import numpy as np
import sys
import os.path

def readObj2(filename):
    vertices = []
    normales = []
    vertices_normales = []
    indices = []

    i = 0
    with open(filename, 'r') as file:
        line = file.readline().strip()
        a = True
        while not "polygons" in line:
            line = file.readline().strip()
            aux = line.split(' ')

            if aux[0] == 'v':
                vertices.append(aux[1])
                vertices.append(aux[2])
                vertices.append(aux[3])

                indices.append(i)

                i += 1
            if aux[0] == 'vn':
                normales.append(aux[1])
                normales.append(aux[2])
                normales.append(aux[3])
        for i in range(0,len(vertices)):
            vertices_normales.append(vertices[i])
            if (i%3 == 2):
                vertices_normales.append(0)
                vertices_normales.append(1)
                vertices_normales.append(normales[3*(i//9)])
                vertices_normales.append(normales[3*(i//9) + 1])
                vertices_normales.append(normales[3*(i//9) + 1]) 

    return vertices_normales,indices