from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r"/Users/mihiretujackson/Documents/GitHub/Contoling-Drone-with-Facial-Recogniton/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()

stream = mic()