from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pyaudio


class AudioVisual(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        self.x = np.arange(0, 2 * np.pi, 0.01)
        self.line, = self.axes.plot(self.x, np.sin(self.x))

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=1024)

    def update_plot(self):
        # This method needs to be connected to a timer or called periodically
        data = np.frombuffer(self.stream.read(1024), dtype=np.int16)
        self.line.set_ydata(np.sin(self.x))  # Update the data.
        self.draw()
