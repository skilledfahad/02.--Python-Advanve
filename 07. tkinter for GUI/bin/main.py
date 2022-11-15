from tkinter import *
from page1 import something

win = Tk()
win.geometry("500x500")  # windows size
win.title("Note")  # windows name

# ======== Lebel ========
win_lebel = Label(win, text = "Hello world, Do you like python??") #  Lebel(Master, Style)win_lebel.pack()
win_lebel.pack()

# ======== Cheackbutton ========
ck_btn1 = Checkbutton(win, text = 'Yes' )
ck_btn1.select()
ck_btn1.pack()

ck_btn2 = Checkbutton(win, text = "No")
ck_btn2.pack()

# ======== Button ========
button = Button (win, text = "Submit", bg= "red", fg= "blue", command= something)  # Button (Master, Style)
button.pack()


win.mainloop()



