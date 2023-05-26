
# from vosk import Model, KaldiRecognizer
# import pyaudio
# import webbrowser

# model = Model(r"/Users/mihiretujackson/Documents/GitHub/Contoling-Drone-with-Facial-Recogniton/vosk-model-small-en-us-0.15")
# recognizer = KaldiRecognizer(model,16000)

# mic = pyaudio.PyAudio()
# stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer= 8192)
# stream.start_stream()

# while True:
#     data = stream.read(4096)
#     if recognizer.AcceptWaveform(data):
#         text = recognizer.Result()
#         command = text[14:-3]
#         print(command)
        
#         # Check for website navigation commands
#         if "open" in command:
#             website = command.split()[-1]
#             webbrowser.open_new_tab('https://www.'+website+'.com')
#             print("Opening website " + website)
        
#         # Check for search command
#         elif "search" in command:
#             query = command.split("search ")[-1]
#             query = query.replace(" ", "+")
#             url = f"https://www.google.com/search?q={query}"
#             webbrowser.open_new_tab(url)
#             print(f"Searching for {query}...")
        
#         # Check for exit command
#         elif "sleep" in command:
#             print("Exiting...")
#             break

# from vosk import Model, KaldiRecognizer
# import pyaudio
# import webbrowser

# model = Model(r"/Users/mihiretujackson/Documents/GitHub/Contoling-Drone-with-Facial-Recogniton/vosk-model-small-en-us-0.15")
# recognizer = KaldiRecognizer(model,16000)

# mic = pyaudio.PyAudio()
# stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer= 8192)
# stream.start_stream()

# print("Hi, how can i help you?")
# while True:
#     data = stream.read(4096)
#     if recognizer.AcceptWaveform(data):
#         text = recognizer.Result()
#         command = text[14:-3]
#         print(command)
        
#         # Check for website navigation commands
#         if "open" in command:
#             website = command.split()[-1]
#             webbrowser.open_new_tab('https://www.'+website+'.com')
#             print("Opening website " + website)
        
#         # Check for search command
#         elif "search" in command:
#             query = command.split("search ")[-1]
#             query = query.replace(" ", "+")
#             url = f"https://www.google.com/search?q={query}"
#             webbrowser.open_new_tab(url)
#             print(f"Searching for {query}...")
        
#         # Check for exit command
#         elif "sleep" in command:
#             print("Exiting...")
#             break
from vosk import Model, KaldiRecognizer
import pyaudio
import webbrowser

model = Model(r"/Users/mihiretujackson/Documents/GitHub/Contoling-Drone-with-Facial-Recogniton/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()
stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer= 8192)
stream.start_stream()

print("Hi, how can I help you?")

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        command = text[14:-3]
        print(command)
        
        # Check for website navigation commands
        if "open" in command:
            website = command.split()[-1]
            webbrowser.open_new_tab('https://www.'+website+'.com')
            print("Opening website " + website)
        
        # Check for search command
        elif "search" in command:
            query = command.split("search ")[-1]
            query = query.replace(" ", "+")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open_new_tab(url)
            print(f"Searching for {query}...")
        
        # Check for exit command
        elif "sleep" in command:
            print("Exiting...")
            break
        
        # Check for code command
        elif "code" in command:
            language = command.split("in ")[-1]
            if language == "python":
                response = "Here's an example of Python code: print('Hello, world!')"
            elif language == "java":
                response = "Here's an example of Java code: System.out.println('Hello, world!');"
            else:
                response = "Sorry, I don't have any examples of that programming language."
            print(response)
