import tkinter
import tkinter.filedialog

screen = tkinter.Tk()
screen.geometry('375x350')
screen.title('Memoriser')

def addvar():
    uservar = str(entry.get())
    listbox.insert(tkinter.END, uservar)
    entry.delete(0, tkinter.END)

def delvar():
    selvar = listbox.curselection()
    for i in reversed(selvar):
        listbox.delete(i)           

def savefile():
    saveit = tkinter.filedialog.asksaveasfile(defaultextension='.txt') 
    if saveit is not None:
        list = listbox.get(0, tkinter.END)
        for i in list:
           print(i.strip(), file=saveit)
        listbox.delete(0, tkinter.END)
        
def openfile():
    openit = tkinter.filedialog.askopenfile(defaultextension='.txt')
    listbox.delete(0, tkinter.END)
    if openit is not None:
        filelist = openit.readlines()
        for i in filelist:
            listbox.insert(tkinter.END, i)

open = tkinter.Button(screen, text='OPEN', width=15, command=openfile)
delete = tkinter.Button(screen, text='DELETE', width=15, command=delvar)
save = tkinter.Button(screen, text='SAVE', width=15, command=savefile)
add = tkinter.Button(screen, text='ADD', width=15, command=addvar)

open.grid(row=0, column=0, padx=5)
delete.grid(row=0, column=1, padx=5)
save.grid(row=0, column=2, padx=5)
add.grid(row=1, column=2, pady=5)

entry = tkinter.Entry(screen, width=37)
entry.grid(row=1, column=0, columnspan=2, pady=5)

listbox = tkinter.Listbox(screen, width=60)
listbox.grid(row=2, column=0, columnspan=3, pady=5)
listbox.config(selectmode=tkinter.MULTIPLE)

listbox.insert(tkinter.END, 'usa')
listbox.insert(tkinter.END, 'uk')
listbox.insert(tkinter.END, 'france')
listbox.insert(tkinter.END, 'russia')
listbox.insert(tkinter.END, 'germany')

screen.mainloop()