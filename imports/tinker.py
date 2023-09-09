import tkinter
import tkinter .messagebox

root = tkinter.Tk()
root.title("To-Do List")

def add_task():
  task = entry_task.get()
  if task != "":
    listbox_tasks.insert(tkinter.END, task)
    entry_task.delete(0, tkinter.END)
  else:
    tkinter.messagebox.showwarning(title="Warning", message="You must enter a task")

#Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

root.mainloop()