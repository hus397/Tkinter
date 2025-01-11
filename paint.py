from tkinter import *
from tkinter.colorchooser import askcolor

class Paint():
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry('400x400')
        self.penbutton = Button(self.screen, text='pen', command=self.penpress)
        self.penbutton.grid(row=0, column=0)
        self.brushbutton = Button(self.screen, text='brush', command=self.brushpress)
        self.brushbutton.grid(row=0, column=1)
        self.colourbutton = Button(self.screen, text='colour', command=self.colourpress)
        self.colourbutton.grid(row=0, column=2)
        self.eraserbutton = Button(self.screen, text='eraser', command=self.eraserpress)
        self.eraserbutton.grid(row=0, column=3)
        self.thicknessscale = Scale(self.screen, from_=1, to=20, orient=HORIZONTAL)
        self.thicknessscale.grid(row=0, column=4)
        self.canvas = Canvas(self.screen, width=400, height=300, bg='white')
        self.canvas.grid(row=2, column=0, columnspan=5)
        self.setup()
        self.screen.mainloop()
    def move(self, event):
        self.thickness = self.thicknessscale.get()
        if self.eraseron == False:
            paintcolour = self.colour
        else:
            paintcolour = 'white'
        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=paintcolour, width=self.thickness, smooth=True, splinesteps=20, capstyle=ROUND)
        self.oldx = event.x
        self.oldy = event.y
    def release(self, event):
        self.oldx = None
        self.oldy = None
    def setup(self):
        self.oldx = None
        self.oldy = None
        self.thickness = 5
        self.colour = 'black'
        self.ActiveButton = self.penbutton
        self.eraseron = False
        self.canvas.bind('<B1-Motion>', self.move)
        self.canvas.bind('<ButtonRelease-1>', self.release)
    def select(self, button):
        self.ActiveButton.config(relief=RAISED)
        button.config(relief=SUNKEN)
        self.ActiveButton = button
    def penpress(self):
        self.select(self.penbutton)
        self.eraseron = False
    def brushpress(self):
        self.select(self.brushbutton)
        self.eraseron = False
    def colourpress(self):
        self.colour = askcolor(color=self.colour)[1]
    def eraserpress(self):
        self.select(self.eraserbutton)
        self.eraseron = True
        
Project = Paint()

        