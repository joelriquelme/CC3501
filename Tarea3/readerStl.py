import numpy as np
import sys
import os.path

def readStl(filename, r=0.0, g=0.0, b=0.0):
    vertices = []
    indices = []

    i = 0
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line != "endsolid":
            line = file.readline().strip()
            aux = line.split(' ')
            if aux[0] == 'vertex':
                vertices.append(aux[1])
                vertices.append(aux[2])
                vertices.append(aux[3])
                vertices.append(r)
                vertices.append(g)
                vertices.append(b)

                indices.append(i)

                i += 1
    
    return vertices,indices


