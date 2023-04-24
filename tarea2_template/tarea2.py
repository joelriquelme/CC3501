# coding=utf-8

import pyglet
from OpenGL.GL import *
from grafica import basic_shapes as bs
from grafica import easy_shaders as es
from grafica import transformations as tr
from grafica import scene_graph as sg

class Controller(pyglet.window.Window):

    def __init__(self, width, height, title="Tarea 2 - SU NOMBRE AQUI"):
        super().__init__(width, height, title)
        self.total_time = 0.0
        self.fillPolygon = True
        self.pipeline = None

# We will use the global controller as communication with the callback function
WIDTH, HEIGHT = 1280, 800
controller = Controller(width=WIDTH, height=HEIGHT)

# Setting up the clear screen color
glClearColor(0.15, 0.15, 0.15, 1.0)

# Setting the model (data of our code)
# Creating our shader program and telling OpenGL to use it
pipeline = # AQUI VA LA PIPELINE PARA 3D
controller.pipeline = pipeline
glUseProgram(pipeline.shaderProgram)


# What happens when the user presses these keys
@controller.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        controller.fillPolygon = not controller.fillPolygon
    elif symbol == pyglet.window.key.ESCAPE:
        controller.close()

@controller.event
def on_draw():
    controller.clear()


def update(dt, controller):
    controller.total_time += dt

# Try to call this function 60 times per second
pyglet.clock.schedule(update, controller)
# Set the view
pyglet.app.run()
