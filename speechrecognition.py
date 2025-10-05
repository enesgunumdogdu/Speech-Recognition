import tkinter as tk
import speech_recognition as sr



window = tk.Tk()
window.title("Speech Recognition")
window.geometry("600x600")
window.configure(bg='black')

label = tk.Label(window, text="Bir şey söyleyin:", bg='black', fg='white')
label.pack(pady=10)

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language='tr-TR')
        print("Algılanan kelime: " + text)
        
        if "dur" in text.lower():
            label.config(text="Dur")
            
    except sr.UnknownValueError:
        label.config(text="Ses anlaşılamadı")
    except sr.RequestError as e:
        label.config(text="Google Ses Tanıma servisi çalışmıyor; {0}".format(e))

dinlebutonu = tk.Button(window, text="Konuş", bg='blue', fg='white', command=listen)
dinlebutonu.pack(pady=10)

window.mainloop()
