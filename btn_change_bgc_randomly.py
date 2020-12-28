"""
This code for button change background randomly
"""
import tkinter
import random
def bgc():
    color=["red","blue","green"]
    window.configure(background=random.choice(color))
window=tkinter.Tk()
window.geometry("800x500")
window.title("game")
window.configure(background="yellow")
lbl1=tkinter.Label(window, text="The button change the background color")
lbl1.pack()

btn1 = tkinter.Button(window,text="Click Me!", bg="red",command=bgc)
btn1.pack()


window.mainloop()