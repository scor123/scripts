"""
CountDown Timer in tkinter
"""

import tkinter
import time
# def change():
def countdown():
    lbl2.configure(bg="white")
    howLong= int(txt1.get())
    for i in range(howLong,0,-1):
        lbl2.configure(text=i)
        window.update()
        time.sleep(1)
    lbl2.configure(text="Done!")
window=tkinter.Tk()
window.geometry("800x500")
window.title("game")
window.configure(background="yellow")
lbl1=tkinter.Label(window, text="How many seconds to count down?")
lbl1.pack()
txt1 = tkinter.Entry(window)
txt1.pack()
btn1 = tkinter.Button(window,text="Start Count Down", bg="red",command=countdown)
btn1.pack()
lbl2= tkinter.Label(window, height="10",width="10")
lbl2.pack()

window.mainloop()