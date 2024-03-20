from PySide6.QtWidgets import QApplication
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt
import sys
from OpenGL.GL import glBegin, glEnd, glVertex2f, glClear, GL_QUADS, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_STENCIL, GL_STENCIL_BUFFER_BIT
from OpenGL.GLU import gluPerspective, gluLookAt, gluOrtho2D
from OpenGL.GL import glViewport, glMatrixMode, glLoadIdentity, glTranslatef, glScale, glLight, glClearColor, GL_PROJECTION, GL_MODELVIEW, GL_LINE_STRIP, glColor3f,glVertex3f
import numpy as np
from scipy import fft
from Musique.fft import getFFT
class OpenGLBarWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGLBarWidget, self).__init__(parent)
    
        self.fft_data = getFFT(super(getFFT), 44100, 512, True)  # Dummy FFT data

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, float(w) / h, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        for i in range(50):
            x = i * 0.04 - 1  # Adjust to space bars evenly
            y = 0
            height = 2  # Or dynamically update based on FFT data
            glBegin(GL_QUADS)
            glVertex2f(x, y)
            glVertex2f(x + 0.02, y)
            glVertex2f(x + 0.02, y + height)
            glVertex2f(x, y + height)
            glEnd()
    def draw_fft(self):
        glBegin(GL_LINE_STRIP)
        for i, val in enumerate(self.fft_data):
            x = np.linspace(-1, 1, len(self.fft_data))[i]
            y = val - 0.5
            glColor3f(1.0, val, 0.5)
            glVertex3f(x, y, 0.0)
        glEnd()
