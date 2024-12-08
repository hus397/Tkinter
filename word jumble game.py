import tkinter
import random
import tkinter.messagebox

wordlist=['servant', 'classic', 'puzzled', 'necklace', 'fitful', 'apply', 'recycle', 'picture', 'cliff', 'fluid', 'illicit', 'shared', 'real', 'fake', 'duct']
noword = 8
userscore = 0
choice = ''

indexes = random.sample(range(len(wordlist)), noword)
def jumbleword():
    global choice
    choice = wordlist[indexes.pop()]
    length = len(choice)
    w = ''
    jumble = random.sample(range(length), length)
    for j in jumble:
        w = w + choice[j]
    jumbletext.config(text=w)
    
def Check():
    global choice
    global userscore
    response = entry.get()
    if response == choice:
        tkinter.messagebox.showinfo('Correct!', 'You were correct!')
        userscore = userscore + 1
        score.config(text='Score:'+ str(userscore))
        jumbleword()
    else:
        tkinter.messagebox.showinfo('Incorrect!', 'You were not correct!')

def Reset():
    global userscore
    userscore = 0
    global indexes
    indexes = random.sample(range(len(wordlist)), noword)
    score.config(text='Score' + str(userscore))
    jumbleword()
    
screen = tkinter.Tk()
screen.geometry('350x300')
screen.title('Jumbled Word Game')
screen.config(bg='black')

header = tkinter.Label(screen, text='Jumbled Word Game', bg='black', fg='white', font='Arial 25 bold', padx=5, pady=5)
header.grid(row=0, column=0, columnspan=3)
jumbletext = tkinter.Label(screen, text='', bg='black', fg='white', font='Arial 12 bold')
jumbletext.grid(row=1, column=1, padx=5, pady=5)

entry = tkinter.Entry(screen, width=40)
entry.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

check = tkinter.Button(screen, text='Check', font='Arial 12 bold', bg='dark grey', fg='green', command=Check)
check.grid(row=3, column=1, padx=0, pady=10)

reset = tkinter.Button(screen, text='Reset', font='Arial 12 bold', bg='light grey', fg='yellow', command=Reset)
reset.grid(row=4, column=1, padx=0, pady=10)

score = tkinter.Label(screen, text='Score:' + str(userscore), font='Arial 12 bold', bg='black', fg='white')
score.grid(row=5, column=0)
    
jumbleword()

screen.mainloop()