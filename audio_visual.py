from PySide6.QtWidgets import QApplication
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt, QTimer
import sys
from OpenGL.GL import glBegin, glEnd, glVertex2f, glClear, GL_QUADS, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_STENCIL, GL_STENCIL_BUFFER_BIT
from OpenGL.GLU import gluPerspective, gluLookAt, gluOrtho2D
from OpenGL.GL import glViewport, glMatrixMode, glLoadIdentity, glTranslatef, glScale, glLight, glClearColor, GL_PROJECTION, GL_MODELVIEW, GL_LINE_STRIP, glColor3f,glVertex3f
import numpy as np
from scipy import fft
from Musique.StreamAnalyzer import Stream_Analyzer
from Musique.StreamReaderPyAudio import Stream_Reader
from Musique.fft import getFFT


class OpenGLBarWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGLBarWidget, self).__init__(parent)
        self.analyzer = Stream_Analyzer()
        # Assume we have a mechanism to start the audio stream and call `audio_callback`
        self.fft_data = self.analyzer.get_latest_fft_data()
        self.analyzer.audio_callback(self.fft_data, 1024, 1, True)
        self.initializeGL()
        self.resizeGL(self.width(), self.height())
        self.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateGeometry)
        self.timer.start(1)
        
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
        if self.fft_data is not None:
            for i, val in enumerate(self.fft_data[:50]):  # Assuming you want to display the first 50 FFT values
                x = i * 0.04 - 1
                y = 0
                height = val  # Scale this value based on your visualization needs
                glBegin(GL_QUADS)
                glVertex2f(x, y)
                glVertex2f(x + 0.02, y)
                glVertex2f(x + 0.02, y + height)
                glVertex2f(x, y + height)
                glEnd()

