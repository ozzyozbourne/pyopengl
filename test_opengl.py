import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
screen = pygame.display.set_mode((1000, 800), DOUBLEBUF | OPENGL)
pygame.display.set_caption("test opengl")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
