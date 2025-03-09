from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

akash_tumi = 0.3
bristir_beg = 250
angle = 0
#background

def prokriti():
    global akash_tumi
    #akash tumi nil
    glBegin(GL_TRIANGLES)
    glColor3f(akash_tumi,akash_tumi,2*akash_tumi)
    glVertex2d(-256,30)
    glVertex2d(256,256)
    glVertex2d(-256,256)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(akash_tumi,akash_tumi,2*akash_tumi)
    glVertex2d(256,30)
    glVertex2d(256,256)
    glVertex2d(-256,256)
    glEnd()

    #gach lagan poribesh bachan
    glBegin(GL_TRIANGLES)
    glColor3f(.05,4,.06)
    glVertex2d(0,95)
    glVertex2d(-40,60)
    glVertex2d(40,60)
    glEnd()

    glPointSize(20)
    glBegin(GL_POINTS)
    glColor3f(.04,.2,.04)
    glVertex2f(0,50)
    glEnd()
    

    #ghor
    glBegin(GL_TRIANGLES)
    glColor3f(.5,0.5, .5)
    glVertex2d(-125,0)
    glVertex2d(-75,50)
    glVertex2d(75,50)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(.5,0.5, .5)
    glVertex2d(125,0)
    glVertex2d(75,50)
    glVertex2d(-125,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(.9,0.6, .1)
    glVertex2d(-90,0)
    glVertex2d(-90,-80)
    glVertex2d(90,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(.9,0.6, .1)
    glVertex2d(90,0)
    glVertex2d(-90,-80)
    glVertex2d(90,-80)
    glEnd()

    #dorja
    glBegin(GL_TRIANGLES)
    glColor3f(0,0, 0)
    glVertex2d(-20,-20)
    glVertex2d(-20,-80)
    glVertex2d(20,-20)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2,0.2,0.2)
    glVertex2d(-20,-80)
    glVertex2d(20,-80)
    glVertex2d(20,-20)
    glEnd()

    #janala
    glPointSize(20)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2f(45,-40)
 
    glEnd()

    glPointSize(20)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2f(-45,-40)
 
    glEnd()

    #poitha
    glBegin(GL_TRIANGLES)
    glColor3f(0,0,0)
    glVertex2d(-90,-80)
    glVertex2d(-95,-85)
    glVertex2d(90,-80)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0,0,0)
    glVertex2d(95,-85)
    glVertex2d(90,-80)
    glVertex2d(-95,-85)
    glEnd()



def keyboardListener(key, x, y):
    global akash_tumi
    if key== b'd':
        akash_tumi+=0.05
        if akash_tumi>.5:
            akash_tumi = .5
        print("Increase Light")

    if key==b'n':
        akash_tumi-=0.05
        print("Decrease Light")

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global angle
    if key==GLUT_KEY_RIGHT:
        angle+=.5
        if angle>0:
            print('bam dike chata dhoro')
        
    if key==GLUT_KEY_LEFT:
        angle-=.5
        if angle<0:
            print('dan dike chata dhoro')

    glutPostRedisplay()
 

def aybristijhepe():
    global bristir_beg,angle
    for i in range(50):  
        glColor3f(0.09, .09, .80)
        glLineWidth(2)
        glBegin(GL_LINES)
        x_offset = random.uniform(-250, 250)
        bristir_beg = random.uniform(-250, 250)
        glVertex2f(x_offset, bristir_beg)
        glVertex2f(x_offset+angle, bristir_beg - 30)
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(.7,.6,.4,.5);	
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)  
    prokriti()
    aybristijhepe()
    glutSwapBuffers()

def animate():
    glutPostRedisplay()
    
def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)
   

glutInit()
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) 
wind = glutCreateWindow(b"GURU GHOR BANAISI OPENGL DIA")
init()  
glutDisplayFunc(display)	
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()		

