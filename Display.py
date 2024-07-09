import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Object:
    def __init__(self, verticies, edges):
        self.verticies = verticies
        self.edges = edges

    def render_object(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()

verticies_cube = ((1, -1, -1),(1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, 1),(1, 1, 1),(-1, -1, 1),(-1, 1, 1))
edges_cube = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))

verticies_prism = ((1, 0, -1),(-1, 0, -1),(0, 1, -1),(1, 0, 1),(-1, 0, 1),(0, 1, 1))
edges_prism = ((0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5))

verticies_pyramid = ((1, 1, 0),(1, -1, 0),(-1, -1, 0),(-1, 1, 0),(0, 0, 1))
edges_pyramid = ((0,1),(0,3),(0,4),(1,2),(1,4),(2,4),(2,3),(3,4))

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    glRotatef(180, 10, 10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

                    cube = Object(verticies_cube, edges_cube)
                    cube.render_object()
                    
                    pygame.display.flip()
                    pygame.time.wait(10)

                if event.key == pygame.K_2:
                    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

                    prism = Object(verticies_prism, edges_prism)
                    prism.render_object()
             
                    pygame.display.flip()
                    pygame.time.wait(10)

                if event.key == pygame.K_3:
                    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

                    pyramid = Object(verticies_pyramid, edges_pyramid)
                    pyramid.render_object()


                    pygame.display.flip()
                    pygame.time.wait(10)

if __name__  == "__main__":
    main()
