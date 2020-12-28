"""
this is tkinter script to change the bgc color

"""


import tkinter
def change_bg():
    window.configure(background="red")
window=tkinter.Tk()
window.geometry("800x200")
window.title("event1")
window.configure(background="yellow")
btn=tkinter.Button(window,text="Change Background Color",bg="white",command=change_bg)
btn.pack()
window.mainloop()