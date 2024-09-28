import tkinter
import time

screen = tkinter.Tk()
screen.geometry('500x300')
screen.title('Digital clock')

def timeget():
    dateclocktime = time.strftime('%H:%M:%S - %dth %B %Y')
    timelabel.configure(text='The time is: ' + dateclocktime)
    timelabel.after(1000, timeget)
timelabel = tkinter.Label(screen, text='The time is:')
timelabel.pack()
timeget()


screen.mainloop()