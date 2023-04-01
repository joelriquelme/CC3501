# coding=utf-8

import pyglet
from math import sin, cos
from OpenGL.GL import *
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grafica import basic_shapes as bs
from grafica import easy_shaders as es
from grafica import transformations as tr
from shapes_utils import HighLevelGPUShape

class Controller(pyglet.window.Window):

    def __init__(self, width, height, title="Tarea 1 Joel Riquelme v2.0"):
        super().__init__(width, height, title)
        self.total_time = 0.0
        self.fillPolygon = True
        self.pipeline = None
        self.repeats = 0

# We will use the global controller as communication with the callback function
WIDTH, HEIGHT = 1200, 800
controller = Controller(width=WIDTH, height=HEIGHT)

# Setting up the clear screen color
pyglet.gl.glClearColor(0, 0.67, 0.894, 1.0)

pipeline = es.SimpleTransformShaderProgram()
controller.pipeline = pipeline
glUseProgram(pipeline.shaderProgram)

###########################

#Setting the background:

#Grass
green_grass_vertices = [
   # x   y  z  r    g    b
    WIDTH * 0.5,  0, 0,  0.0, 0.33, 0.0,
   -WIDTH * 0.5 ,  HEIGHT * -0.5, 0,  0.0, 0.5, 0.0, 
   -WIDTH * 0.5, 0, 0, 0.0, 0.33, 0.0,
    WIDTH * 0.5,  HEIGHT * -0.5,  0, 0.0, 0.5, 0.0,
]
grass_vertices = [
    0, 1, 3,
    0, 1, 2,
]
grass = bs.Shape(green_grass_vertices,grass_vertices)


#Tree trunk
brown_trunk_vertices = [
   # x   y    r    g    b
    (2/WIDTH) * -5,   (2/HEIGHT)*0, 0, 0.33, 0.1882, 0.055,
   (2/WIDTH) *5,  (2/HEIGHT)*0, 0, 0.33, 0.1882, 0.055, 
   (2/WIDTH) *5, (2/HEIGHT)*20, 0, 0.467, 0.235, 0.0235,
    (2/WIDTH) *-5,  (2/HEIGHT)*20, 0, 0.467, 0.235, 0.0235,
]
trunk_vertices = [
    0, 1, 2,
    0, 2, 3,
]
trunk = bs.Shape(brown_trunk_vertices,trunk_vertices)

#Tree leaf
green_leaf_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *30,   (2/HEIGHT)*20, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *15,   (2/HEIGHT)*35, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *25,   (2/HEIGHT)*35, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *10,   (2/HEIGHT)*50, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *20,   (2/HEIGHT)*50, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *5,   (2/HEIGHT)*65, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *15,   (2/HEIGHT)*65, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *0,   (2/HEIGHT)*80, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *-15,   (2/HEIGHT)*65, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *-5,   (2/HEIGHT)*65, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *-20,   (2/HEIGHT)*50, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *-10,   (2/HEIGHT)*50, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *-25,   (2/HEIGHT)*35, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *-15,   (2/HEIGHT)*35, 0, 0.0784, 0.4784, 0.1333,
    (2/WIDTH) *-30,   (2/HEIGHT)*20, 0, 0.0784, 0.4784, 0.1333,

]
leaf_vertices = [
    0, 14, 13,
    0, 13, 1,
    2, 12, 11,
    2, 11, 3,
    4, 10, 9,
    4, 9, 5,
    6, 7, 8,
    
]
leaf = bs.Shape(green_leaf_vertices,leaf_vertices)

#Setting de left half of de body
black_body1_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *0,   (2/HEIGHT)*200, 0.0,  0.0, 0.0, 0.0,
   (2/WIDTH) *-30,  (2/HEIGHT)*180, 0.0, 0.0, 0.0, 0.0, 
   (2/WIDTH) *-8, (2/HEIGHT)*20, 0.0, 0.0, 0.0, 0.0,
    (2/WIDTH) *0,  (2/HEIGHT)*0, 0.0, 0.0, 0.0, 0.0,
]
body1_vertices = [
    0, 1, 2,
    0, 2, 3,
]
body1 = bs.Shape(black_body1_vertices,body1_vertices)

#Setting de right half of the body
gray_body2_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *0,   (2/HEIGHT)*200, 0.0,  0.25, 0.25, 0.25,
   (2/WIDTH) *30,  (2/HEIGHT)*180, 0.0, 0.25, 0.25, 0.25, 
   (2/WIDTH) *8, (2/HEIGHT)*20, 0.0, 0.25, 0.25, 0.25,
    (2/WIDTH) *0,  (2/HEIGHT)*0, 0.0, 0.25, 0.25, 0.25,
]
body2_vertices = [
    0, 1, 2,
    0, 2, 3,
]
body2 = bs.Shape(gray_body2_vertices,body2_vertices)

