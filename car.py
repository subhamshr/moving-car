from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Global variables for the car animation
bx = 10
def circle(rx, ry, cx, cy):
    glBegin(GL_POLYGON)
    glVertex2f(cx, cy)
    for i in range(361):
        angle = i * math.pi / 180
        x = rx * math.cos(angle)
        y = ry * math.sin(angle)
        glVertex2f(x + cx, y + cy)
    glEnd()
def sun(rx, ry, cx, cy):
    glBegin(GL_POLYGON)
    glVertex2f(cx, cy)
    for i in range(361):
        angle = i * math.pi / 180
        x = rx * math.cos(angle)
        y = ry * math.sin(angle)
        glVertex2f(x + cx, y + cy)
    glEnd()
    
def hills():
    # Hills 1 (Dark Green)
    glColor3ub(0, 100, 0)
    glBegin(GL_POLYGON)
    glVertex2d(-40, 150)  # Adjusted y-coordinate
    glVertex2d(200, 150)  # Adjusted y-coordinate
    glVertex2d(100, 330)  # Adjusted y-coordinate
    glEnd()

    # Hills 2 (Dark Green)
    glColor3ub(0, 128, 0)
    glBegin(GL_POLYGON)
    glVertex2d(150, 150)  # Adjusted y-coordinate
    glVertex2d(350, 150)  # Adjusted y-coordinate
    glVertex2d(250, 330)  # Adjusted y-coordinate
    glEnd()

    # Hills 3 (Dark Green)
    glColor3ub(0, 100, 0)
    glBegin(GL_POLYGON)
    glVertex2d(300, 150)  # Adjusted y-coordinate
    glVertex2d(520, 150)  # Adjusted y-coordinate
    glVertex2d(400, 330)  # Adjusted y-coordinate
    glEnd()


def init():
    glClearColor(0.529, 0.808, 0.922, 0.0)  # Light Blue
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 500, 0.0, 500)  # window size


def display():
    global bx
    glClear(GL_COLOR_BUFFER_BIT)

    # Ground Color (Light Brown)
    glColor3ub(222, 184, 135)
    glBegin(GL_POLYGON)
    glVertex2d(0, 0)
    glVertex2d(500, 0)
    glVertex2d(500, 150)
    glVertex2d(0, 150)
    glEnd()

   # road
    glColor3ub(128, 128, 128)  # Gray color
    glBegin(GL_POLYGON)
    glVertex2d(0, 55)
    glVertex2d(500, 55)
    glVertex2d(500, 115)
    glVertex2d(0, 115)
    glEnd()


    # dashed lines on the road
    glColor3ub(255, 255, 255)  # White color for dashed lines
    glLineWidth(2.0)
    glBegin(GL_LINES)
    for i in range(0, 501, 20):  # Draw dashed lines every 20 units
        glVertex2d(i, 85)
        glVertex2d(i + 10, 85)
    glEnd()

    # hills
    hills()

    # sun design
    glColor3ub(255, 215, 0)
    sun(30, 40, 175, 350)

    glPushMatrix()
    glTranslatef(bx, 0, 0)
#carcolor
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(410, 100)
    glVertex2d(490, 100)
    glVertex2d(485, 130)
    glVertex2d(410, 130)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2d(420, 130)
    glVertex2d(475, 130)
    glVertex2d(465, 160)
    glVertex2d(430, 160)
    glEnd()

    # car window
    glColor3ub(220, 220, 220)
    glBegin(GL_POLYGON)
    glVertex2d(425, 130)
    glVertex2d(445, 130)
    glVertex2d(445, 150)
    glVertex2d(430, 150)
    glEnd()

    # car window
    glColor3ub(220, 220, 220)
    glBegin(GL_POLYGON)
    glVertex2d(450, 130)
    glVertex2d(470, 130)
    glVertex2d(465, 150)
    glVertex2d(450, 150)
    glEnd()

    # car wheel
    glColor3ub(0, 0, 0)
    circle(10, 14, 435, 100)
    circle(10, 14, 465, 100)

    glColor3ub(245, 245, 245)
    circle(6, 10, 435, 100)
    circle(6, 10, 465, 100)
    glPopMatrix()
    bx += 2
    if bx > 0:
        bx = -500
    glutPostRedisplay()
    glFlush()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 600)
    glutInitWindowPosition(300, 50)
    glutCreateWindow(b"A Moving Car Scenario")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
