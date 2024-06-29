from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# initialize the default values
bg = (0.0, 0.0, 0.0, 0.0)
speed = 0.01
point_size = 6
blink = 500
general_radius = 50
point_color = []
random_colors = []
IsBlinkOn = False
IsAnimationOn = True

change_size = False

class Points:
    def __init__(self):
        # coordinate
        self.x = 0
        self.y = 0
        #color
        self.r = 0
        self.g = 0
        self.b = 0
        #acceleration
        self.dx = 0
        self.dy = 0

class color:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0


def draw_points():
    global blink, point_size
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    for c in point_color:
        glColor3f(c.r, c.g, c.b)
        glVertex2f(c.x, c.y)
    glEnd()

def GenRandomBalls(n,x,y):
    global point_color

    for _ in range(n):
        p = Points()

        # random position within 6 radius
        p.x = random.randint(x, x + general_radius)
        p.y = random.randint(y, y + general_radius)

        # random color
        p.r = random.uniform(0, 1)
        p.g = random.uniform(0, 1)
        p.b = random.uniform(0, 1)

        choice = random.randint(1,4)

        if choice == 1:
            p.dx = speed
            p.dy = speed
        elif choice == 2:
            p.dx = - speed
            p.dy = speed
        elif choice == 3:
            p.dx = speed
            p.dy = - speed
        elif choice == 4:
            p.dx = -speed
            p.dy = -speed

        point_color.append(p)

        c = color()
        c.r = p.r
        c.g = p.g
        c.b = p.b
        random_colors.append(c)


def animate():
    global point_color, point_size, change_size, IsAnimationOn

    if not IsAnimationOn:
        return

    # accelarate points based on dx and dy
    n = len(point_color)
    for i in range(n):
        point_color[i].x += point_color[i].dx
        point_color[i].y += point_color[i].dy

        if point_color[i].x > 500 or point_color[i].x < 0 or point_color[i].y > 500 or point_color[i].y < 0:
            point_color[i].dy = point_color[i].dy * (-1)
            point_color[i].dx = point_color[i].dx * (-1)

    if IsBlinkOn:
        if point_size >= 0 and not change_size:
            point_size -= 0.008

        if point_size < 0:
            change_size = True

        if point_size <= point_size and change_size:
            point_size += 0.008

        if point_size > point_size:
            change_size = False

    glutPostRedisplay()


def mousefunc(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    global IsBlinkOn, point_size
    # convert point
    y = 800 - y

    # gen points
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            GenRandomBalls(5, x, y)

    # blink point
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            IsBlinkOn = not IsBlinkOn

            if IsBlinkOn == False:
                point_size = point_size

    glutPostRedisplay()


def specialKeyfunc(key, x, y):
    global ball_col

    if key == GLUT_KEY_UP:
        n = len(ball_col)
        for i in range(n):

            if abs(ball_col[i].dx) >= speed:
                print("Reached Max Speed.")
                break

            ball_col[i].dx *= 1.4
            ball_col[i].dy *= 1.4

    if key == GLUT_KEY_DOWN:
        n = len(ball_col)
        for i in range(n):

            if abs(ball_col[i].dx) <= speed:
                print("Reached Min Speed.")
                break

            ball_col[i].dx /= 1.5
            ball_col[i].dy /= 1.5

    glutPostRedisplay()


def keyboard(key, x, y):
    global IsAnimationOn
    if key == b' ':
        IsAnimationOn = not IsAnimationOn


# Common Part
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
# Set the background color
    glClearColor(*bg)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
# Call the draw points function
    draw_points()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
# Window size
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
# Window name
wind = glutCreateWindow(b"Building Amazing Box")
# Call the functions
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutMouseFunc(mousefunc)
glutSpecialFunc(specialKeyfunc)
glutKeyboardFunc(keyboard)
glutMainLoop()