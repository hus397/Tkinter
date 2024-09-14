import tkinter

screen = tkinter.Tk()
screen.geometry('670x100')
screen.title('WEIGHT CONVERTER')

def Convert():
    entryno = int(entrypoint.get())
    poundstext = entryno/453.6
    ouncestext = entryno/28.35
    kilogramstext = entryno/1000
    kilogramsentry.delete('1.0', tkinter.END)
    kilogramsentry.insert(tkinter.END, kilogramstext)
    poundsentry.delete('1.0', tkinter.END)
    poundsentry.insert(tkinter.END, poundstext)
    ouncesentry.delete('1.0', tkinter.END)
    ouncesentry.insert(tkinter.END, ouncestext)

exp = tkinter.Label(screen, text = 'Enter the weight in G')
exp.grid(row=0, column=0)
entrypoint = tkinter.Entry(screen)
entrypoint.grid(row=0, column=1)
convert = tkinter.Button(screen, text='Convert', command=Convert)
convert.grid(row=0, column=2)

kilograms = tkinter.Label(screen, text='Kilograms')
kilograms.grid(row=1, column=0)
pounds = tkinter.Label(screen, text='Pounds')
pounds.grid(row=1, column=1)
ounces = tkinter.Label(screen, text='Ounces')
ounces.grid(row=1, column=2)

kilogramsentry = tkinter.Text(screen, height=1, width=30)
kilogramsentry.grid(row=2, column=0)
poundsentry = tkinter.Text(screen, height=1, width=30)
poundsentry.grid(row=2, column=1)
ouncesentry = tkinter.Text(screen, height=1, width=30)
ouncesentry.grid(row=2, column=2)

screen.mainloop()