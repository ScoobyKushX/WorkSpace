# OpenGLVisualizer.py

from PySide6.QtOpenGLWidgets import QOpenGLWidget
import numpy as np
from OpenGL.GL import (glBegin, glEnd, glVertex3f, glColor3f, glLoadIdentity,
                       glTranslatef, glClear, glClearColor, glViewport,
                       glMatrixMode, gluPerspective, GL_LINE_STRIP,
                       GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT,
                       GL_PROJECTION, GL_MODELVIEW)

class OpenGLVisualizer(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGLVisualizer, self).__init__(parent)
        self.fft_data = np.random.rand(512)  # Dummy FFT data

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, float(w) / h, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)
        self.draw_fft()

    def draw_fft(self):
        glBegin(GL_LINE_STRIP)
        for i, val in enumerate(self.fft_data):
            x = np.linspace(-1, 1, len(self.fft_data))[i]
            y = val - 0.5
            glColor3f(1.0, val, 0.5)
            glVertex3f(x, y, 0.0)
        glEnd()
