from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer
from OpenGL.GL import GL_QUADS, GL_LINES, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_POLYGON, glClear, glLoadIdentity, glColor3f, glClearColor, glBegin, glVertex2f, glEnd, glViewport
from OpenGL.GLU import gluOrtho2D, gluPerspective
import numpy as np
from Musique.StreamReaderPyAudio import Stream_Reader
from Musique.StreamAnalyzer import Stream_Analyzer
from Musique.fft import FFTget  
class OpenGLBarWidget(QOpenGLWidget):
    def __init__(self, parent=None, rate=44800, updates_per_second=100, bar_color=(1.0, 0.0, 0.0)):
        super(OpenGLBarWidget, self).__init__(parent)
        self.stream_reader = Stream_Reader(rate=rate, updates_per_second=updates_per_second)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 // updates_per_second)  # Update rate in milliseconds
        self.bar_color = bar_color

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        data = self.stream_reader.read()
        fft_data = FFTget.getFFT(data, self.stream_reader.rate)

        glClear(int(GL_COLOR_BUFFER_BIT) | int(GL_DEPTH_BUFFER_BIT))
        glLoadIdentity()
        gluOrtho2D(0, 1, 0, 1)

        glColor3f(*self.bar_color)
        bar_width = 1.0 / len(fft_data*2)
        for i, val in enumerate(fft_data):
            glBegin(GL_QUADS)
            glVertex2f(i * bar_width, 0)
            glVertex2f(i * bar_width, val)
            glVertex2f((i + 1) * bar_width, val)
            glVertex2f((i + 1) * bar_width, 0)
            glEnd()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def closeEvent(self, event):
        self.stream_reader.close()
        event.accept()

    def get_frequency_range(self, rate):
        chunk_size = len(self.fft_data) * 2  # Assume FFT size is double the bar count
        return np.fft.rfftfreq(chunk_size, d=1.0 / rate)

    def set_bass_gain(self, gain): self.bass_gain = gain
    def set_mid_gain(self, gain): self.mid_gain = gain
    def set_high_gain(self, gain): self.high_gain = gain
    def set_visual_opacity(self, opacity): self.visual_opacity = opacity
    def set_start_color(self, r, g, b): self.start_color = [r, g, b]
    def set_end_color(self, r, g, b): self.end_color = [r, g, b]
    def set_bar_width(self, width): self.bar_width = width
    def set_scale(self, scale): self.scale = scale