#Left Side:

#Setting the left wing 1
red_lwing1_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *-22,   (2/HEIGHT)*194, 0.0,  0.75, 0.0, 0.0,
   (2/WIDTH) *-15,  (2/HEIGHT)*120, 0.0, 0.75, 0.0, 0.0, 
   (2/WIDTH) *-200, (2/HEIGHT)*220, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *-160, (2/HEIGHT)*240, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *-108, (2/HEIGHT)*232, 0.0, 0.75, 0.0, 0.0,
]
lwing1_vertices = [
    0, 1, 2,
    0, 2, 3,
    0, 3, 4,
]
lwing1 = bs.Shape(red_lwing1_vertices,lwing1_vertices)

#Setting the left wing 2
red_lwing2_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *-15,   (2/HEIGHT)*120, 0.0,  0.5, 0.0, 0.0,
   (2/WIDTH) *-200,  (2/HEIGHT)*220, 0.0, 0.5, 0.0, 0.0, 
   (2/WIDTH) *-180, (2/HEIGHT)*120, 0.0, 0.5, 0.0, 0.0,
]
lwing2_vertices = [
    0, 1, 2,
]
lwing2 = bs.Shape(red_lwing2_vertices,lwing2_vertices)

#Setting the left wing 3
red_lwing3_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *-15,   (2/HEIGHT)*120, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *-140,  (2/HEIGHT)*120, 0.0, 0.75, 0.0, 0.0, 
   (2/WIDTH) *-170, (2/HEIGHT)*80, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *-150, (2/HEIGHT)*20, 0.0, 0.75, 0.0, 0.0,
]
lwing3_vertices = [
    0, 1, 2,
    0, 2, 3,
]
lwing3 = bs.Shape(red_lwing3_vertices,lwing3_vertices)

#Setting the left wing 4
red_lwing4_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *-15,  (2/HEIGHT)* 120, 0.0, 0.5, 0.0, 0.0,
   (2/WIDTH) *-60,  (2/HEIGHT)*0, 0.0, 0.5, 0.0, 0.0, 
   (2/WIDTH) *-110, (2/HEIGHT)*-20, 0.0, 0.5, 0.0, 0.0,
   (2/WIDTH) *-150, (2/HEIGHT)*20, 0.0, 0.5, 0.0, 0.0,
]
lwing4_vertices = [
    0, 1, 2,
    0, 2, 3,
]
lwing4 = bs.Shape(red_lwing4_vertices,lwing4_vertices)

#Right Side:

#Setting the right wing 1
red_rwing1_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *22,   (2/HEIGHT)*194, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *15,  (2/HEIGHT)*120, 0.0, 0.75, 0.0, 0.0, 
   (2/WIDTH) *200, (2/HEIGHT)*220, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *160, (2/HEIGHT)*240, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *108, (2/HEIGHT)*232, 0.0, 0.75, 0.0, 0.0,
]
rwing1_vertices = [
    0, 1, 2,
    0, 2, 3,
    0, 3, 4,
]
rwing1 = bs.Shape(red_rwing1_vertices,rwing1_vertices)

#Setting the right wing 2
red_rwing2_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *15,   (2/HEIGHT)*120, 0.0, 0.5, 0.0, 0.0,
   (2/WIDTH) *200,  (2/HEIGHT)*220, 0.0, 0.5, 0.0, 0.0, 
   (2/WIDTH) *180, (2/HEIGHT)*120, 0.0, 0.5, 0.0, 0.0,
]
rwing2_vertices = [
    0, 1, 2,
]
rwing2 = bs.Shape(red_rwing2_vertices,rwing2_vertices)

#Setting the right wing 3
red_rwing3_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *15,   (2/HEIGHT)*120, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *140,  (2/HEIGHT)*120, 0.0, 0.75, 0.0, 0.0, 
   (2/WIDTH) *170, (2/HEIGHT)*80, 0.0, 0.75, 0.0, 0.0,
   (2/WIDTH) *150, (2/HEIGHT)*20, 0.0, 0.75, 0.0, 0.0,
]
rwing3_vertices = [
    0, 1, 2,
    0, 2, 3,
]
rwing3 = bs.Shape(red_rwing3_vertices,rwing3_vertices)

#Setting the right wing 4
red_rwing4_vertices = [
   # x   y    r    g    b
    (2/WIDTH) *15,   (2/HEIGHT)*120, 0.0, 0.5, 0.0, 0.0,
   (2/WIDTH) *60,  (2/HEIGHT)*0, 0.0, 0.5, 0.0, 0.0, 
   (2/WIDTH) *110, (2/HEIGHT)*-20, 0.0, 0.5, 0.0, 0.0,
   (2/WIDTH) *150, (2/HEIGHT)*20, 0.0, 0.5, 0.0, 0.0,
]
rwing4_vertices = [
    0, 1, 2,
    0, 2, 3,
]
rwing4 = bs.Shape(red_rwing4_vertices,rwing4_vertices)


