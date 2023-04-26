import tkinter as tk
import speech_recognition as sr


# arayüzümüzü oluşturuyoruz
window = tk.Tk()
window.title("Speech Recognition")
window.geometry("600x600")
window.configure(bg='black')

# label oluşturma
label = tk.Label(window, text="Bir şey söyleyin:", bg='black', fg='white')
label.pack(pady=10)

# kaydettiğimiz  sesi transkribe etmek için bir recognizer nesnesi oluşturuyoruz
r = sr.Recognizer()

# mikrofondan ses kaydettiğimiz listen fonksiyonu
def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
    
    try:
        # transkripsiyonu alıyoruz
        text = r.recognize_google(audio, language='tr-TR')
        print("Algılanan kelime: " + text)
        
        # türkiye kelimesini içeriyorsa label'a "Türkiye" yazdıracağımız kısım kontrolü
        if "türkiye" in text.lower():
            label.config(text="Türkiye")
            
    except sr.UnknownValueError:
        label.config(text="Ses anlaşılamadı")
    except sr.RequestError as e:
        label.config(text="Google Ses Tanıma servisi çalışmıyor; {0}".format(e))

# button oluşturuyoruz ve guiye ekliyoruz.
dinlebutonu = tk.Button(window, text="Konuş", bg='blue', fg='white', command=listen)
dinlebutonu.pack(pady=10)

window.mainloop()
