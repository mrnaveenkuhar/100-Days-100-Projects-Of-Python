#---------------------------------------------|| 100 Projects for 100 Days ||---------------------------------------------#
#Day 08
#Name : TO Do List Manager
#discription : This is a simple to do list manager. You can add, remove, and view your to do list.

#importing modules
from tkinter import *
from tkinter import messagebox
import json

#creating window
window = Tk()
window.title("To Do List Manager")
window.config(padx=50, pady=50)

#creating canvas

canvas = Canvas(width=200, height=224)

canvas.grid(column=1, row=0)

#creating label

label = Label(text="To Do List Manager", font=("Arial", 20, "bold"))
label.grid(column=1, row=1)

#creating entry

entry = Entry(width=20)
entry.grid(column=1, row=2)

#creating buttons

def add():
    task = entry.get()
    if task == "":
        messagebox.showerror(title="Error", message="Please enter a task")
    else:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.append(task)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file)
        entry.delete(0, END)
        view()

def view():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        messagebox.showinfo(title="To Do List", message=data)

def remove():
    task = entry.get()
    if task == "":
        messagebox.showerror(title="Error", message="Please enter a task")
    else:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.remove(task)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file)
        entry.delete(0, END)
        view()

add_button = Button(text="Add", command=add)
add_button.grid(column=0, row=3)

view_button = Button(text="View", command=view)
view_button.grid(column=1, row=3)

remove_button = Button(text="Remove", command=remove)
remove_button.grid(column=2, row=3)

window.mainloop()
