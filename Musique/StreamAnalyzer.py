import numpy as np
"""
    The code defines a class `Stream_Analyzer` in Python for real-time audio stream analysis using Fast
    Fourier Transform (FFT) with methods to capture and process audio data.
    
    :param f: Here's a brief explanation of the parameters used in the `Stream_Analyzer` class:
    :return: The `round_up_to_even` function returns the next highest even number after rounding up the
    input number `f`.
    """
import sounddevice as sd
from Musique.fft import FFTget
from scipy.fft import fft
from Musique.StreamReaderPyAudio import Stream_Reader
from Musique.StreamReaderSoundDevice import Stream_Reader as sdReader
class Stream_Analyzer:
    """
    Classe pour analyser le flux audio en temps réel, effectuer une transformation de Fourier (FFT),
    et récupérer les données de fréquence pour la visualisation.
    """

    def __init__(self, device=None, rate=44100, FFT_window_size_ms=50, updates_per_second=100, n_frequency_bins=102):
        """
        Initialisation de l'analyseur de flux audio.

        :param device: ID du périphérique audio à utiliser.
        :param rate: Taux d'échantillonnage pour l'enregistrement audio.
        :param FFT_window_size_ms: Taille de la fenêtre pour la FFT en millisecondes.
        :param updates_per_second: Nombre de mises à jour par seconde.
        :param n_frequency_bins: Nombre de bins de fréquence à utiliser pour l'analyse.
        """
        self.latest_fft_data = None

        self.device = device
        self.rate = rate
        self.updates_per_second = updates_per_second
        self.n_frequency_bins = n_frequency_bins
        self.FFT_window_size = round_up_to_even(self.rate * FFT_window_size_ms / 1000)
        self.fft = np.zeros(int(self.FFT_window_size/2))

        # Démarrage du flux d'entrée pour la capture audio
        self.stream = sd.InputStream(device=self.device, channels=1, samplerate=self.rate, callback=self.audio_callback)
        self.stream.start()

    def audio_callback(self, indata, frames, time, status):
    # Affiche le statut si une erreur est signalée
        if status:
            print(status)

        # Traite les données seulement si 'indata' n'est pas None
        if indata is not None:
            # Applique la FFT et stocke le résultat dans `latest_fft_data`
            fft_instance = FFTget()
            self.latest_fft_data = np.abs(fft_instance.getFFT(indata, self.rate))
# Mise à jour des données FFT en temps réel
            
        else:
            # Gérer le cas où 'indata' est None si nécessaire
            print("Aucune donnée audio reçue.")

    def get_latest_fft_data(self):
        return self.latest_fft_data
    
    def get_frequency_bins(self):
        """
        Récupère les valeurs actuelles de la FFT pour chaque bin de fréquence.

        :return: Les valeurs de la FFT pour chaque bin de fréquence.
        """
        # Calcule les indices pour chaque bin de fréquence
        freq_bins = np.linspace(0, self.rate / 2, num=len(self.fft), endpoint=True)
        return self.fft

    def stop(self):
        """
        Arrête le flux audio et ferme la connexion.
        """
        self.stream.stop()
        self.stream.close()

def round_up_to_even(f):
    """
    Arrondit un nombre au prochain nombre pair le plus élevé.

    :param f: Le nombre à arrondir.
    :return: Le prochain nombre pair le plus élevé.
    """
    return np.ceil(f / 2.) * 2
