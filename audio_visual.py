import sys
import numpy as np
import pyaudio
from scipy.fftpack import fft
from PySide6.QtWidgets import QMainWindow, QApplication
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class RealTimeAudioVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_audio_stream()
        self.init_ui()

    def init_audio_stream(self):
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 44100
        self.chunk_size = 1024
        self.audio_stream = pyaudio.PyAudio().open(format=self.audio_format, channels=self.channels,
                                                   rate=self.sample_rate, input=True, frames_per_buffer=self.chunk_size)

    def init_ui(self):
        fig = Figure()
        self.canvas = FigureCanvas(fig)
        self.setCentralWidget(self.canvas)

        self.audio_ax = fig.add_subplot(211)
        self.spectrogram_ax = fig.add_subplot(212)

        self.x_audio = np.arange(0, 2 * self.chunk_size, 2)
        self.y_audio = np.zeros(self.chunk_size)
        self.line, = self.audio_ax.plot(self.x_audio, self.y_audio)

        self.audio_ax.set_xlim(0, self.chunk_size)
        self.audio_ax.set_ylim(-2 ** 15, 2 ** 15)

        self.timer = self.canvas.new_timer(50)
        self.timer.add_callback(self.update_plot)
        self.timer.start()

    def update_plot(self):
        audio_data = np.frombuffer(self.audio_stream.read(self.chunk_size), np.int16)
        self.line.set_ydata(audio_data)

        self.y_audio = np.append(self.y_audio, audio_data)
        self.y_audio = self.y_audio[-self.chunk_size:]

        fft_data = np.abs(fft(audio_data))[:self.chunk_size // 2]
        self.spectrogram_ax.clear()
        self.spectrogram_ax.plot(fft_data)

        self.canvas.draw()

    def closeEvent(self, event):
        self.timer.stop()
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        pyaudio.PyAudio().terminate()
        super().closeEvent(event)


app = QApplication(sys.argv)
main_window = RealTimeAudioVisualizer()
main_window.show()
sys.exit(app.exec())
