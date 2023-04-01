# coding=utf-8

import pyglet
from math import sin, cos
from pyglet_basic_shapes_wrapper import CustomShape2D


class Controller(pyglet.window.Window):

    def __init__(self, width, height, title="Tarea 1 Joel Riquelme v1.0"):
        super().__init__(width, height, title)
        self.total_time = 0.0
        self.fillPolygon = True


# We will use the global controller as communication with the callback function
WIDTH, HEIGHT = 1200, 800
controller = Controller(width=WIDTH, height=HEIGHT)

# Setting up the clear screen color
pyglet.gl.glClearColor(0, 0.67, 0.894, 1.0)

###########################

#Setting the background:

#Grass
green_grass_vertices = [
   # x   y    r    g    b
    WIDTH * 0.5,  0,  0.0, 0.33, 0.0,
   -WIDTH * 0.5 ,  HEIGHT * -0.5,  0.0, 0.5, 0.0, 
   -WIDTH * 0.5, 0, 0.0, 0.33, 0.0,
    WIDTH * 0.5,  HEIGHT * -0.5, 0.0, 0.5, 0.0,
]
grass_vertices = [
    0, 1, 3,
    0, 1, 2,
]

#Tree:
#Tree trunk
brown_trunk_vertices = [
   # x   y    r    g    b
    -5,   0,  0.33, 0.1882, 0.055,
   5,  0,  0.33, 0.1882, 0.055, 
   5, 20, 0.467, 0.235, 0.0235,
    -5,  20, 0.467, 0.235, 0.0235,
]
trunk_vertices = [
    0, 1, 2,
    0, 2, 3,
]

