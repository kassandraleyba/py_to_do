import tkinter
import tkinter .messagebox

root = tkinter.Tk()
root.title("To-Do List")

#Create GUI
listbox_tasks = tkinter.Listbox(root, height=3, width=50)
listbox_tasks.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

root.mainloop()