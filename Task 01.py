from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# initialize the default view
bg = (0.0, 0.0, 0.0, 0.0)
raindrop_angle = 0.0
raindrop_arr = []

# Task 1 (i)
  ## Draw Raindrop
def raindrop(x1, y1):
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    glEnd()
def rain_drops():
    global raindrop_angle
    for rain in range(0, len(raindrop_arr)):
        new_x, new_y = raindrop_arr[rain]
        # update the raindrop coordinate
        new_x += raindrop_angle
        new_y -= 1
        # avoid the raindrop entering the house
        if (new_y < 250) or (120 < new_x < 380 and 100 < new_y < 300):
            new_x = random.uniform(100, 400)
            new_y = random.uniform(200, 500)
        raindrop_arr[rain] = (new_x, new_y)

 ## Draw House
def draw_house():
    # Red Colour House
    glColor3f(1.0,0.0,0.0)

    # Drawing Roof
    glBegin(GL_TRIANGLES)
    # Roof -> (Triangle - 3 points)
       ## Triangle Top Point
    glVertex2f(250, 400)
       ## Triangle Bottom Right Point
    glVertex2f(400, 300)
       ## Triangle Bottom Right Point
    glVertex2f(100, 300)
    glEnd()

    # Drawing body
    glPointSize(5)
    glLineWidth(1)
    glBegin(GL_LINES)
       ## Top Left
    glVertex2f(120, 300)
    glVertex2f(120, 100)
       ## Bottom
    glVertex2f(120, 100)
    glVertex2f(380, 100)
       ## Top Right
    glVertex2f(380, 100)
    glVertex2f(380, 300)
    glEnd()

    # Drawing door
    glPointSize(5)
    glLineWidth(2)
    glBegin(GL_LINES)
     # Left side
    glVertex2f(150,100)
    glVertex2f(150, 200)
     # Top line
    glVertex2f(150, 200)
    glVertex2f(200, 200)
    # Right side
    glVertex2f(200, 200)
    glVertex2f(200, 100)
    glEnd()

    # Drawing door lock
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(190, 145)
    glEnd()

    # Drawing window
    glPointSize(5)
    glLineWidth(2)
    glBegin(GL_LINES)
     ## Bottom to top
    glVertex2f(350, 200)
    glVertex2f(350, 250)
     ## Bottom line
    glVertex2f(350, 200)
    glVertex2f(300, 200)
     ## Again Bottom to top
    glVertex2f(300, 200)
    glVertex2f(300, 250)
     ## Top line
    glVertex2f(300, 250)
    glVertex2f(350, 250)
     ## Vertical Divider
    glVertex2f(325, 200)
    glVertex2f(325, 250)
     ## Horizontal Divider
    glVertex2f(300, 225)
    glVertex2f(350, 225)
    glEnd()

def animation():
    rain_drops()
    glutPostRedisplay()


# Task 1 (ii)
def specialKeyListener(key, x,y):
    global raindrop_angle
    if key == GLUT_KEY_RIGHT:
        raindrop_angle += 0.5
        print("Bending to the Right")
    if key == GLUT_KEY_LEFT:
        raindrop_angle -= 0.5
        print("Bending to the Left")
    glutPostRedisplay()


# Task 1 (iii)
def keyboardListener(key, x,y):
    global bg
    if key == b'd':
        bg = (0.0, 0.0, 0.0, 0.0)
        print("It's Night Time. Dark Theme Enabled!")
    if key == b'l':
        bg = (1.0, 1.0, 1.0, 1.0)
        print("It's Day Time. Light Theme Enabled!")
    glutPostRedisplay()


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
# Call the draw house function
    draw_house()
# Call the raindrop function
    for i in raindrop_arr:
        raindrop(i[0], i[1])
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Window Size
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)

# Window Name
wind = glutCreateWindow(b"Raindrop over a house for whole day")

# Call all the functions
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutIdleFunc(animation)
glutSpecialFunc(specialKeyListener)

# At First we get random raindrop coordinate in raindrop_arr
for drop in range(100):
    x2 = random.uniform(00, 500)
    y2 = random.uniform(00, 500)
    raindrop_arr.append((x2, y2))
glutMainLoop()
