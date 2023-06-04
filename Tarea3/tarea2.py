# coding=utf-8

from readerStl import *
import os.path
import sys
import numpy as np
import pyglet
from OpenGL.GL import *

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.scene_graph as sg
import grafica.easy_shaders as es

class Controller(pyglet.window.Window):

    def __init__(self, width, height, title="Tarea 2 Joel Riquelme"):
        super().__init__(width, height, title)
        self.total_time = 0.0
        self.fillPolygon = True
        self.showAxis = True
        self.pipeline = None
        self.repeats = 0
        self.camara = tr.lookAt(
            np.array([10,-10,5]),
            np.array([0,0,0]),
            np.array([0,0,1])
        )

# Se asigna el ancho y alto de la ventana y se crea.
WIDTH, HEIGHT = 1280, 800
controller = Controller(width=WIDTH, height=HEIGHT)
# Se asigna el color de fondo de la ventana
glClearColor(0, 0.67, 0.894, 1.0)

# Como trabajamos en 3D, necesitamos chequear cuáles objetos están en frente, y cuáles detrás.
glEnable(GL_DEPTH_TEST)

# Se configura el pipeline y se le dice a OpenGL que utilice ese shader
mvpPipeline = es.SimpleModelViewProjectionShaderProgram()
controller.pipeline = mvpPipeline
glUseProgram(mvpPipeline.shaderProgram)

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
        controller.camara = tr.lookAt(
            np.array([10,-10,5]),
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key._2:
        controller.camara = tr.lookAt(
            np.array([10,0,5]),
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key._3:
        controller.camara = tr.lookAt(
            np.array([10, -10,0]),
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key._4:
        controller.camara = tr.lookAt(
            np.array([0, 1,30]),
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    elif symbol == pyglet.window.key._5:
        controller.camara = tr.lookAt(
            np.array([-10,10, 7]),
            np.array([0,0,0]),
            np.array([0,0,1])
        )

    else:
        print('Unknown key')

#Función que crea la mariposa

def createMariposa(pipeline):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    
    #Setting de left half of de body
    black_body1_vertices = [
    # x   y  z  r    g    b
    (2/WIDTH) *0,   -0.025, (2/HEIGHT)*200,  0.0, 0.0, 0.0,
    (2/WIDTH) *-30, -0.015,  (2/HEIGHT)*180, 0.0, 0.0, 0.0, 
    (2/WIDTH) *-8, -0.01,(2/HEIGHT)*20,  0.0, 0.0, 0.0,
    (2/WIDTH) *0, -0.01, (2/HEIGHT)*0,  0.0, 0.0, 0.0,
    (2/WIDTH) *0,   0.025, (2/HEIGHT)*200,  0.0, 0.0, 0.0,
    (2/WIDTH) *-30, 0.015,  (2/HEIGHT)*180, 0.0, 0.0, 0.0, 
    (2/WIDTH) *-8, 0.01,(2/HEIGHT)*20,  0.0, 0.0, 0.0,
    (2/WIDTH) *0, 0.01, (2/HEIGHT)*0,  0.0, 0.0, 0.0,
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

    #Setting de right half of the body
    gray_body2_vertices = [
    # x   y  z  r    g    b
    (2/WIDTH) *0, -0.025,  (2/HEIGHT)*200,   0.25, 0.25, 0.25,
    (2/WIDTH) *30, -0.015, (2/HEIGHT)*180,  0.25, 0.25, 0.25, 
    (2/WIDTH) *8, -0.01, (2/HEIGHT)*20,  0.25, 0.25, 0.25,
    (2/WIDTH) *0, -0.01, (2/HEIGHT)*0,  0.25, 0.25, 0.25,
    (2/WIDTH) *0, 0.025,  (2/HEIGHT)*200,   0.35, 0.35, 0.35,
    (2/WIDTH) *30, 0.015, (2/HEIGHT)*180,  0.35, 0.35, 0.35, 
    (2/WIDTH) *8, 0.01, (2/HEIGHT)*20,  0.35, 0.35, 0.35,
    (2/WIDTH) *0, 0.01, (2/HEIGHT)*0,  0.35, 0.35, 0.35,
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

    #Setting the wing 1
    red_wing1_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-22, -0.01,  (2/HEIGHT)*194, 0.70, 0.0, 0.0,
    (2/WIDTH) *-15, -0.01, (2/HEIGHT)*120, 0.70, 0.0, 0.0, 
    (2/WIDTH) *-200, -0.05, (2/HEIGHT)*220, 0.70, 0.0, 0.0,
    (2/WIDTH) *-160, -0.03, (2/HEIGHT)*240, 0.70, 0.0, 0.0,
    (2/WIDTH) *-108, -0.03, (2/HEIGHT)*232, 0.70, 0.0, 0.0,
    (2/WIDTH) *-22, 0.01,  (2/HEIGHT)*194, 0.85, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01, (2/HEIGHT)*120, 0.85, 0.0, 0.0, 
    (2/WIDTH) *-200, 0.05, (2/HEIGHT)*220, 0.85, 0.0, 0.0,
    (2/WIDTH) *-160, 0.03, (2/HEIGHT)*240, 0.85, 0.0, 0.0,
    (2/WIDTH) *-108, 0.03, (2/HEIGHT)*232, 0.85, 0.0, 0.0,
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

    #Setting the wing 2
    red_wing2_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-15, -0.01,  (2/HEIGHT)*120,   0.5, 0.0, 0.0,
    (2/WIDTH) *-200, -0.05, (2/HEIGHT)*220,  0.5, 0.0, 0.0, 
    (2/WIDTH) *-180, -0.01, (2/HEIGHT)*120,  0.5, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01,  (2/HEIGHT)*120,   0.6, 0.0, 0.0,
    (2/WIDTH) *-200, 0.05, (2/HEIGHT)*220,  0.6, 0.0, 0.0, 
    (2/WIDTH) *-180, 0.01, (2/HEIGHT)*120,  0.6, 0.0, 0.0,    
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

    #Setting the wing 3
    red_wing3_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-15, -0.01,  (2/HEIGHT)*120,  0.70, 0.0, 0.0,
    (2/WIDTH) *-140, -0.01, (2/HEIGHT)*120,  0.70, 0.0, 0.0, 
    (2/WIDTH) *-170, -0.01, (2/HEIGHT)*80, 0.70, 0.0, 0.0,
    (2/WIDTH) *-150, -0.05, (2/HEIGHT)*20, 0.70, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01,  (2/HEIGHT)*120,  0.85, 0.0, 0.0,
    (2/WIDTH) *-140, 0.01, (2/HEIGHT)*120,  0.85, 0.0, 0.0, 
    (2/WIDTH) *-170, 0.01, (2/HEIGHT)*80, 0.85, 0.0, 0.0,
    (2/WIDTH) *-150, 0.05, (2/HEIGHT)*20, 0.85, 0.0, 0.0,
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

    #Setting the left wing 4
    red_wing4_vertices = [
    # x   y    r    g    b
    (2/WIDTH) *-15, -0.01, (2/HEIGHT)* 120, 0.5, 0.0, 0.0,
    (2/WIDTH) *-60, -0.01, (2/HEIGHT)*0, 0.5, 0.0, 0.0, 
    (2/WIDTH) *-110, -0.03, (2/HEIGHT)*-20, 0.5, 0.0, 0.0,
    (2/WIDTH) *-150, -0.05, (2/HEIGHT)*20, 0.5, 0.0, 0.0,
    (2/WIDTH) *-15, 0.01, (2/HEIGHT)* 120, 0.6, 0.0, 0.0,
    (2/WIDTH) *-60, 0.01, (2/HEIGHT)*0, 0.6, 0.0, 0.0, 
    (2/WIDTH) *-110, 0.03, (2/HEIGHT)*-20, 0.6, 0.0, 0.0,
    (2/WIDTH) *-150, 0.05, (2/HEIGHT)*20, 0.6, 0.0, 0.0,

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
    

    grass = bs.createColorCube(0.0, 0.33, 0.0)
    gpuGreenGrass = createGPUShape(grass)

    gpuBrownCube = createGPUShape(bs.createColorCube(0.33, 0.1882, 0.055))

    #Leaf
    leaf_vertices = [
    # x   y    r    g    b
    0.5, 0.0, 0.5, 0, 1, 0,
    0.5, 0.0, -0.5, 0, 1, 0,
    -0.5, 0.0, -0.5, 0, 1, 0,
    -0.5, 0.0, 0.5, 0, 1, 0,
    0.0, 1, 0.0, 0, 1, 0, 
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
        tr.scale(1000,1000,1),
        tr.translate(0,0,-5)
    ])
    floor.childs += [gpuGreenGrass]
   
    scenery = sg.SceneGraphNode ("scenery")
    scenery.childs += [floor,forest]

    return scenery

def importedMariposa(pipeline, r,g,b):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    
    Bvertices,Bindices = readStl("ASCII.stl", r, g, b)

    gpuButterfly = createGPUShape(bs.Shape(Bvertices,Bindices))


    butterFly = sg.SceneGraphNode("butterfly")
    butterFly.transform = tr.matmul([
        tr.scale(0.015,0.015,0.015),
        tr.rotationX(np.pi/2),

    ])
    butterFly.childs += [gpuButterfly] 
    
    return butterFly

def importedAmongUs(pipeline, r, g, b):

    # Convenience function to ease initialization
    def createGPUShape(shape):
        gpuShape = es.GPUShape().initBuffers()
        pipeline.setupVAO(gpuShape)
        gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
        return gpuShape
    
    Bvertices,Bindices = readStl("amongUs.stl", r, g, b)

    gpuAmongUs = createGPUShape(bs.Shape(Bvertices,Bindices))

    amongUs = sg.SceneGraphNode("amongUs")
    amongUs.transform = tr.matmul([
        tr.translate(20,-20,-4),
        tr.scale(0.2,0.2,0.2),
        tr.rotationZ(np.pi/2.5),

    ])
    amongUs.childs += [gpuAmongUs] 
    
    return amongUs


    

# Creating shapes on GPU memory
cpuAxis = bs.createAxis(7)
gpuAxis = es.GPUShape().initBuffers()
mvpPipeline.setupVAO(gpuAxis)
gpuAxis.fillBuffers(cpuAxis.vertices, cpuAxis.indices, GL_STATIC_DRAW)

mariposaNode = createMariposa(mvpPipeline)
escenarioNode = createScenery(mvpPipeline)
butterflypinkNode = importedMariposa(mvpPipeline, 1.0 , 0.7765, 0.9373)
butterflyblueNode = importedMariposa(mvpPipeline, 0.6627 , 0.9804, 0.9569)
amongUsNode = importedAmongUs(mvpPipeline, 1.0, 0.0, 0.0)

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
    glUniformMatrix4fv(glGetUniformLocation(mvpPipeline.shaderProgram, "projection"), 1, GL_TRUE,
                       projection)


    view = controller.camara


    glUniformMatrix4fv(glGetUniformLocation(mvpPipeline.shaderProgram, "view"), 1, GL_TRUE, view)

    if controller.showAxis:
        glUniformMatrix4fv(glGetUniformLocation(mvpPipeline.shaderProgram, "model"), 1, GL_TRUE,
                           tr.identity())
        mvpPipeline.drawCall(gpuAxis, GL_LINES)


    theta = np.sin(3.0 * controller.total_time)

    mariposaNode.transform = tr.translate(3 * np.sin(controller.total_time),3 * np.cos(controller.total_time),(3 * np.cos(np.sin(controller.total_time))-3))
    lwingRotationNode = sg.findNode(mariposaNode, "lwing")
    lwingRotationNode.transform = tr.rotationZ(theta)
    rwingRotationNode = sg.findNode(mariposaNode, "rwing")
    rwingRotationNode.transform = tr.rotationZ(np.pi-theta)

    pinkNode = sg.findNode(butterflypinkNode, "butterfly")
    pinkNode.transform = tr.matmul([
        tr.translate(3 * np.cos(controller.total_time +2),3 * np.sin(controller.total_time),(3 * np.cos(np.sin(controller.total_time))-3)),
        tr.scale(0.015,0.015,0.015),
        tr.rotationX(np.pi/2),
        #tr.rotationY(np.pi-theta),
    ])

    blueNode = sg.findNode(butterflyblueNode, "butterfly")
    blueNode.transform = tr.matmul([
        tr.translate(3 * np.cos(controller.total_time),(3 * np.cos(np.sin(controller.total_time))-3),3 * np.sin(controller.total_time+2)),
        tr.scale(0.015,0.015,0.015),
        tr.rotationX(np.pi/2),
        #tr.rotationY(theta),
    ])

    sg.drawSceneGraphNode(mariposaNode, mvpPipeline, "model")
    sg.drawSceneGraphNode(escenarioNode, mvpPipeline, "model")
    sg.drawSceneGraphNode(butterflypinkNode, mvpPipeline, "model")
    sg.drawSceneGraphNode(butterflyblueNode, mvpPipeline, "model")
    sg.drawSceneGraphNode(amongUsNode, mvpPipeline, "model")
    

def update(dt, controller):
    controller.total_time += dt

# Try to call this function 60 times per second
pyglet.clock.schedule(update, controller)
# Set the view
pyglet.app.run()
