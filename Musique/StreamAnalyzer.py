import numpy as np
import sounddevice as sd
from Musique.fft import getFFT
from scipy.fft import fft
from Musique.StreamReaderPyAudio import Stream_Reader
from Musique.StreamReaderSoundDevice import Stream_Reader as sdReader
class Stream_Analyzer:
    """
    Classe pour analyser le flux audio en temps réel, effectuer une transformation de Fourier (FFT),
    et récupérer les données de fréquence pour la visualisation.
    """

    def __init__(self, device=None, rate=44100, FFT_window_size_ms=50, updates_per_second=100, n_frequency_bins=51):
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
        # Convert 'indata' to a numpy array if it's not already one
        indata = np.array(Stream_Reader.input_device(self.device)) or np.array(Stream_Reader.stream_start(self.device))
        audio_data = np.frombuffer(indata, dtype=np.float32)
        # Apply FFT and store the result
        self.latest_fft_data = np.abs(fft(audio_data))
        """
        Fonction de rappel appelée par le flux d'entrée audio pour traiter les données en temps réel.

        :param indata: Les données audio capturées.
        :param frames: Le nombre de frames dans les données audio.
        :param time: L'horodatage des données audio.
        :param status: Le statut de la capture audio.
        """
        if status:
            print(status)
        # Mise à jour des données FFT en temps réel
        self.fft = np.abs(getFFT(indata[:, 0], self.rate, self.FFT_window_size))
    
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
