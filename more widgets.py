import tkinter
import tkinter.filedialog

screen = tkinter.Tk()
screen.geometry('400x400')
screen.title('Widgets')
#screen.config(background='green')

def open():
    file = tkinter.filedialog.askopenfile(title='Files')
    
def save():
    saveit = tkinter.filedialog.asksaveasfile(defaultextension='.txt') 

#the filedialog widget contains functions allow you to open or save an existing or new file (asksaveasfilename changes file name) 

frame = tkinter.Frame(screen, background='red', height=100, width=200)
frame.pack()
#frames group widgets together allowing functions to apply (show and hide) to multiple widgets (div in html)
but1 = tkinter.Button(frame, text='Open', command=open)
but1.pack()
but2 = tkinter.Button(screen, text='Save', command=save)
but2.pack()
but3 = tkinter.Button(frame, text='Save')
but3.pack()

listbox = tkinter.Listbox(screen)
listbox.insert(tkinter.END, 'hello')
listbox.insert(tkinter.END, 'greetings')
listbox.insert(tkinter.END, 'hey')
listbox.insert(tkinter.END, 'hi')
listbox.delete('hi')
listbox.config(selectmode=tkinter.MULTIPLE)
listbox.pack()
#listboxes are like comboboxes except that all options are shown and none are hidden
#options can be added with insert or config
#to change whether it selects one or multiple, use selectmode
#to get from a list create a loop to move through it

scrollbar = tkinter.Scrollbar(screen)


screen.mainloop()
