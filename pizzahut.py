import tkinter
import tkinter.ttk

screen = tkinter.Tk()
screen.geometry('400x200')
screen.title('Pizza App')
pizzachoicelist = ['Margherita', 'Pepperoni', 'Pollo']
quantitylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def message():
    sizeselection = str(sizesel.get())
    noselection = str(nochoice.get())
    choice = str(pizzachoice.get())
    basetext.config(text='You ordered ' + noselection + ' ' + sizeselection + ' size ' + '\n' + choice + ' pizzas from us.')

Pizzatitle = tkinter.Label(screen, text='Welcome to Pizza Hut!')
Pizzatitle.grid(row=1, column=1)

fav = tkinter.Label(screen, text='Enter your favourite pizza:')
fav.grid(row=3, column=0)
no = tkinter.Label(screen, text='Enter the quantity:')
no.grid(row=4, column=0)

pizzachoice = tkinter.ttk.Combobox(screen)
pizzachoice['values'] = pizzachoicelist
pizzachoice.grid(row=3, column=1)
nochoice = tkinter.ttk.Combobox(screen)
nochoice['values'] = quantitylist
nochoice.grid(row=4, column=1)
order = tkinter.Button(screen, text='Order', command=message)
order.grid(row=5, column=1)

sizesel = tkinter.StringVar()
sml = tkinter.Radiobutton(screen, text = 'S', variable = sizesel, value = 'Small')
sml.grid(row=3, column=2)
med = tkinter.Radiobutton(screen, text = 'M', variable = sizesel, value = 'Medium')
med.grid(row=4, column=2)
lrg = tkinter.Radiobutton(screen, text = 'L', variable = sizesel, value = 'Large')
lrg.grid(row=5, column=2)

basetext = tkinter.Label(screen, text = '')
basetext.grid(row=7, column=1)

screen.mainloop()