# coding=utf-8

from readerStl import *
import os.path
import sys
import numpy as np
import pyglet
from OpenGL.GL import *
from readerObj import *
from readerObj2 import *

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.scene_graph as sg
import grafica.easy_shaders as es
import grafica.lighting_shaders as ls
from grafica.assets_path import getAssetPath

LIGHT_FLAT    = 0
LIGHT_GOURAUD = 1
LIGHT_PHONG   = 2

viewPos = np.array([10,-10,5])


class Controller(pyglet.window.Window):

    def __init__(self, width, height, title="Tarea 3 Joel Riquelme"):
        super().__init__(width, height, title)
        self.total_time = 0.0
        self.fillPolygon = True
        self.showAxis = True
        self.pipeline = None
        self.repeats = 0
        self.camara = tr.lookAt(
            viewPos,
            np.array([0,0,0]),
            np.array([0,0,1])
        )
        self.lightingModel = LIGHT_FLAT
        self.moving_direction = 0
        self.light_theta = 0
        self.inputTexture = "rosa-bebe.jpg"
    
        

# Se asigna el ancho y alto de la ventana y se crea.
WIDTH, HEIGHT = 1280, 800
controller = Controller(width=WIDTH, height=HEIGHT)
# Se asigna el color de fondo de la ventana
glClearColor(0, 0.67, 0.894, 1.0)

# Como trabajamos en 3D, necesitamos chequear cuáles objetos están en frente, y cuáles detrás.
glEnable(GL_DEPTH_TEST)

# Different shader programs for different lighting strategies
textureFlatPipeline = ls.SimpleTextureFlatShaderProgram()
textureGouraudPipeline = ls.SimpleTextureGouraudShaderProgram()
texturePhongPipeline = ls.SimpleTexturePhongShaderProgram()

# This shader program does not consider lighting
colorPipeline = es.SimpleModelViewProjectionShaderProgram()

# Convenience function to ease initialization
def createGPUShape(pipeline, shape):
    gpuShape = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuShape)
    gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
    return gpuShape

# Creating shapes on GPU memory
gpuAxis = createGPUShape(colorPipeline, bs.createAxis(4))