#GPU's

gpuGrass = HighLevelGPUShape(pipeline, grass)
gpuTrunk1 = HighLevelGPUShape(pipeline, trunk)
gpuTrunk2 = HighLevelGPUShape(pipeline, trunk)
gpuTrunk3 = HighLevelGPUShape(pipeline, trunk)
gpuLeaf1 = HighLevelGPUShape(pipeline, leaf)
gpuLeaf2 = HighLevelGPUShape(pipeline, leaf)
gpuLeaf3 = HighLevelGPUShape(pipeline, leaf)
gpuBody1 = HighLevelGPUShape(pipeline, body1)
gpuBody2 = HighLevelGPUShape(pipeline, body2)
gpuLWing1 = HighLevelGPUShape(pipeline, lwing1)
gpuLWing2 = HighLevelGPUShape(pipeline, lwing2)
gpuLWing3 = HighLevelGPUShape(pipeline, lwing3)
gpuLWing4 = HighLevelGPUShape(pipeline, lwing4)
gpuRWing1 = HighLevelGPUShape(pipeline, rwing1)
gpuRWing2 = HighLevelGPUShape(pipeline, rwing2)
gpuRWing3 = HighLevelGPUShape(pipeline, rwing3)
gpuRWing4 = HighLevelGPUShape(pipeline, rwing4)


#Draw's

def draw_grass(controller: Controller):
    gpuGrass.draw(controller.pipeline)

def draw_trunk(controller: Controller):
    gpuTrunk1.scale = tr.uniformScale(3.0)
    gpuTrunk1.draw(controller.pipeline)
    gpuTrunk2.scale = tr.uniformScale(3.5)
    gpuTrunk2.translation = tr.translate(-0.5, 0, 0.0)
    gpuTrunk2.draw(controller.pipeline)
    gpuTrunk3.scale = tr.uniformScale(4.0)
    gpuTrunk3.translation = tr.translate(0.5, 0, 0.0)
    gpuTrunk3.draw(controller.pipeline)

def draw_leaf(controller: Controller):
    gpuLeaf1.scale = tr.uniformScale(3.0)
    gpuLeaf1.draw(controller.pipeline)
    gpuLeaf2.scale = tr.uniformScale(3.5)
    gpuLeaf2.translation = tr.translate(-0.5, 0, 0.0)
    gpuLeaf2.draw(controller.pipeline)
    gpuLeaf3.scale = tr.uniformScale(4.0)
    gpuLeaf3.translation = tr.translate(0.5, 0, 0.0)
    gpuLeaf3.draw(controller.pipeline)

def draw_body(controller: Controller):
    gpuBody1.draw(controller.pipeline)
    gpuBody1.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)
    gpuBody2.draw(controller.pipeline)
    gpuBody2.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)

def draw_lwing(controller: Controller):
    gpuLWing1.draw(controller.pipeline)
    gpuLWing1.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)
    gpuLWing1.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )
    gpuLWing2.draw(controller.pipeline)
    gpuLWing2.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)
    gpuLWing2.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )
    gpuLWing3.draw(controller.pipeline)
    gpuLWing3.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)
    gpuLWing3.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )
    gpuLWing4.draw(controller.pipeline)
    gpuLWing4.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0) 
    gpuLWing4.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )

def draw_rwing(controller: Controller):
    gpuRWing1.draw(controller.pipeline)
    gpuRWing1.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)
    gpuRWing1.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )
    gpuRWing2.draw(controller.pipeline)
    gpuRWing2.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)
    gpuRWing2.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )
    gpuRWing3.draw(controller.pipeline)
    gpuRWing3.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0)
    gpuRWing3.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )
    gpuRWing4.draw(controller.pipeline)
    gpuRWing4.translation = tr.translate(
        0.5 * cos(controller.total_time * 3.0), 0.3 * sin(controller.total_time * 3.0),0.0) 
    gpuRWing4.scale = tr.scale(0.8 + 0.6 * sin(controller.total_time*5),1,0.0 )


# What happens when the user presses these keys
@controller.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE:
        controller.close()

@controller.event
def on_draw():
    controller.clear()
    draw_grass(controller)
    draw_trunk(controller)
    draw_leaf(controller)
    draw_body(controller)
    draw_lwing(controller)
    draw_rwing(controller)


# Each time update is called, on_draw is called again
# That is why it is better to draw and update each one in a separated function
# We could also create 2 different gpuQuads and different transform for each
# one, but this would use more memory
def update(dt, controller):
    controller.total_time += dt

# Try to call this function 60 times per second
pyglet.clock.schedule(update, controller)
# Set the view
pyglet.app.run()

