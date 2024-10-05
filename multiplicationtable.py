import tkinter
import tkinter.ttk

screen = tkinter.Tk()
screen.geometry('400x600')
screen.title('Mathematical times table generator')
numbervalues = []

for i in range(1, 31):
    numbervalues.append(i)
        
def multiply():
    selection=int(numberchoice.get())
    selection2=int(multsel.get())
    table=str()
    for i in range(1, selection2+1):
        table = table + (str(selection) + 'x' + str(i) + '=' + str(selection*i) + '\n')
    multable.configure(text=table)
        

heading = tkinter.Label(screen, text='Mathematical table')
heading.grid(row=1, column=1)
norlabel = tkinter.Label(screen, text='Number and Range:', padx=5)
norlabel.grid(row=3, column=0)
numberchoice = tkinter.ttk.Combobox(screen)
numberchoice['values'] = numbervalues
numberchoice.grid(row=3, column=1)
multsel = tkinter.IntVar()
multno1 = tkinter.Radiobutton(screen, text='10', variable=multsel, value=10)
multno1.grid(row=3, column=2)
multno2 = tkinter.Radiobutton(screen, text='20', variable=multsel, value=20)
multno2.grid(row=4, column=2)
multno3 = tkinter.Radiobutton(screen, text='30', variable=multsel, value=30)
multno3.grid(row=5, column=2)
generate = tkinter.Button(screen, text='Generate', command=multiply)
generate.grid(row=6, column=1)

multable = tkinter.Label(screen)
multable.grid(row=8, column=1)


screen.mainloop()