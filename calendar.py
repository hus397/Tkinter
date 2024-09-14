import tkinter
from calendar import calendar

screen = tkinter.Tk()
screen.geometry('800x600')
screen.title("CALENDAR")


def calendarshow():
  screen2 = tkinter.Tk()
  screen2.geometry("800x800")
  screen2.title("Calendar")
  entryvalue = int(entry.get())
  thecalendar = calendar(entryvalue)
  calendarlabel = tkinter.Text(screen2, height=600, padx = 150)
  calendarlabel.insert("1.0", thecalendar)
  calendarlabel.place(x=0, y=0)
  screen2.mainloop()


title = tkinter.Label(screen,
                      text="CALENDAR",
                      fg="black",
                      bg="light grey",
                      font="Times 60 bold")
title.pack()

year = tkinter.Label(screen, text="Enter Year", fg="black", bg="light green")
year.pack(pady=30)

entry = tkinter.Entry(screen)
entry.pack()

calendarshow = tkinter.Button(screen,
                              text="Show Calendar",
                              fg="black",
                              bg="red",
                              command=calendarshow)
calendarshow.pack(pady=30)

exit = tkinter.Button(screen, text="Exit", fg="black", bg="red")
exit.pack()

screen.mainloop()