# El controlador puede recibir inputs del usuario. Estas funciones define cómo manejarlos.
@controller.event
def on_key_press(symbol, camara):

    if symbol == pyglet.window.key.SPACE:
        controller.fillPolygon = not controller.fillPolygon

    elif symbol == pyglet.window.key.LCTRL:
        controller.showAxis = not controller.showAxis

    elif symbol == pyglet.window.key.ESCAPE:
        controller.close()

    elif symbol == pyglet.window.key._1:
        viewPos = np.array([10,-10,5])
        controller.camara = tr.lookAt(
            viewPos,
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key._2:
        viewPos = np.array([10,0,5])
        controller.camara = tr.lookAt(
            viewPos,
            np.array([0,0,0]),
            np.array([0,0,1])
        )
        

    elif symbol == pyglet.window.key._3:
        viewPos = np.array([10, -10,0])
        controller.camara = tr.lookAt(
            viewPos,
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key._4:
        viewPos = np.array([0, 1,30])
        controller.camara = tr.lookAt(
            viewPos,
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key._5:
        viewPos = np.array([-10,10, 7])
        controller.camara = tr.lookAt(
            viewPos,
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key.Q:
        controller.lightingModel = LIGHT_FLAT

    elif symbol == pyglet.window.key.W:
        controller.lightingModel = LIGHT_GOURAUD

    elif symbol == pyglet.window.key.E:
        controller.lightingModel = LIGHT_PHONG

    elif symbol == pyglet.window.key.LEFT:
        controller.moving_direction = -1.0

    elif symbol == pyglet.window.key.RIGHT:
        controller.moving_direction = +1.0

    elif symbol == pyglet.window.key.A:
        controller.inputTexture = "rosa-bebe.jpg"

    elif symbol == pyglet.window.key.S:
        controller.inputTexture = "calipso.jpg"
    
    elif symbol == pyglet.window.key.D:
        controller.inputTexture = "texture_red.jpg"

    else:
        print('Unknown key')


@controller.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        controller.moving_direction -= -1.0
    elif symbol == pyglet.window.key.RIGHT:
        controller.moving_direction += -1.0

def createMariposa(pipeline,texture):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    
    #Setting de left half of de body
    black_body1_vertices = [
    # x   y  z  r    g    b
    (2/WIDTH) *0,   -0.025, (2/HEIGHT)*200,  0.0, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-30, -0.015,  (2/HEIGHT)*180, 0.0, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-8, -0.01,(2/HEIGHT)*20,  0.0, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *0, -0.01, (2/HEIGHT)*0,  0.0, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *0,   0.025, (2/HEIGHT)*200,  0.0, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-30, 0.015,  (2/HEIGHT)*180, 0.0, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-8, 0.01,(2/HEIGHT)*20,  0.0, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *0, 0.01, (2/HEIGHT)*0,  0.0, 0.0, 0.0, 0.0, 0.0,
    ]
    body1_vertices = [
    0, 1, 2,
    0, 2, 3,
    4, 5, 6,
    4, 6, 7,
    0, 4, 1,
    4, 1, 5,
    1, 5, 2,
    5, 2, 6,
    2, 6, 3,
    6, 2, 7,
    7, 6, 3,
    ]
    body1 = bs.Shape(black_body1_vertices,body1_vertices)
    gpuBlackbody = createGPUShape(body1)
    gpuBlackbody.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)


    #Setting de right half of the body
    gray_body2_vertices = [
    # x   y  z  r    g    b
    (2/WIDTH) *0, -0.025,  (2/HEIGHT)*200,   0.25, 0.25, 0.25, 0.0, 0.0,
    (2/WIDTH) *30, -0.015, (2/HEIGHT)*180,  0.25, 0.25, 0.25, 0.0, 0.0,
    (2/WIDTH) *8, -0.01, (2/HEIGHT)*20,  0.25, 0.25, 0.25, 0.0, 0.0,
    (2/WIDTH) *0, -0.01, (2/HEIGHT)*0,  0.25, 0.25, 0.25, 0.0, 0.0,
    (2/WIDTH) *0, 0.025,  (2/HEIGHT)*200,   0.35, 0.35, 0.35, 0.0, 0.0,
    (2/WIDTH) *30, 0.015, (2/HEIGHT)*180,  0.35, 0.35, 0.35, 0.0, 0.0,
    (2/WIDTH) *8, 0.01, (2/HEIGHT)*20,  0.35, 0.35, 0.35, 0.0, 0.0,
    (2/WIDTH) *0, 0.01, (2/HEIGHT)*0,  0.35, 0.35, 0.35, 0.0, 0.0,
    ]
    body2_vertices = [
    0, 1, 2,
    0, 2, 3,
    4, 5, 6,
    4, 6, 7,
    0, 4, 1,
    4, 1, 5,
    1, 5, 2,
    5, 2, 6,
    2, 6, 3,
    6, 2, 7,
    7, 6, 3,
    ]
    body2 = bs.Shape(gray_body2_vertices,body2_vertices)
    gpuGraybody = createGPUShape(body2)
    gpuGraybody.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)


    #Setting the wing 1
    red_wing1_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-22, -0.01,  (2/HEIGHT)*194, 0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-15, -0.01, (2/HEIGHT)*120, 0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-200, -0.05, (2/HEIGHT)*220, 0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-160, -0.03, (2/HEIGHT)*240, 0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-108, -0.03, (2/HEIGHT)*232, 0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-22, 0.01,  (2/HEIGHT)*194, 0.85, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01, (2/HEIGHT)*120, 0.85, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-200, 0.05, (2/HEIGHT)*220, 0.85, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-160, 0.03, (2/HEIGHT)*240, 0.85, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-108, 0.03, (2/HEIGHT)*232, 0.85, 0.0, 0.0, 0.0, 0.0,
    ]   
    wing1_vertices = [
    0, 1, 2,
    0, 2, 3,
    0, 3, 4,
    5, 6, 7,
    5, 7, 8,
    5, 8, 9,
    0, 5, 4,
    5, 4, 9,
    9, 8, 4,
    4, 3, 8,
    8, 7, 2,
    2, 3, 8,
    ]
    wing1 = bs.Shape(red_wing1_vertices,wing1_vertices)
    gpuRedwing1 = createGPUShape(wing1)
    gpuRedwing1.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)


    #Setting the wing 2
    red_wing2_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-15, -0.01,  (2/HEIGHT)*120,   0.5, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-200, -0.05, (2/HEIGHT)*220,  0.5, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-180, -0.01, (2/HEIGHT)*120,  0.5, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01,  (2/HEIGHT)*120,   0.6, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-200, 0.05, (2/HEIGHT)*220,  0.6, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-180, 0.01, (2/HEIGHT)*120,  0.6, 0.0, 0.0, 0.0, 0.0,   
    ]
    wing2_vertices = [
    0, 1, 2,
    3, 4, 5,
    1, 4, 2,
    4, 5, 2,
    5, 3, 2,
    0, 2, 3,
    ]
    wing2 = bs.Shape(red_wing2_vertices,wing2_vertices)
    gpuRedwing2 = createGPUShape(wing2)
    gpuRedwing2.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)


    #Setting the wing 3
    red_wing3_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-15, -0.01,  (2/HEIGHT)*120,  0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-140, -0.01, (2/HEIGHT)*120,  0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-170, -0.01, (2/HEIGHT)*80, 0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-150, -0.05, (2/HEIGHT)*20, 0.70, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01,  (2/HEIGHT)*120,  0.85, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-140, 0.01, (2/HEIGHT)*120,  0.85, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-170, 0.01, (2/HEIGHT)*80, 0.85, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-150, 0.05, (2/HEIGHT)*20, 0.85, 0.0, 0.0, 0.0, 0.0,
    ]
    wing3_vertices = [
    0, 1, 2,
    0, 2, 3,
    4, 5, 6,
    4, 6, 7,
    5, 6, 1,
    1, 2, 6,
    6, 7, 2,
    2, 3, 7,
    ]
    wing3 = bs.Shape(red_wing3_vertices,wing3_vertices)
    gpuRedwing3 = createGPUShape(wing3)
    gpuRedwing3.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)


    #Setting the left wing 4
    red_wing4_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-15, -0.01, (2/HEIGHT)* 120, 0.5, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-60, -0.01, (2/HEIGHT)*0, 0.5, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-110, -0.03, (2/HEIGHT)*-20, 0.5, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-150, -0.05, (2/HEIGHT)*20, 0.5, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01, (2/HEIGHT)* 120, 0.6, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-60, 0.01, (2/HEIGHT)*0, 0.6, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-110, 0.03, (2/HEIGHT)*-20, 0.6, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *-150, 0.05, (2/HEIGHT)*20, 0.6, 0.0, 0.0, 0.0, 0.0,

    ]
    wing4_vertices = [
    0, 1, 2,
    0, 2, 3,
    4, 5, 6,
    4, 6, 7,
    0, 1, 4,
    4, 5, 1,
    1, 2, 5,
    5, 6, 2,
    2, 3, 6,
    6, 7, 3, 
    ]
    wing4 = bs.Shape(red_wing4_vertices,wing4_vertices)
    gpuRedwing4 = createGPUShape(wing4)
    gpuRedwing4.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)



    ###########Grafos de escena##############

    #Body

    grayBody = sg.SceneGraphNode("grayBody")
    grayBody.childs += [gpuGraybody]

    blackBody = sg.SceneGraphNode("blackBody")
    blackBody.childs += [gpuBlackbody]

    body = sg.SceneGraphNode("body")
    body.transform = tr.scale(2, 3, 2)
    body.childs += [grayBody,blackBody]

    #Wings:

    #Right side:

    rredWing1 = sg.SceneGraphNode("rredWing1")
    rredWing1.childs += [gpuRedwing1]

    rredWing2 = sg.SceneGraphNode("rredWing2")
    rredWing2.childs += [gpuRedwing2]

    rredWing3 = sg.SceneGraphNode("rredWing3")
    rredWing3.childs += [gpuRedwing3]

    rredWing4 = sg.SceneGraphNode("rredWing4")
    rredWing4.childs += [gpuRedwing4]

    rwing = sg.SceneGraphNode("rwing")
    rwing.transform = tr.scale(-1,1,1)
    rwing.childs += [rredWing1, rredWing2, rredWing3, rredWing4]

    #Left side:

    lredWing1 = sg.SceneGraphNode("lredWing1")
    lredWing1.childs += [gpuRedwing1]

    lredWing2 = sg.SceneGraphNode("lredWing2")
    lredWing2.childs += [gpuRedwing2]

    lredWing3 = sg.SceneGraphNode("lredWing3")
    lredWing3.childs += [gpuRedwing3]

    lredWing4 = sg.SceneGraphNode("lredWing4")
    lredWing4.childs += [gpuRedwing4]

    lwing = sg.SceneGraphNode("lwing")
    lwing.transform = tr.matmul([
            tr.translate(0, 0, 0),
            tr.rotationZ(60 * np.pi / 180),
    ])
    lwing.childs += [lredWing1, lredWing2, lredWing3, lredWing4]

    #wing grafo:

    wings = sg.SceneGraphNode("wings")
    wings.transform = tr.scale(2,2,2) 
    wings.childs += [lwing,rwing]

    mariposa = sg.SceneGraphNode("mariposa")
    mariposa.childs += [body,wings]

    return mariposa

