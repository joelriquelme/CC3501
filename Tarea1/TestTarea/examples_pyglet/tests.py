# coding=utf-8
"""Drawing 4 shapes with different transformations"""

import pyglet
from math import sin, cos
from pyglet_basic_shapes_wrapper import CustomShape2D


class Controller(pyglet.window.Window):

    def __init__(self, width, height, title="Pyglet window"):
        super().__init__(width, height, title)
        self.total_time = 0.0
        self.fillPolygon = True


# We will use the global controller as communication with the callback function
WIDTH, HEIGHT = 800, 600
controller = Controller(width=WIDTH, height=HEIGHT)

# Setting up the clear screen color
pyglet.gl.glClearColor(0, 0.67, 0.894, 1.0)


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


batch = pyglet.graphics.Batch()



shape_quad1 = CustomShape2D(
    vertices=black_body1_vertices,
    indices=body1_vertices,
    batch=batch,
)
shape_quad1.position = (WIDTH * 0.5, HEIGHT * 0.5)

@controller.event
def on_draw():
    controller.clear()
    batch.draw()


# Set the view
pyglet.app.run()



