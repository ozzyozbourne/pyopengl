import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

dimension = (1000, 800)
done = False

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -400, 400)

def plot_graph():
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glEnd()

def init_pygame():
    pg.init()
    screen =  pg.display.set_mode(dimension, DOUBLEBUF | OPENGL)
    pg.display.set_caption('Graphics in PyOpenGL')
    return screen

def refresh():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pg.display.flip()
    pg.time.wait(100)

init_pygame()
init_ortho()
glPointSize(10)
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    refresh()


pg.quit()

