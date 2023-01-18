## to do list ##

## import tkinter
from tkinter import *
from tkinter import messagebox

## create new task from entry box. The value entered will be stored in the task variable. If no task is entered prompt a warning. 

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning","Please enter a task.")

## Add delete button to delete selected item in the list box

def deleteTask():
    lb.delete(ANCHOR)

## Create and configure a window

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To Do List')
ws.config(bg= '#223441')
ws.resizable(width=False, height=False)

## Create a frame, add padding around side

frame = Frame(ws)
frame.pack(pady=10)

## Create a listbox to store list graphically 

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

## sample task list for now, filled with dummy data

task_list = [
    'Eat food',
    'Drink water',
    'Practice Vim',
    'Go to work',
    'Sleep',
    ]

for item in task_list:
    lb.insert(END, item)

## Create a scroll bar for tasks list

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

## Create an entry box to take input from user

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

## Create another frame to add buttons

button_frame = Frame(ws)
button_frame.pack(pady=20)

## Add buttons into button frame

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
