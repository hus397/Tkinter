from tkinter import *
import random
import time

screen = Tk()
screen.geometry('600x400')
screen.title('Ping Pong')

canvas = Canvas(screen, width=600, height=400, bg='black')
canvas.pack()

canvas.create_line(300, 0, 300, 400, fill='white', width=4)
scoreboard = canvas.create_text(300, 20, font=('Arial', 15, 'bold'), text=' 0   0 ', fill='white')
canvas.create_oval(250, 150, 350, 250, outline='white', fill='black', width=4)

class Ball():
    def __init__(self, canvas, paddleL, paddleR):
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
        self.paddleL = paddleL
        self.paddleR = paddleR
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
        self.paddlewasd()
        self.paddlearrow()
        canvas.itemconfigure(scoreboard, text= str(self.sp1) + ':' + str(self.sp2))
    def paddlewasd(self):
        self.paddlepos = self.canvas.coords(self.paddleL.paddle)
        if self.pos[3] >= self.paddlepos[1] and self.pos[1] <= self.paddlepos[3]:
            if self.pos[0] >= self.paddlepos[0] and self.pos[0] <= self.paddlepos[2]:
                self.x = self.x * -1
    def paddlearrow(self):
        self.paddlepos = self.canvas.coords(self.paddleR.paddle)
        if self.pos[3] >= self.paddlepos[1] and self.pos[1] <= self.paddlepos[3]:
            if self.pos[2] >= self.paddlepos[0] and self.pos[2] <= self.paddlepos[2] :
                self.x = self.x * -1
    
               

#create paddles (2 classes)
class PaddleWASD():
    def __init__(self, canvas):
        self.canvas = canvas
        self.y = 0
        self.paddle = self.canvas.create_rectangle(10, 50, 15, 125, fill='white')
        self.canvas.bind_all('w', self.moveup)
        self.canvas.bind_all('s', self.movedown)
    def draw(self):
        self.canvas.move(self.paddle, 0, self.y)
        self.pos = self.canvas.coords(self.paddle)
        if self.pos[1] <= 0 or self.pos[3] >= 400: 
            self.y = 0
    def moveup(self, event):
        self.y = -3
    def movedown(self, event):
        self.y = 3
        
    
class PaddleArrow():
    def __init__(self, canvas):
        self.canvas = canvas
        self.y = 0
        self.paddle = self.canvas.create_rectangle(585, 50, 590, 125, fill='white')
        self.canvas.bind_all('<KeyPress-Up>', self.moveup)
        self.canvas.bind_all('<KeyPress-Down>', self.movedown)
    def draw(self):
        self.canvas.move(self.paddle, 0, self.y)
        self.pos = self.canvas.coords(self.paddle)
        if self.pos[1] <= 0 or self.pos[3] >= 400: 
            self.y = 0    
    def moveup(self, event):
        self.y = -3
    def movedown(self, event):
        self.y = 3



paddlewas = PaddleWASD(canvas)
paddlearw = PaddleArrow(canvas)
ball = Ball(canvas, paddlewas, paddlearw)



while True:
    ball.draw()
    paddlewas.draw()
    paddlearw.draw()
    time.sleep(0.02)
    screen.update_idletasks()
    screen.update()


#centre at 300,200
#thickness 20
#start point 290, 190
#end point 310, 210
