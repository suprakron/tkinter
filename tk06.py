from tkinter import *
from tkinter import messagebox 
def calgrade_click():

    name = str(entry_name.get())
    score = int(entry_score.get())
    result_var.set("ได้คะแนนรวม = " + str(score))
    if ((score >=0) and (score<=50)) :
        messagebox. showinfo (name , "ตุณได้เกรด F")
    elif ((score >=50) and (score<60)):
        messagebox. showinfo (name, "ตุณได้เกรด D")  
    elif((score >-60) and (score<70)):
        messagebox. showinfo (name, "ตุณได้เกรด C") 
    elif((score >=70) and (score<=80)):
        messagebox. showinfo (name, "ตุณได้เกรด B") 
    elif ((score >=80) and (score<=100)):
        messagebox. showinfo (name, "ตุณได้เกรด A") 
    else:
        messagebox. showinfo (name, "ตุณได้เกรด")

win_grade = Tk()
win_grade.title ("โปรแกรมคำนวณเกรด") 
win_grade. geometry ("640x490")

lbl_grade = Label(text="ชื่อ และ คะแนนเก็บ ", fg="black", bg="white") 
lbl_grade.pack(side = TOP)

 

f_name = Frame(win_grade)
lbl_name = Label(f_name,text="ชื่อ")
lbl_name.grid(column=10, row=10)
lbl_name.pack(side = LEFT)
entry_name = Entry(f_name)
entry_name.pack(side = LEFT)
f_name.pack()

f_score = Frame (win_grade)
lbl_score = Label (f_score, text="คะแนนเก็บ") 
lbl_score.grid(column=10, row=10) 
lbl_score.pack(side = LEFT)
entry_score = Entry(f_score)
entry_score.pack(side = LEFT)
f_score.pack()

result_var = StringVar()
result_var.set("euuuny= ")
lbl_result = Label(win_grade, textvariable=result_var,fg ="dark red")
btn_cal = Button(win_grade,text="คำนวณเกรด",command=calgrade_click)

win_grade.mainloop()