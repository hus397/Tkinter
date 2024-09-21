import tkinter
import random
screen = tkinter.Tk()
screen.geometry('400x200')
screen.title('Rock Paper Scissors Game')
choices = ['rock', 'paper', 'scissors']
yourscore = 0
compscore = 0

def computerchoice():
    choice = random.choice(choices)
    computerselected.configure(text = 'Computer selected:' + choice)
    return choice
    
def computerwins():
    global compscore
    compscore = compscore + 1
    computerscore.configure(text = 'Computer Score:' + str(compscore))
    winner.configure(text = 'You lose!')
    
def playerwins():
    global yourscore
    yourscore = yourscore + 1
    playerscore.configure(text = 'Player score:' + str(yourscore))
    winner.configure(text = 'You win!')
    
def tie():
    winner.configure(text = 'Tie!')
    
def playerchoice(selection):
    youselected.configure(text = 'Player Selected:' + selection)
    csel = computerchoice()
    if selection == 'rock' and csel == 'paper' or selection == 'paper' and csel == 'scissors' or selection == 'scissors' and csel == 'rock':
        computerwins()
    elif selection == 'paper' and csel == 'rock' or selection == 'rock' and csel == 'scissors' or selection == 'scissors' and csel == 'paper':
        playerwins()
    elif selection == csel:    
        tie()
         
rps = tkinter.Label(screen, text='Rock Paper Scissors')
rps.grid(row=0, column=1)
winner = tkinter.Label(screen, text='')
winner.grid(row=1, column=1)
youroptions = tkinter.Label(screen, text='Your Options:')
youroptions.grid(row=2, column=0)
rock = tkinter.Button(screen, text='Rock', command = lambda: playerchoice('rock'))
rock.grid(row=3, column=1)
paper = tkinter.Button(screen, text='Paper', command = lambda: playerchoice('paper'))
paper.grid(row=3, column=2)
scissors = tkinter.Button(screen, text='Scissors', command = lambda: playerchoice('scissors'))
scissors.grid(row=3, column=3)
score = tkinter.Label(screen, text='Score:')
score.grid(row=4, column=0)
youselected = tkinter.Label(screen, text='You Selected:')
youselected.grid(row=5, column=1)
playerscore = tkinter.Label(screen, text='Player Score:')
playerscore.grid(row=5, column=2)
computerselected = tkinter.Label(screen, text = 'Computer Selected')
computerselected.grid(row=6, column=1)
computerscore = tkinter.Label(screen, text='Computer Score:')
computerscore.grid(row=6, column=2)
screen.mainloop()