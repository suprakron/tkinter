from tkinter import *
from tkinter import messagebox


def calgrade_click():

    name = str(entry_name.get())
    bill = int(entry_score.get())
    result_var.set("จำนวน =" + str(bill))
    if ((bill >= 0) and (bill <= 50)):
        messagebox.showinfo(name, "หน่วยละ 0 บาท")
    elif ((bill >= 50) and (bill <= 60)):
        messagebox.showinfo(name, "หน่วยละ 3 บาท")
    elif ((bill >= 60) and (bill <= 70)):
        messagebox.showinfo(name, "หน่วยละ 5 บาท")
    elif ((bill >= 70) and (bill <= 80)):
        messagebox.showinfo(name, "หน่วยละ 7 บาท")
    else:
        messagebox.showinfo(name, "หน่วยละ")


win_grade = Tk()
win_grade.title("โปรแกรมคำนวณค่าไฟฟ้าแบบก้าวหน้า ")
win_grade.geometry("640x480")

lbl_grade = Label(text="โปรแกรมคำนวณค่าไฟฟ้าแบบก้าวหน้า ",
                  fg="black", bg="white")
lbl_grade.pack(side=TOP)
f_name = Frame(win_grade)
lbl_name = Label(f_name, text="ชื่อ")
lbl_name.grid(column=10, row=10)
lbl_name.pack(side=LEFT)
entry_name = Entry(f_name)
entry_name.pack(side=LEFT)
f_name.pack()
f_score = Frame(win_grade)
lbl_score = Label(f_score, text="จำนวนหน่วย")
lbl_score.grid(column=10, row=10)
lbl_score.pack(side=LEFT)
entry_score = Entry(f_score)
entry_score.pack(side=LEFT)
f_score.pack()
result_var = StringVar()
result_var.set("จำนวน = ")
lbl_result = Label(win_grade, textvariable=result_var, fg="dark red")
lbl_result.pack()
btn_cal = Button(win_grade, text="คำนวณ", command=calgrade_click)
btn_cal.pack()
win_grade.mainloop()
