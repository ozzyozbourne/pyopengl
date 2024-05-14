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
    gluOrtho2D(0, 1000, 0, 800)


def draw_star(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glVertex2i(x, y)
    glEnd()

done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_star(231, 151, 20)
    draw_star(257, 253, 20)
    draw_star(303, 180, 15)
    draw_star(443, 228, 15)
    draw_star(435, 287, 10)
    draw_star(385, 315, 20)

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
