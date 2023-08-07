from tkinter import *
from tkinter import messagebox

def newtask():
    task = my_entry.get()
    if task != "":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning", "plese write some task")
def deletetask():
    lb.delete(ANCHOR)

root=Tk()
root.geometry("500x480+500+200")
root.title("TODO LIST")
root.config(bg="grey")
root.resizable(0,0)

frame=Frame(root).pack(pady=12)

lb = Listbox(frame,width=25,height=8,font=("Times",18),bd=0,fg="red",highlightthickness=0,activestyle="none")
lb.pack(side=TOP)

task_list=["read books", "Exersise","eatting food","take small nap","work on task","watching movies"]

for item in task_list:
    lb.insert(END,item)

sb = Scrollbar(frame)
sb.place(x=383,y=23,relheight=0.47)

lb.config(yscrollcommand = sb.set)
sb.config(command=lb.yview)

my_entry = Entry(root,font=("times",25),bg="green")
my_entry .pack(pady=20)

button_frame=Frame(root).pack(pady=20)
 
btn= Button(button_frame,text="Add Task",font=("times 14"),bg="yellow",padx=22,pady=10,command=newtask)
btn.pack()

del_task= Button(button_frame,text="Delete Task",font=("times 14"),bg="brown",padx=20,pady=12,command=deletetask).pack()


root.mainloop()

