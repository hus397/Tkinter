import tkinter

screen = tkinter.Tk()
screen.geometry('515x300')
screen.title('My Address Book')

record = {}

def upl():
    list.delete(0, tkinter.END)
    list2 = record.keys()
    for i in list2:
        list.insert(tkinter.END, i)

def upac():
    namen = namee.get()
    addressn = addresse.get()
    mobilen = mobilee.get()
    emailn = emaile.get()
    bdayn = bdaye.get()
    record[namen]=[addressn, mobilen, emailn, bdayn]
    upl()
    
def deletevar():
    selvar = list.curselection()
    selvar = list.get(selvar)
    del record[selvar]
    upl()
    
def edits():
    selvar = list.curselection()
    selvar = list.get(selvar)
    namee.insert(tkinter.END, selvar)
    l1 = record[selvar]
    addresse.insert(tkinter.END, l1[0])
    mobilee.insert(tkinter.END, l1[1])
    emaile.insert(tkinter.END, l1[2])
    bdaye.insert(tkinter.END, l1[3])
    

header = tkinter.Label(screen, text = 'My Address Book')
header.grid(row=0, column=1)

open = tkinter.Button(screen, text='Open', width=7)
open.grid(row=0, column=2)

list = tkinter.Listbox(screen, width=30)
list.grid(row=1, column=0, rowspan=9, columnspan=2)

name = tkinter.Label(screen, text='Name:', padx=30, pady=10)
name.grid(row=1, column=2)

address = tkinter.Label(screen, text='Address:', pady=10)
address.grid(row=3, column=2)

mobile = tkinter.Label(screen, text='Mobile:', pady=10)
mobile.grid(row=5, column=2)

email = tkinter.Label(screen, text='Email:', pady=10)
email.grid(row=7, column=2)

bday = tkinter.Label(screen, text='Birthday:', pady=10)
bday.grid(row=9, column=2)


namee = tkinter.Entry(screen)
namee.grid(row=1, column=3)

addresse = tkinter.Entry(screen)
addresse.grid(row=3, column=3)

mobilee = tkinter.Entry(screen)
mobilee.grid(row=5, column=3)

emaile = tkinter.Entry(screen)
emaile.grid(row=7, column=3)

bdaye = tkinter.Entry(screen)
bdaye.grid(row=9, column=3)


edit = tkinter.Button(screen, text='Edit', width=10, command=edits)
edit.grid(row=11, column=0)

delete = tkinter.Button(screen, text='Delete', width=10, command=deletevar)
delete.grid(row=11, column=1)

upa = tkinter.Button(screen, text='Update/Add', width=10, command=upac)
upa.grid(row=11, column=3)

save = tkinter.Button(screen, text='Save', width=40)
save.grid(row=12, column=1, columnspan=2)


screen.mainloop()