#Tree leaf
green_leaf_vertices = [
   # x   y    r    g    b
    30,   20,  0.0784, 0.4784, 0.1333,
    15,   35,  0.0784, 0.4784, 0.1333,
    25,   35,  0.0784, 0.4784, 0.1333,
    10,   50,  0.0784, 0.4784, 0.1333,
    20,   50,  0.0784, 0.4784, 0.1333,
    5,   65,  0.0784, 0.4784, 0.1333,
    15,   65,  0.0784, 0.4784, 0.1333,
    0,   80,  0.0784, 0.4784, 0.1333,
    -15,   65,  0.0784, 0.4784, 0.1333,
    -5,   65,  0.0784, 0.4784, 0.1333,
    -20,   50,  0.0784, 0.4784, 0.1333,
    -10,   50,  0.0784, 0.4784, 0.1333,
    -25,   35,  0.0784, 0.4784, 0.1333,
    -15,   35,  0.0784, 0.4784, 0.1333,
    -30,   20,  0.0784, 0.4784, 0.1333,

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


#Setting de left half of de body
black_body1_vertices = [
   # x   y    r    g    b
    0,   200,  0.0, 0.0, 0.0,
   -20,  180,  0.0, 0.0, 0.0, 
   -8, 20, 0.0, 0.0, 0.0,
    0,  0, 0.0, 0.0, 0.0,
]
body1_vertices = [
    0, 1, 2,
    0, 2, 3,
]

#Setting de right half of the body
gray_body2_vertices = [
   # x   y    r    g    b
    0,   200,  0.25, 0.25, 0.25,
   20,  180,  0.25, 0.25, 0.25, 
   8, 20, 0.25, 0.25, 0.25,
    0,  0, 0.25, 0.25, 0.25,
]
body2_vertices = [
    0, 1, 2,
    0, 2, 3,
]

#Left Side:

#Setting the left wing 1
red_lwing1_vertices = [
   # x   y    r    g    b
    -22,   194,  0.75, 0.0, 0.0,
   -15,  120,  0.75, 0.0, 0.0, 
   -200, 220, 0.75, 0.0, 0.0,
   -160, 240, 0.75, 0.0, 0.0,
   -108, 232, 0.75, 0.0, 0.0,
]
lwing1_vertices = [
    0, 1, 2,
    0, 2, 3,
    0, 3, 4,
]

#Setting the left wing 2
red_lwing2_vertices = [
   # x   y    r    g    b
    -15,   120,  0.5, 0.0, 0.0,
   -200,  220,  0.5, 0.0, 0.0, 
   -180, 120, 0.5, 0.0, 0.0,
]
lwing2_vertices = [
    0, 1, 2,
]

#Setting the left wing 3
red_lwing3_vertices = [
   # x   y    r    g    b
    -15,   120,  0.75, 0.0, 0.0,
   -140,  120,  0.75, 0.0, 0.0, 
   -170, 80, 0.75, 0.0, 0.0,
   -150, 20, 0.75, 0.0, 0.0,
]
lwing3_vertices = [
    0, 1, 2,
    0, 2, 3,
]

#Setting the left wing 4
red_lwing4_vertices = [
   # x   y    r    g    b
    -15,   120,  0.5, 0.0, 0.0,
   -60,  0,  0.5, 0.0, 0.0, 
   -110, -20, 0.5, 0.0, 0.0,
   -150, 20, 0.5, 0.0, 0.0,
]
lwing4_vertices = [
    0, 1, 2,
    0, 2, 3,
]


#Right Side:

#Setting the right wing 1
red_rwing1_vertices = [
   # x   y    r    g    b
    22,   194,  0.75, 0.0, 0.0,
   15,  120,  0.75, 0.0, 0.0, 
   200, 220, 0.75, 0.0, 0.0,
   160, 240, 0.75, 0.0, 0.0,
   108, 232, 0.75, 0.0, 0.0,
]
rwing1_vertices = [
    0, 1, 2,
    0, 2, 3,
    0, 3, 4,
]

#Setting the right wing 2
red_rwing2_vertices = [
   # x   y    r    g    b
    15,   120,  0.5, 0.0, 0.0,
   200,  220,  0.5, 0.0, 0.0, 
   180, 120, 0.5, 0.0, 0.0,
]
rwing2_vertices = [
    0, 1, 2,
]

#Setting the right wing 3
red_rwing3_vertices = [
   # x   y    r    g    b
    15,   120,  0.75, 0.0, 0.0,
   140,  120,  0.75, 0.0, 0.0, 
   170, 80, 0.75, 0.0, 0.0,
   150, 20, 0.75, 0.0, 0.0,
]
rwing3_vertices = [
    0, 1, 2,
    0, 2, 3,
]

#Setting the right wing 4
red_rwing4_vertices = [
   # x   y    r    g    b
    15,   120,  0.5, 0.0, 0.0,
   60,  0,  0.5, 0.0, 0.0, 
   110, -20, 0.5, 0.0, 0.0,
   150, 20, 0.5, 0.0, 0.0,
]
rwing4_vertices = [
    0, 1, 2,
    0, 2, 3,
]

batch = pyglet.graphics.Batch()

###########################

#Create the shapes

#Backgroung:
#Grass
shape_grass = CustomShape2D(
    vertices=green_grass_vertices,
    indices=grass_vertices,
    batch=batch,
)
shape_grass.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Trunk1
shape_trunk1 = CustomShape2D(
    vertices=brown_trunk_vertices,
    indices=trunk_vertices,
    batch=batch,
)
shape_trunk1.position = (WIDTH * 0.5, HEIGHT * 0.5)
shape_trunk1.scale = 3

#Leaf1
shape_leaf1 = CustomShape2D(
    vertices=green_leaf_vertices,
    indices=leaf_vertices,
    batch=batch,
)
shape_leaf1.position = (WIDTH * 0.5, HEIGHT * 0.5)
shape_leaf1.scale = 3

#Trunk2
shape_trunk2 = CustomShape2D(
    vertices=brown_trunk_vertices,
    indices=trunk_vertices,
    batch=batch,
)
shape_trunk2.position = (WIDTH * 0.25, HEIGHT * 0.5)
shape_trunk2.scale = 3.5

#Leaf2
shape_leaf2 = CustomShape2D(
    vertices=green_leaf_vertices,
    indices=leaf_vertices,
    batch=batch,
)
shape_leaf2.position = (WIDTH * 0.25, HEIGHT * 0.5)
shape_leaf2.scale = 3.5

#Trunk3
shape_trunk3 = CustomShape2D(
    vertices=brown_trunk_vertices,
    indices=trunk_vertices,
    batch=batch,
)
shape_trunk3.position = (WIDTH * 0.75, HEIGHT * 0.5)
shape_trunk3.scale = 4

#Leaf3
shape_leaf3 = CustomShape2D(
    vertices=green_leaf_vertices,
    indices=leaf_vertices,
    batch=batch,
)
shape_leaf3.position = (WIDTH * 0.75, HEIGHT * 0.5)
shape_leaf3.scale = 4


#Body1
shape_body1 = CustomShape2D(
    vertices=black_body1_vertices,
    indices=body1_vertices,
    batch=batch,
)
shape_body1.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Body2
shape_body2 = CustomShape2D(
    vertices=gray_body2_vertices,
    indices=body2_vertices,
    batch=batch,
)
shape_body2.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Left side:

#Left Wing1
shape_lwing1 = CustomShape2D(
    vertices=red_lwing1_vertices,
    indices=lwing1_vertices,
    batch=batch,
)
shape_lwing1.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Left Wing2
shape_lwing2 = CustomShape2D(
    vertices=red_lwing2_vertices,
    indices=lwing2_vertices,
    batch=batch,
)
shape_lwing2.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Left Wing3
shape_lwing3 = CustomShape2D(
    vertices=red_lwing3_vertices,
    indices=lwing3_vertices,
    batch=batch,
)
shape_lwing3.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Left Wing4
shape_lwing4 = CustomShape2D(
    vertices=red_lwing4_vertices,
    indices=lwing4_vertices,
    batch=batch,
)
shape_lwing4.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Right side:

#Right Wing1
shape_rwing1 = CustomShape2D(
    vertices=red_rwing1_vertices,
    indices=rwing1_vertices,
    batch=batch,
)
shape_rwing1.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Right Wing2
shape_rwing2 = CustomShape2D(
    vertices=red_rwing2_vertices,
    indices=rwing2_vertices,
    batch=batch,
)
shape_rwing2.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Right Wing3
shape_rwing3 = CustomShape2D(
    vertices=red_rwing3_vertices,
    indices=rwing3_vertices,
    batch=batch,
)
shape_rwing3.position = (WIDTH * 0.5, HEIGHT * 0.5)

#Right Wing4
shape_rwing4 = CustomShape2D(
    vertices=red_rwing4_vertices,
    indices=rwing4_vertices,
    batch=batch,
)
shape_rwing4.position = (WIDTH * 0.5, HEIGHT * 0.5)

#########################

#Move butterfly

def update_figures(dt: float, controller: Controller):
    controller.total_time += dt
    #move all shapes
    shape_body1.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_body2.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_lwing1.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_lwing2.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_lwing3.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_lwing4.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_rwing1.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_rwing2.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_rwing3.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    shape_rwing4.position = WIDTH * 0.5 + 200.0 * cos(controller.total_time), HEIGHT * 0.5 + 120.0 * sin(controller.total_time)
    #scale shapes
    shape_lwing1.scale = 1.0 + 0.25 * sin(controller.total_time * 10)
    shape_lwing2.scale = 1.0 + 0.25 * sin(controller.total_time * 10)
    shape_lwing3.scale = 1.0 + 0.25 * sin(controller.total_time * 10)
    shape_lwing4.scale = 1.0 + 0.25 * sin(controller.total_time * 10)
    shape_rwing1.scale = 1.0 + 0.25 * sin(controller.total_time * 10)
    shape_rwing2.scale = 1.0 + 0.25 * sin(controller.total_time * 10)
    shape_rwing3.scale = 1.0 + 0.25 * sin(controller.total_time * 10)
    shape_rwing4.scale = 1.0 + 0.25 * sin(controller.total_time * 10)

pyglet.clock.schedule(update_figures, controller)

#########################

@controller.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        controller.fillPolygon = not controller.fillPolygon
    elif symbol == pyglet.window.key.ESCAPE:
        controller.close()

@controller.event
def on_draw():
    controller.clear()
    batch.draw()

# Set the view
pyglet.app.run()