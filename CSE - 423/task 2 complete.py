from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

speed = 0.04
blink = False
stop = False
points = []
blink_cycle = 1.0
blink_off_duration = 0.2

def coordinate(x, y):
    return x-250,250-y

def born_dots(x, y):
    direction = random.choice([(-1, 1), (-1, -1), (1, 1), (1, -1)])
    return {'x': x, 'y': y, 'dirx': direction[0], 'diry': direction[1]}

def draw_dots():
    global points
    glPointSize(10)
    glBegin(GL_POINTS)
    for i in points:
        glColor3f(random.random(), random.random(), random.random())
        glVertex2f(i['x'], i['y'])
    glEnd()

def draw_boarder():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(-250, -250)
    glVertex2f(250, -250)

    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(250, -250)
    glVertex2f(250, 250)

    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(250, 250)
    glVertex2f(-250, 250)

    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(-250, 250)
    glVertex2f(-250, -250)

    glEnd()

def draw_triangles():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(-245, -245)
    glVertex2f(245, 245)
    glVertex2f(-245, 245)

    glVertex2f(245, 245)
    glVertex2f(-245, -245)
    glVertex2f(245, -245)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if blink==True and (time.time() % blink_cycle) < blink_off_duration: #@help from gpt and google
        draw_triangles()
        draw_boarder()

    else:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
        draw_boarder()
        draw_dots()

    glutSwapBuffers()

def animate():
    global speed, stop

    if stop == True:
        return

    for i in points:
        i['x'] += i['dirx'] * speed
        i['y'] += i['diry'] * speed

        if i['x'] <= -250 or i['x'] >= 250:
            i['dirx'] = -i['dirx']
        if i['y'] <= -250 or i['y'] >= 250:
            i['diry'] = -i['diry']

    glutPostRedisplay()


def idur_input(click, state, x, y):
    global points, blink, stop
    if stop:
        return
    if click == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if -500 < x < 500 and -500 < y < 500:
            C_x, C_y = coordinate(x, y)
            p = born_dots(C_x, C_y)
            points.append(p)

    elif click == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        blink = not blink

def freeze(key, x, y):
    global stop
    if key == b' ':
        stop = not stop

def speed_key(key, x, y):
    global speed, stop
    if stop:
        return
    if key == GLUT_KEY_UP:
        speed += 0.01 
    elif key == GLUT_KEY_DOWN:
        speed -= 0.01 

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(500,500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"ball r ball")
init()
glutDisplayFunc(display)
glutIdleFunc(animate)
glutMouseFunc(idur_input)
glutKeyboardFunc(freeze)
glutSpecialFunc(speed_key)
glutMainLoop()