def createScenery(pipeline):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    

    gpuGreenGrass = createGPUShape(bs.createTextureNormalsCube())
    gpuGreenGrass.texture = es.textureSimpleSetup(
        getAssetPath("grass.jpg"), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)

    gpuBrownCube = createGPUShape(bs.createTextureNormalsCube())
    gpuBrownCube.texture = es.textureSimpleSetup(
        getAssetPath("oak.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)


    #Leaf
    leaf_vertices = [
    # x   y             text coord  normals
    0.5, 0.0, 0.5,      0, 1,        1,0,1,
    0.5, 0.0, -0.5,     0, 0,        1,0,-1,
    -0.5, 0.0, -0.5,    0, 1,        -1,0,-1,
    -0.5, 0.0, 0.5,     0, 0,        -1,0,1,
    0.0, 1, 0.0,        1, 1/2,      0,1,0, 
    ]
    leaf_indices = [
    0, 1, 2,
    0, 2, 3,
    0, 1, 4,
    0, 3, 4,
    2, 1, 4,
    2, 3, 4
    ]
    leaf = bs.Shape(leaf_vertices,leaf_indices)
    gpuGreenLeaf = createGPUShape(leaf)
    gpuGreenLeaf.texture = es.textureSimpleSetup(
        getAssetPath("leaf.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)


    #####GRAFOS#####

    leaf = sg.SceneGraphNode("leaf")
    leaf.transform = tr.matmul([
        tr.translate(0,0,0.5),
        tr.scale(1,1,2),
        tr.rotationX(np.pi/2)
    ])
    leaf.childs += [gpuGreenLeaf]

    trunk = sg.SceneGraphNode("trunk")
    trunk.transform = tr.matmul([
        tr.scale(0.25,0.25,1.5),
    ])
    trunk.childs += [gpuBrownCube]

    tree1 = sg.SceneGraphNode("tree")
    tree1.transform = tr.matmul([
        tr.translate(0,10,-4),
        tr.scale(2,2,2)
    ])
    tree1.childs += [trunk,leaf]

    tree2 = sg.SceneGraphNode("tree")
    tree2.transform = tr.matmul([
        tr.translate(-15,10,-4),
        tr.scale(2.5,2.5,2.5)
    ])
    tree2.childs += [trunk,leaf]

    tree3 = sg.SceneGraphNode("tree")
    tree3.transform = tr.matmul([
        tr.translate(-12,-4,-4),
        tr.scale(2.5,2.5,2.5)
    ])
    tree3.childs += [trunk,leaf]

    tree4 = sg.SceneGraphNode("tree")
    tree4.transform = tr.matmul([
        tr.translate(-6,0,-4),
        tr.scale(2.5,2.5,2.5)
    ])
    tree4.childs += [trunk,leaf]

    tree5 = sg.SceneGraphNode("tree")
    tree5.transform = tr.matmul([
        tr.translate(-5,6,-4),
        tr.scale(2.5,2.5,2.5)
    ])
    tree5.childs += [trunk,leaf]

    tree6 = sg.SceneGraphNode("tree")
    tree6.transform = tr.matmul([
        tr.translate(-25,6,-4),
        tr.scale(2.5,2.5,2.5)
    ])
    tree6.childs += [trunk,leaf]

    tree7 = sg.SceneGraphNode("tree")
    tree7.transform = tr.matmul([
        tr.translate(-5,26,-4),
        tr.scale(2.5,2.5,2.5)
    ])
    tree7.childs += [trunk,leaf]

    forest = sg.SceneGraphNode("forest")
    forest.childs += [tree1,tree2,tree3,tree4,tree5,tree6,tree7]

    floor = sg.SceneGraphNode("floor")
    floor.transform = tr.matmul([
        tr.scale(60,60,1),
        tr.translate(0,0,-5)
    ])
    floor.childs += [gpuGreenGrass]
   
    scenery = sg.SceneGraphNode ("scenery")
    scenery.childs += [floor,forest]

    return scenery

def importedAmongUs(pipeline,texture):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    
    Bvertices,Bindices = readObj2("amongUs.obj")

    gpuAmongUs = createGPUShape(bs.Shape(Bvertices,Bindices))
    gpuAmongUs.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)

    amongUs = sg.SceneGraphNode("amongUs")
    amongUs.transform = tr.matmul([
        tr.translate(20,-20,-4.5),
        tr.scale(0.2,0.2,0.2),
        tr.rotationZ(np.pi/2.5),

    ])
    amongUs.childs += [gpuAmongUs] 
    
    return amongUs

def createSun(pipeline,texture):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    
    gpuSun = createGPUShape(bs.anticreateTextureNormalsCube())
    gpuSun.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)
    
    sun = sg.SceneGraphNode("sun")
    sun.transform = tr.matmul([
        tr.translate(1,1,1),
        tr.scale(0.2,0.2,0.2),
        tr.rotationZ(np.pi/2.5),

    ])
    sun.childs += [gpuSun] 
    
    return sun

def importedMariposa(pipeline,texture):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    
    Bvertices,Bindices = readObj2("ASCII.obj")

    gpuButterfly = createGPUShape(bs.Shape(Bvertices,Bindices))
    gpuButterfly.texture = es.textureSimpleSetup(
        getAssetPath(texture), GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE, GL_LINEAR, GL_LINEAR)
    

    butterFly = sg.SceneGraphNode("butterfly")
    butterFly.transform = tr.matmul([
        tr.scale(0.015,0.015,0.015),
        tr.rotationX(np.pi/2),

    ])
    butterFly.childs += [gpuButterfly] 
    
    return butterFly

mariposaNode = createMariposa(textureGouraudPipeline,controller.inputTexture)
sunNode = createSun(textureGouraudPipeline,"sun1.jpg")
escenarioNode = createScenery(textureGouraudPipeline)
amongUsNode = importedAmongUs(textureGouraudPipeline,"roof2.jpg")
butterflypinkNode = importedMariposa(textureGouraudPipeline,"rosa-bebe.jpg")
butterflyblueNode = importedMariposa(textureGouraudPipeline,"calipso.jpg")



@controller.event
def on_draw():
    controller.clear()

    # Si el controller está en modo fillPolygon, dibuja polígonos. Si no, líneas.
    if controller.fillPolygon:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Using the same view and projection matrices in the whole application
    projection = tr.perspective(50, float(WIDTH)/float(HEIGHT), 0.1, 100)

    view = controller.camara

    lightX = 30 * np.sin(controller.light_theta) 
    lightY = 30 * np.cos(controller.light_theta)
    lightPos = np.array([lightX,2,lightY])
    
    # The axis is drawn without lighting effects
    if controller.showAxis:
        glUseProgram(colorPipeline.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(colorPipeline.shaderProgram, "projection"), 1, GL_TRUE, projection)
        glUniformMatrix4fv(glGetUniformLocation(colorPipeline.shaderProgram, "view"), 1, GL_TRUE, view)
        glUniformMatrix4fv(glGetUniformLocation(colorPipeline.shaderProgram, "model"), 1, GL_TRUE, tr.identity())
        colorPipeline.drawCall(gpuAxis, GL_LINES)

    # Selecting the lighting shader program
    if controller.lightingModel == LIGHT_FLAT:
            lightingPipeline = textureFlatPipeline
    elif controller.lightingModel == LIGHT_GOURAUD:
            lightingPipeline = textureGouraudPipeline
    elif controller.lightingModel == LIGHT_PHONG:
            lightingPipeline = texturePhongPipeline
    else:
        raise Exception()
        
    glUseProgram(lightingPipeline.shaderProgram)

    # Setting all uniform shader variables
        
    # White light in all components: ambient, diffuse and specular.
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "La"), 1.0, 1.0, 1.0)
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "Ld"), 1.0, 1.0, 1.0)
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "Ls"), 1.0, 1.0, 1.0)

    # Object is barely visible at only ambient. Bright white for diffuse and specular components.
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "Ka"), 0.2, 0.2, 0.2)
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "Kd"), 0.9, 0.9, 0.9)
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "Ks"), 1.0, 1.0, 1.0)

    # TO DO: Explore different parameter combinations to understand their effect!
    
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "lightPosition"), lightPos[0], lightPos[1], lightPos[2])
    glUniform3f(glGetUniformLocation(lightingPipeline.shaderProgram, "viewPosition"), viewPos[0], viewPos[1], viewPos[2])
    glUniform1ui(glGetUniformLocation(lightingPipeline.shaderProgram, "shininess"), 100)

    glUniform1f(glGetUniformLocation(lightingPipeline.shaderProgram, "constantAttenuation"), 0.001)
    glUniform1f(glGetUniformLocation(lightingPipeline.shaderProgram, "linearAttenuation"), 0.001)
    glUniform1f(glGetUniformLocation(lightingPipeline.shaderProgram, "quadraticAttenuation"), 0.001)

    glUniformMatrix4fv(glGetUniformLocation(lightingPipeline.shaderProgram, "projection"), 1, GL_TRUE, projection)
    glUniformMatrix4fv(glGetUniformLocation(lightingPipeline.shaderProgram, "view"), 1, GL_TRUE, view)

    theta = np.sin(3.0 * controller.total_time)

    mariposaNode = createMariposa(textureGouraudPipeline,controller.inputTexture)

    mariposaNode.transform = tr.translate(3 * np.sin(controller.total_time),3 * np.cos(controller.total_time),(3 * np.cos(np.sin(controller.total_time))-3))
    lwingRotationNode = sg.findNode(mariposaNode, "lwing")
    lwingRotationNode.transform = tr.rotationZ(theta)
    rwingRotationNode = sg.findNode(mariposaNode, "rwing")
    rwingRotationNode.transform = tr.rotationZ(np.pi-theta)

    sunNode.transform = tr.translate(lightPos[0], lightPos[1], lightPos[2])

    butterflypinkNode.transform = tr.matmul([
        tr.translate(3 * np.cos(controller.total_time +2),3 * np.sin(controller.total_time),(3 * np.cos(np.sin(controller.total_time))-3)),
        tr.scale(0.015,0.015,0.015),
        tr.rotationX(np.pi/2),
        tr.rotationY(np.pi/3),
    ])

    butterflyblueNode.transform = tr.matmul([
        tr.translate(3 * np.cos(controller.total_time),(3 * np.cos(np.sin(controller.total_time))-3),3 * np.sin(controller.total_time+2)),
        tr.scale(0.015,0.015,0.015),
        tr.rotationX(np.pi/2),
        tr.rotationY(np.pi/3),
    ])


    sg.drawSceneGraphNode(mariposaNode, lightingPipeline, "model")
    sg.drawSceneGraphNode(escenarioNode, lightingPipeline, "model")
    sg.drawSceneGraphNode(amongUsNode, lightingPipeline, "model")
    sg.drawSceneGraphNode(sunNode, lightingPipeline, "model")
    sg.drawSceneGraphNode(butterflypinkNode, lightingPipeline, "model")
    sg.drawSceneGraphNode(butterflyblueNode, lightingPipeline, "model")

def update(dt, controller):
    controller.total_time += dt
    controller.light_theta += dt * controller.moving_direction

# Try to call this function 60 times per second
pyglet.clock.schedule(update, controller)
# Set the view
pyglet.app.run()
