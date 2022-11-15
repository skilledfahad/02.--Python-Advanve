from tkinter import *
def something():
  subwin = Tk()
  subwin.geometry("500x500")  # subwindows size
  subwin.title("Note")  # subwindows name

  # ======== Lebel ========
  subwin_lebel = Label(subwin, text = "Thanks for your review.")
  subwin_lebel.pack()

  subwin.mainloop()

