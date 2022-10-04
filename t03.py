from tkinter import * 
from tkinter import messagebox 
def calgrade_click():
    name = str(entry_name.get() 
    bill - int (entry_score.get() 
    result_var. set ("hu = " + str(bill)) if ((bill >=0) and (billc=50)) :
messagebox.showinfo (name," 0 ") elif ((bill >=50) and (billc=60)):
messagebox.showinfo (name,"minua 3 Ux") elif ((bill >60) and (billc-70)): messagebox.showinfo (name, "
w at 5 ") elif((bill >=70) and (bill<=80)):
messagebox.showinfo (name, "wiu 7 ")
messagebox.showinfo (name, "wizuar")
win_grade = Tk() win_grade.title("lusunsurunuphlwihuuurt ) win_grade.geometry("640x480") 1bl_grade = Label(text="lusursu r i lvýhuuurina ", fg="black", bg="white") lbl_grade.pack (side = TOP) f_name = Frame (win_grade) lbl_name = Label (f_name, text="do") lbl name.grid(column=10, row=10) lbl name.pack (side - LEFT) entry_name = Entry (f_name) entry_name.pack (side = LEFT) f name.pack() f_score = Frame (win_grade) 1bl_score = Label (f_score, text="uuiu") lbl score.grid (column-10, row-10) lbl_score.pack (side - LEFT) entry_score = Entry(f_score) entry_score.pack (side - LEET) f_score.pack() result_var = Stringvar() result var.set("
") 1b1_result = Label (win_grade, textvariable-result_var, fg "dark red") lbl_result.pack btn_cal - Button (win_grade, text = " 74", command-calgrade_click) btn_cal.pack() win_grade.mainloop
