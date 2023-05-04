from djitellopy import Tello
from vosk import Model, KaldiRecognizer
import pyaudio

tello = Tello()
tello.connect()

model = Model(r"/Users/mihiretujackson/Documents/GitHub/Contoling-Drone-with-Facial-Recogniton/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()

listening = False

def get_command():
    # global listening
    listening = True
    stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer= 8192)
   
    while listening:
         stream.start_stream()
         try:
              data = stream.read(4096)
              if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    response = result[14:-3]
                    listening = False
                    stream.close()
                    return response
         except OSError:
              pass
def analyze_command(command):
     try:
          if command == "take off":
               tello.takeoff()
          elif command == "land":
               tello.land()
          elif command == "move up":
               tello.move_up(30)
          elif command == "move down":
               tello.move_down(30)
          elif command == "move left":
               tello.move_left(30)
          elif command == "move right":
               tello.move_right(30)
          elif command == "do a flip": 
               tello.flip()
               tello.flip_right()
          else:
               print("I don't understand the command")
     except Exception:
          pass
while True:
     print("waiting for Command")
     command = get_command()
     analyze_command(command)
          
               
               
               



               
               
               

       
                    

              


