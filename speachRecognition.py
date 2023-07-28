# from vosk import Model, KaldiRecognizer
# import pyaudio

# model = Model(r"/Users/mihiretujackson/Documents/GitHub/Contoling-Drone-with-Facial-Recogniton/vosk-model-small-en-us-0.15")
# recognizer = KaldiRecognizer(model,16000)

# mic = pyaudio.PyAudio()

# stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer= 8192)
# stream.start_stream()

# while True:
#     data = stream.read(4096)
   
#     if recognizer.AcceptWaveform(data):
#         text = recognizer.Result()
#         print(text)
#         print(text[14:-3])
#         if "Sleep" in text:
#             break

   
from vosk import Model, KaldiRecognizer
import pyaudio
import pyautogui

model = Model(r"/Users/mihiretujackson/Documents/GitHub/Contoling-Drone-with-Facial-Recogniton/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()

stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        command = result[result.find('"text"') + 8 : result.find('"text"') + result[result.find('"text"') + 8:].find('"')]
        command = command.lower()
        print("Command:", command)
        
        if "scroll up" in command:
            pyautogui.scroll(1)  # Scroll up
        elif "scroll down" in command:
            pyautogui.scroll(-1)  # Scroll down
        
        if "sleep" in command:
            break

stream.stop_stream()
stream.close()
mic.terminate()



