from tkinter import *
import random

screen = Tk()
screen.geometry('600x400')
screen.title('Ping Pong')

canvas = Canvas(screen, width=600, height=400, bg='black')
canvas.pack()

canvas.create_line(300, 0, 300, 400, fill='white', width=4)
scoreboard = canvas.create_text(300, 20, font=('Arial', 15, 'bold'), text=' 0   0 ', fill='white')
canvas.create_oval(250, 150, 350, 250, outline='white', fill='black', width=4)

class Ball():
    def __init__(self, canvas):
        self.canvas = canvas
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill='red')
        self.directions = [1, 2, 3, 4, -1, -2, -3, -4]
        random.shuffle(self.directions)
        self.x = self.directions[1]
        self.y = self.directions[2]
        self.canvaswidth = 600
        self.canvasheight = 400
        self.sp1 = 0
        self.sp2 = 0
    def draw(self):
        self.canvas.move(self.ball, self.x, self.y)
        self.pos = self.canvas.coords(self.ball)
        if self.pos[1] <= 0 or self.pos[3] >= 400: #check for border collisions
            self.y = self.y * -1
        if self.pos[0] <= 0:
            self.x = self.x * -1
            self.sp2 = self.sp2 + 1
        if self.pos[2] >= 600:
            self.x = self.x * -1
            self.sp1 = self.sp1 + 1

#create paddles (2 classes)
        
        
        
screen.mainloop()

#centre at 300,200
#thickness 20
#start point 290, 190
#end point 310, 210
