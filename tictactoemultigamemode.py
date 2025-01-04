import tkinter
import random
import tkinter.messagebox

screen0 = tkinter.Tk()
screen0.geometry('300x300')
screen0.title('Menu')

def singleplayer():
    screen1.mainloop()
    screen2.destroy()

def multiplayer():
    screen2.mainloop()
    screen1.destroy()

label = tkinter.Label(screen0, text='Welcome to Tic Tac Toe! Choose Your Gamemode!')
label.pack()
sp = tkinter.Button(screen0, text='Single Player', command=singleplayer)
sp.pack()
mp = tkinter.Button(screen0, text='Multi Player', command=multiplayer)
mp.pack()

screen1 = tkinter.Tk()
screen1.geometry('300x300')
screen1.title('Single Player')

def press(button):
    if button in buttons1:
        button.config(text='O')
        buttons1.remove(button)
        win()
        computer_play()
        win()

def computer_play():
    choice = random.choice(buttons1)
    buttons1.remove(choice)
    choice.config(text='X')

def win():
    for i in win_combinations1:
        if i[0].cget('text') == i[1].cget('text') == i[2].cget('text') == 'O':
            tkinter.messagebox.showinfo('You Win!', 'Well Done! You Win!')
            screen1.destroy()
        elif i[0].cget('text') == i[1].cget('text') == i[2].cget('text') == 'X':
            tkinter.messagebox.showinfo('You Lose!', 'Unlucky! You Lose!')
            screen1.destroy()
    if len(buttons1) == 0:
        tkinter.messagebox.showinfo('You Drew!', 'Unlucky! You Drew!')
        screen1.destroy()

Computer = tkinter.Label(screen1, text='Computer: X')
Computer.grid(row=0, column=0, columnspan=3)

User = tkinter.Label(screen1, text='User: O')
User.grid(row=1, column=0, columnspan=3)

lt1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(lt1))
lt1.grid(row=2, column=0)
mt1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(mt1))
mt1.grid(row=2, column=1)
rt1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(rt1))
rt1.grid(row=2, column=2)
lm1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(lm1))
lm1.grid(row=3, column=0)
mm1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(mm1))
mm1.grid(row=3, column=1)
rm1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(rm1))
rm1.grid(row=3, column=2)
lb1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(lb1))
lb1.grid(row=4, column=0)
mb1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(mb1))
mb1.grid(row=4, column=1)
rb1 = tkinter.Button(screen1, width=10, height=5, command=lambda:press(rb1))
rb1.grid(row=4, column=2)

buttons1 = [lt1, mt1, rt1, lm1, mm1, rm1, lb1, mb1, rb1]

win_combinations1 = [(lt1, mt1, rt1), (lm1, mm1, rm1), (lb1, mb1, rb1), (lt1, lm1, lb1), (mt1, mm1, mb1), (rt1, rm1, rb1), (lt1, mm1, rb1), (rt1, mm1, lb1)]


turn = True

screen2 = tkinter.Tk()
screen2.geometry('300x300')
screen2.title('Multi Player')

def press2p(button):
    global turn
    if turn == True:
        if button in buttons:
            button.config(text='X')
            buttons.remove(button)
            win2p()
            turn = False
    elif turn == False:
        if button in buttons:
            button.config(text='O')
            buttons.remove(button)
            win2p()
            turn = True
            

def win2p():
    for i in win_combinations:
        if i[0].cget('text') == i[1].cget('text') == i[2].cget('text') == 'O':
            tkinter.messagebox.showinfo('Player 2 Wins!', 'Well Done Player 2! You Win!')
            screen2.destroy()
        elif i[0].cget('text') == i[1].cget('text') == i[2].cget('text') == 'X':
            tkinter.messagebox.showinfo('Player 1 Wins!', 'Well Done Player 1! You Win!')
            screen2.destroy()
    if len(buttons) == 0:
        tkinter.messagebox.showinfo('Draw!', 'Unlucky! You both drew!')
        screen2.destroy()

Player1 = tkinter.Label(screen2, text='Player 1: X')
Player1.grid(row=0, column=0, columnspan=3)

Player2 = tkinter.Label(screen2, text='Player 2: O')
Player2.grid(row=1, column=0, columnspan=3)

lt = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(lt))
lt.grid(row=2, column=0)
mt = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(mt))
mt.grid(row=2, column=1)
rt = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(rt))
rt.grid(row=2, column=2)
lm = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(lm))
lm.grid(row=3, column=0)
mm = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(mm))
mm.grid(row=3, column=1)
rm = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(rm))
rm.grid(row=3, column=2)
lb = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(lb))
lb.grid(row=4, column=0)
mb = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(mb))
mb.grid(row=4, column=1)
rb = tkinter.Button(screen2, width=10, height=5, command=lambda:press2p(rb))
rb.grid(row=4, column=2)

buttons = [lt, mt, rt, lm, mm, rm, lb, mb, rb]

win_combinations = [(lt, mt, rt), (lm, mm, rm), (lb, mb, rb), (lt, lm, lb), (mt, mm, mb), (rt, rm, rb), (lt, mm, rb), (rt, mm, lb)]

screen0.mainloop()


