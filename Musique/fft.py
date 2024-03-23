
import numpy as np

class FFTget:
    @staticmethod
    def getFFT(data, rate):
        data = np.array(data, dtype='float')
        fft_data = np.abs(np.fft.rfft(data))
        fft_data /= np.max(fft_data)  # Normalize
        return fft_data
