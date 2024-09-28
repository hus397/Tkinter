import tkinter
import random
import tkinter.messagebox

screen = tkinter.Tk()
screen.geometry('300x100')
screen.title('Guess the number game')
welcome = tkinter.Label(screen, text='Welcome to the game!')
welcome.grid(row=0, column=1)

def msg():
    name = nameentry.get()
    tkinter.messagebox.showinfo('name', 'Well, ' + name + ', I am thinking of a number between 1 and 20.')

namelabel = tkinter.Label(screen, text="What's your name?")
namelabel.grid(row=2, column=0)
nameentry = tkinter.Entry(screen)
nameentry.grid(row=2, column=1)
ok = tkinter.Button(screen, text='OK', command=msg)
ok.grid(row=2, column=2)    

number = random.randint(1,20)    
def numbergen():
    name = nameentry.get()
    guess = int(guessentry.get())
    if guess == number:
        tkinter.messagebox.showinfo('Well done!', 'Well done, ' + name + ', You guessed correct! My number was: ' + str(number))
    elif guess > number:
        tkinter.messagebox.showinfo('Unlucky!', 'Well, ' + name + ', my number was lower than your guess.')
    elif guess < number:
        tkinter.messagebox.showinfo('Unlucky!', 'Well, ' + name + ', my number was higher than your guess.')
        
guesslabel = tkinter.Label(screen, text='Take a guess:')
guesslabel.grid(row=3, column=0)
guessentry = tkinter.Entry(screen)
guessentry.grid(row=3, column=1)
guessbutton = tkinter.Button(screen, text='Guess', command = numbergen)
guessbutton.grid(row=3, column=2)
screen.mainloop()