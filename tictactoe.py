import tkinter
import random
import tkinter.messagebox

screen1 = tkinter.Tk()
screen1.geometry('300x300')
screen1.title('Single Player')

def press(button):
    if button in buttons:
        button.config(text='O')
        buttons.remove(button)
        win()
        computer_play()
        win()

def computer_play():
    choice = random.choice(buttons)
    buttons.remove(choice)
    choice.config(text='X')

def win():
    for i in win_combinations:
        if i[0].cget('text') == i[1].cget('text') == i[2].cget('text') == 'O':
            tkinter.messagebox.showinfo('You Win!', 'Well Done! You Win!')
            screen1.destroy()
        elif i[0].cget('text') == i[1].cget('text') == i[2].cget('text') == 'X':
            tkinter.messagebox.showinfo('You Lose!', 'Unlucky! You Lose!')
            screen1.destroy()
    if len(buttons) == 0:
        tkinter.messagebox.showinfo('You Drew!', 'Unlucky! You Drew!')
        screen1.destroy()

Computer = tkinter.Label(screen1, text='Computer: X')
Computer.grid(row=0, column=0, columnspan=3)

User = tkinter.Label(screen1, text='User: O')
User.grid(row=1, column=0, columnspan=3)

lt = tkinter.Button(screen1, width=10, height=5, command=lambda:press(lt))
lt.grid(row=2, column=0)
mt = tkinter.Button(screen1, width=10, height=5, command=lambda:press(mt))
mt.grid(row=2, column=1)
rt = tkinter.Button(screen1, width=10, height=5, command=lambda:press(rt))
rt.grid(row=2, column=2)
lm = tkinter.Button(screen1, width=10, height=5, command=lambda:press(lm))
lm.grid(row=3, column=0)
mm = tkinter.Button(screen1, width=10, height=5, command=lambda:press(mm))
mm.grid(row=3, column=1)
rm = tkinter.Button(screen1, width=10, height=5, command=lambda:press(rm))
rm.grid(row=3, column=2)
lb = tkinter.Button(screen1, width=10, height=5, command=lambda:press(lb))
lb.grid(row=4, column=0)
mb = tkinter.Button(screen1, width=10, height=5, command=lambda:press(mb))
mb.grid(row=4, column=1)
rb = tkinter.Button(screen1, width=10, height=5, command=lambda:press(rb))
rb.grid(row=4, column=2)

buttons = [lt, mt, rt, lm, mm, rm, lb, mb, rb]

win_combinations = [(lt, mt, rt), (lm, mm, rm), (lb, mb, rb), (lt, lm, lb), (mt, mm, mb), (rt, rm, rb), (lt, mm, rb), (rt, mm, lb)]

screen1.mainloop()