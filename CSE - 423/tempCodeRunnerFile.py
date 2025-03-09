from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500
speed = 0.03
blink = False
stop = False
points = []

def coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def born_dots(x, y):
    way = random.choice([(-1, 1), (-1, -1), (1, 1), (1, -1)] )
    return {'x': x, 'y': y, 'dx': way[0], 'dy': way[1]}
    

def draw_dots():
    global points, blink
    glPointSize(10)
    glBegin(GL_POINTS)
    for i in points:
        if blink ==False: 
            glColor3f([random.random(), random.random(), random.random()])
            glVertex2f(i['x'], i['y'])
    glEnd()

def drawBoarder():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(-250,-250)
    glVertex2f(+250,-250)

    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(+250,-250)
    glVertex2f(250,250)

    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(250,250)
    glVertex2f(-250,250)

    glColor3f(0.5, 0.7, 1.0)
    glVertex2f(-250,250)
    glVertex2f(-250,-250)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    drawBoarder()
    draw_dots()
    glutSwapBuffers()

def animate():
    global speed, blink, stop

    if stop==True:
        return

    for point in points:
        point['x'] += point['dx'] * speed
        point['y'] += point['dy'] * speed

        if point['x'] <= -W_Width / 2 or point['x'] >= W_Width / 2:
            point['dx'] = -point['dx']
        if point['y'] <= -W_Height / 2 or point['y'] >= W_Height / 2:
            point['dy'] = -point['dy']

    

    glutPostRedisplay()

def idur_input(click, set, x, y):
    global points, blink, stop
    if stop:
        return
    if click == GLUT_RIGHT_BUTTON and set == GLUT_DOWN:
        if -W_Width < x and x < W_Width and -W_Height < y and y < W_Height:
            C_x, C_y = coordinate(x, y)
            p = born_dots(C_x, C_y)
            points.append(p)

    elif click == GLUT_LEFT_BUTTON and set == GLUT_DOWN:
        if blink == True:
            blink = False
        else:
            blink = True

def freeze(space, x, y):
    global stop
    if space == b' ':  
        stop = not stop

def speed_key(butn, x, y):
    global speed, stop
    if stop:
        return
    if butn == GLUT_KEY_UP:
        speed += 0.01 
    elif butn == GLUT_KEY_DOWN:
        speed -= 0.01 

def init():
    glClearColor(0, 0, 0, 0)  
    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity() 
    gluPerspective(104, 1, 1, 1000.0)  

glutInit()
glutInitWindowSize(W_Width, W_Height)
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