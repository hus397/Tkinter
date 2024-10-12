import tkinter
import tkinter.messagebox
import time

screen = tkinter.Tk()
screen.geometry('400x200')
screen.title('Stopwatch')


hr = tkinter.StringVar()
mn = tkinter.StringVar()
s = tkinter.StringVar()

def timesup():
    tkinter.messagebox.showinfo('Time`s up','Time is up!')

def scount():
    tot = int(hr.get()) * 3600 + int(mn.get()) * 60 + int(s.get())
    while tot > 0:
        tot = tot - 1
        time.sleep(1)
        newh = tot//3600
        newm = (tot%3600)//60
        news = (tot%3600)%60
        hr.set("{00:2d}".format(newh))
        mn.set("{00:2d}".format(newm))
        s.set("{00:2d}".format(news))
        if tot == 0:
            timesup()
        screen.update()
        
        
hours = tkinter.Entry(screen, textvariable=hr)
hours.grid(row=0, column=0)
minutes = tkinter.Entry(screen, textvariable=mn)
minutes.grid(row=0, column=1)
seconds = tkinter.Entry(screen, textvariable=s)
seconds.grid(row=0, column=2)
count = tkinter.Button(screen, text = 'Start', command = scount)
count.grid(row=1, column=1)

screen.mainloop()