import numpy as np
import pyaudio as pa
import time
from collections import deque

from scipy import fft, misc

from Musique.utils import numpy_data_buffer, round_up_to_even

class Stream_Reader:
    def __init__(self, device=None, rate=44100, updates_per_second=10, FFT_window_size=None, verbose=False):
        self.pa = pa.PyAudio()
        self.rate = rate
        self.verbose = verbose
        self.device = device if device is not None else self.pa.get_default_input_device_info()['index']
        self.update_window_n_frames = round_up_to_even(self.rate / updates_per_second)
        self.stream = self.pa.open(format=pa.paFloat32, channels=1, rate=self.rate,
                                   input=True, frames_per_buffer=self.update_window_n_frames, 
                                   input_device_index=self.device)
        if self.verbose:
            print(f'Recording at {self.rate} Hz')

    def read(self):
        data = self.stream.read(self.update_window_n_frames, exception_on_overflow=False)
        return np.fromstring(data, dtype=np.float32)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()