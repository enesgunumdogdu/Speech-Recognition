import tkinter as tk
import speech_recognition as sr


window = tk.Tk()
window.title("Speech Recognition")
window.geometry("600x600")
window.configure(bg='black')

label = tk.Label(window, text="Say something:", bg='black', fg='white')
label.pack(pady=10)

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        print("Detected word: " + text)
        
        if "stop" in text.lower():
            label.config(text="Stop")
            
    except sr.UnknownValueError:
        label.config(text="Could not understand audio")
    except sr.RequestError as e:
        label.config(text="Google Speech Recognition service error; {0}".format(e))

listen_button = tk.Button(window, text="Speak", bg='blue', fg='white', command=listen)
listen_button.pack(pady=10)

window.mainloop()
