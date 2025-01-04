from tkinter import *

class Paint():
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry('400x400')
        self.pen = Button(self.screen, text='pen')
        self.pen.grid(row=0, column=0)
        self.brush = Button(self.screen, text='brush')
        self.brush.grid(row=0, column=1)
        self.colour = Button(self.screen, text='colour')
        self.colour.grid(row=0, column=2)
        self.eraser = Button(self.screen, text='eraser')
        self.eraser.grid(row=0, column=3)
        self.thickness = Scale(self.screen, from_=1, to=20, orient=HORIZONTAL)
        self.thickness.grid(row=0, column=4)
        self.canvas = Canvas(self.screen, width=400, height=300)
        self.canvas.grid(row=2, column=0, columnspan=5)
        self.setup()
        self.screen.mainloop()
    def move(self):
        pass
    def release(self):
        pass
    def setup(self):
        self.oldx = None
        self.oldy = None
        self.thickness = 5
        self.colour = 'black'
        self.ActiveButton = self.pen
        self.eraseron = False
        self.canvas.bind('<B1-Motion>', self.move)
        self.canvas.bind('<ButtonRelease-1>', self.release)
        
        
        
Project = Paint()

        