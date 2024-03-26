from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer
from OpenGL.GL import GL_QUADS, GL_LINES, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_POLYGON, glClear, glLoadIdentity, glColor3f, glClearColor, glBegin, glVertex2f, glEnd, glViewport
from OpenGL.GLU import gluOrtho2D, gluPerspective
import numpy as np
from Musique.StreamReaderPyAudio import Stream_Reader
from Musique.StreamAnalyzer import Stream_Analyzer
from Musique.fft import FFTget  
import time
class OpenGLBarWidget(QOpenGLWidget):
    def __init__(self, parent=None, rate=44800, updates_per_second=60, bar_color=(1.0, 0.0, 0.0)):
        super(OpenGLBarWidget, self).__init__(parent)
        self.stream_reader = Stream_Reader(rate=rate, updates_per_second=updates_per_second)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(60 // updates_per_second)  # Update rate in milliseconds
        self.bar_color = bar_color
        # Initialize additional attributes
        self.start_color = [1.0, 0.0, 0.0]  # Default red
        self.end_color = [0.0, 0.0, 1.0]  # Default blue
        self.bar_width = 0.02  # Default width
        self.sliderValue = 1.0
        self.setUpdatesEnabled(True)
        self.valueRate = 1.0
        
        self.bass_gain = 1.0
        self.mid_gain = 1.0
        self.high_gain = 1.0
        self.visual_opacity = 1.0
        self.scale = 1.0
        self.smoothing = 1.0
        # More attributes for additional sliders
        self.additional_gain_1 = 1.0
        self.additional_gain_2 = 1.0
        self.additional_gain_3 = 1.0
        self.additional_gain_4 = 1.0
        self.additional_gain_5 = 1.0
        self.additional_gain_6 = 1.0
        self.additional_gain_7 = 1.0
        self.additional_gain_8 = 1.0
        self.updates_per_second_and_rate(updates_per_second, rate)
        self.param_3 = 1.0
        self.param_4 = 1.0
        self.param_5 = 1.0
        self.param_6 = 1.0
        self.param_7 = 1.0
        self.param_8 = 1.0
        self.param_9 = 1.0
        self.param_10 = 1.0
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        data = self.stream_reader.read()
        self.fft_data = fft_data = FFTget.getFFT(data, self.stream_reader.rate)
        fft_data = FFTget.getFFT(data, self.stream_reader.rate)
        #fft_data = self.apply_smoothing(fft_data)
        #fft_data = self.apply_gain(fft_data)
        
        # Normalize FFT data
        #fft_data = fft_data / np.max(fft_data)
        

        glClear(int(GL_COLOR_BUFFER_BIT) | int(GL_DEPTH_BUFFER_BIT))
        glLoadIdentity()
        gluOrtho2D(0, 1, 0, 1)

        glColor3f(*self.bar_color)
        bar_width = 1.0 / len(fft_data*2)
        for i, val in enumerate(fft_data):
            glBegin(GL_QUADS)
            glVertex2f(i * bar_width/2, 0)
            glVertex2f(i * bar_width/2, float(val))  # Ensure val is a float
            glVertex2f((i + 1) * bar_width/2, float(val))
            glVertex2f((i + 1) * bar_width/2, 0)
            glEnd()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def closeEvent(self, event):
        self.stream_reader.close()
        event.accept()

    def get_frequency_range(self, rate):
        chunk_size = len(self.fft_data) * 2  # Assume FFT size is double the bar count
        return np.fft.rfftfreq(chunk_size, d=1.0 / rate)

    def set_bass_gain(self, gain):
        self.bass_gain = gain / 50.0
        self.apply_gain(self.fft_data)
        self.update()

    def set_mid_gain(self, gain):
        self.mid_gain = gain / 50.0
        self.apply_gain(self.fft_data)
        self.update()

    def set_high_gain(self, gain):
        self.high_gain = gain / 50.0
        self.apply_gain(self.fft_data)
        self.update()

    def set_visual_opacity(self, opacity):
        self.visual_opacity = opacity / 100.0
        self.update()

    def set_scale(self, scale_value):
        self.scale = scale_value / 100.0
        self.update()
        
    def set_bar_width(self, width):
        self.bar_width = width / 100.0
        self.update()

    def set_smoothing(self, smoothing):
        self.smoothing = smoothing / 100.0
        self.update()

    def set_start_color(self, color):
        self.start_color = color
        self.update()

    def set_end_color(self, color):
        self.end_color = color
        self.update()
        
    def set_slider_value(self, value):
        self.sliderValue = value
        self.update()
    
    def apply_smoothing(self, fft_data):
        # Apply a simple moving average for smoothing
        smoothing_kernel = np.ones(int(self.smoothing)) / self.smoothing
        smoothed_data = np.convolve(fft_data, smoothing_kernel, mode='same')
        smoothed_data *= self.smoothing
        return smoothed_data
    
        

    # In audio_visual.py
    

    def apply_gain(self, fft_data):
        # Adjust the frequency ranges for the gains
        frequencies = np.arange(len(fft_data)) * self.stream_reader.rate / len(fft_data) * 2
        for i, freq in enumerate(frequencies):
            if freq <= 600:  # Bass frequencies
                fft_data[i] *= self.bass_gain
            elif 600 < freq <= 4000:  # Mid frequencies
                fft_data[i] *= self.mid_gain
            elif freq > 4000:  # High frequencies
                fft_data[i] *= self.high_gain
            # Additional gains for each slider
            if i % 8 == 0:
                fft_data[i] *= self.additional_gain_1
            elif i % 8 == 1:
                fft_data[i] *= self.additional_gain_2
            elif i % 8 == 2:
                fft_data[i] *= self.additional_gain_3
            elif i % 8 == 3:
                fft_data[i] *= self.additional_gain_4
            elif i % 8 == 4:
                fft_data[i] *= self.additional_gain_5
            elif i % 8 == 5:
                fft_data[i] *= self.additional_gain_6
            elif i % 8 == 6:
                fft_data[i] *= self.additional_gain_7
            elif i % 8 == 7:
                fft_data[i] *= self.additional_gain_8
        return fft_data
        
    def set_additional_gain_2(self, value):
        self.additional_gain_2 = value
        self.update()

    def set_additional_gain_3(self, value):
        self.additional_gain_3 = value
        self.update()

    def set_additional_gain_4(self, value):
        self.additional_gain_4 = value
        self.update()

    def set_additional_gain_5(self, value):
        self.additional_gain_5 = value
        self.update()

    def set_additional_gain_6(self, value):
        self.additional_gain_6 = value
        self.update()

    def set_additional_gain_7(self, value):
        self.additional_gain_7 = value
        self.update()

    def set_additional_gain_8(self, value):
        self.additional_gain_8 = value
        self.update()
    
    def set_additional_gain_9(self, value):
        self.additional_gain_9 = value
        self.update()
        
    
    # Implementing methods for additional sliders
    
    def set_sample_rate(self, value):
        # Placeholder for changing the sample rate
        # This might need more elaborate handling depending on how the sample rate impacts the Stream_Reader
        valueRate = self.stream_reader.rate * value
        print(f"Sample rate adjusted to: {value}")
        return valueRate
    
    def set_updates_per_second(self, value):
        # Adjust updates per second in real-time
        self.sliderValue = max(1, value)
        print(f"Updates per second adjusted to: {self.set_updates_per_second}")
        return self.sliderValue

    def set_start_color_r(self, value):
        # Adjust the red component of the start color
        self.start_color[0] = value / 255.0

    def set_start_color_g(self, value):
        # Adjust the green component of the start color
        self.start_color[1] = value / 255.0

    def set_start_color_b(self, value):
        # Adjust the blue component of the start color
        self.start_color[2] = value / 255.0
        
    def updates_per_second_and_rate(self, updates_per_second, sample_rate):
        updates_per_second = self.sliderValue*updates_per_second
        sample_rate = self.stream_reader.rate*self.valueRate
        self.set_updates_per_second(updates_per_second)
        self.set_sample_rate(sample_rate)
        self.update()