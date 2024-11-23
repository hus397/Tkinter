import tkinter
import speech_recognition as sr

screen = tkinter.Tk()
screen.title('SPEECH TO TEXT')
screen.geometry('600x150')

def on():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        output.insert(tkinter.END, '(Try say something!)')
        audio=r.listen(source)
        text = r.recognize_google(audio)
        output.delete(0, tkinter.END)
        output.insert(tkinter.END, text)

vn = tkinter.Label(screen, text='Voice Notepad', font='Calibri 20 bold')
vn.grid(row=0, column=1)

click = tkinter.Button(screen, text='Click on me to start!', width=20, command=on)
click.grid(row=1, column=0, padx=10, pady=10)

output = tkinter.Text(screen, width=30, height=5)
output.grid(row=1, column=1, padx=10, pady=10)

save = tkinter.Button(screen, text='Save the text', width=20)
save.grid(row=1, column=2)

screen.mainloop()