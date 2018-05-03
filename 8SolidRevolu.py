from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def f(t):
	A = (0,1)
	B = (1,0)
	x = (1-t)*A[0]+t*B[0]
	x = (1-t)*A[1]+t*B[1]
	return (x,y)

def Piramide():

    ang = math.pi / 180
    d = 0.01
    s = 5

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(-10.0, 0.0, 0.0)
    glVertex3f(10.0, 0.0, 0.0)
    glEnd()
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, -10.0, 0.0)
    glVertex3f(0.0, 10.0, 0.0)
    glEnd()
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, -10.0)
    glVertex3f(0.0, 0.0, 10.0)
    glEnd()

    #N = 10
    #for j in range(0, 360, s):
#	glColor3f(j/360.0, j/360.0, 0.8)
#	for i in range(0, N+1):
#		x, y = f(i/(N*1.0))

    for j in range(0, 360, s):
	glColor3f(j/360.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(0.0, 1.0, 0.0 * math.cos(ang * j))
        glVertex3f(0.5 * math.sin(ang * j), 0.5,  0.5 * math.cos(ang * j))
        glVertex3f(0.5 * math.sin(ang * (j+s)), 0.5,  0.5 * math.cos(ang * (j+s)))
        glVertex3f(0.0, 1.0,  0.0 * math.cos(ang * (j+s)))
	glEnd()
        glBegin(GL_QUADS)
        glVertex3f(0.5 * math.sin(ang * j), 0.5,  0.5 * math.cos(ang * j))
        glVertex3f(0.1 * math.sin(ang * j), 0.0,  0.1 * math.cos(ang * j))
        glVertex3f(0.1 * math.sin(ang * (j + s)), 0.0,  0.1 * math.cos(ang * (j+s)))
        glVertex3f(0.5 * math.sin(ang * (j + s)), 0.5, 0.5 *  math.cos(ang * (j+s)))
	glEnd()
        glBegin(GL_QUADS)
        glVertex3f(0.1 * math.sin(ang * j), 0.0,  0.1 * math.cos(ang * j))
        glVertex3f(0.1 * math.sin(ang * j), -1.0,  0.1 * math.cos(ang * j))
        glVertex3f(0.1 * math.sin(ang * (j+s)), -1.0,  0.1 * math.cos(ang * (j+s)))
        glVertex3f(0.1 * math.sin(ang * (j + s)), 0.0,  0.1 * math.cos(ang * (j+s)))
	glEnd()
        glBegin(GL_QUADS)
        glVertex3f(0.1 * math.sin(ang * j), -1.0,  0.1 * math.cos(ang * j))
        glVertex3f(0.0, -1.0,  0.0 * math.cos(ang * j))
        glVertex3f(0.0, -1.0,  0.0 * math.cos(ang * (j+s)))
        glVertex3f(0.1 * math.sin(ang * (j + s)), -1.0,  0.1 * math.cos(ang * (j+s)))
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
