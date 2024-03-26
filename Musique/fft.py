import numpy as np
# Importation de NumPy pour les opérations mathématiques et de tableau.

class FFTget:
    @staticmethod
    def getFFT(data, rate):
        # Définition d'une méthode statique pour calculer la transformée de Fourier rapide (FFT).

        data = np.array(data, dtype='float', ndmin=2)
        # Conversion des données en un tableau numpy de type float.

        fft_data = np.abs(np.fft.rfft(data))
        # Calcul de la FFT et prise de la valeur absolue pour obtenir la magnitude.

        return fft_data
        # Retourne les données FFT.