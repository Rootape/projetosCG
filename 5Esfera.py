from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def Piramide():

    ang = math.pi / 180
    d = 0.01

    for i in range(0, 100):
        for j in range(0, 360):
            glColor3f(0.8, 0.8, 0.8)
            glBegin(GL_QUADS)
            glVertex3f(math.cos(j * ang), i*d, math.sin(j * ang))
            glVertex3f(math.cos((j+1) * ang), i*d, math.sin((j+1) * ang))
            glVertex3f(math.cos(j * ang), (i+1)*d, math.sin(j * ang))
            glVertex3f(math.cos((j+1) * ang), (i+1)*d, math.sin((j+1) * ang))
            glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()	
