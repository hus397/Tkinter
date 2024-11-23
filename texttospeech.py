import tkinter
import os
from gtts import gTTS

screen = tkinter.Tk()
screen.geometry('400x200')

def ttspch():
    aud = gTTS(entry.get(), lang='en', slow=False)
    aud.save('ttsaudio.wav')
    os.system('ttsaudio.wav')

frame1 = tkinter.Frame(screen, bg='pink', width=400, height=100, padx=160, pady=20)
tts = tkinter.Label(frame1, text='Text to Speech')
tts.pack()
frame1.pack()

frame2 = tkinter.Frame(screen, bg='green', width=400, height=100, padx=150, pady=10)
entry = tkinter.Entry(frame2)
entry.pack()
submit = tkinter.Button(frame2, text='Submit', command=ttspch)
submit.pack()
frame2.pack()

screen.mainloop()  
