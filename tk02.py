from tkinter import *
window = Tk()
window.title("Hello")
window.geometry("640x480")
lbl = Label(window, text="Hello", font=("Arial Bold",30)) 
lbl.grid(column=0,row=0)
btn = Button(window,text="Click Me",font = ("Arial",40), bg = "orange", fg = "red")
btn.grid(column=1,row=0) 
window.mainloop() 