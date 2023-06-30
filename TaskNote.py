
from tkinter import *

root = Tk()
root.title("planB")
root.geometry("400x650+400+100")
root.resizable(False, False)

taskList = []


def Deletetask():
    global taskList
    task = str(listBox.get(ANCHOR))
    if task in taskList:
        taskList.remove(task)
        with open("tasklist.txt", "w") as tasksfile:
            for task in taskList:
                tasksfile.write(task + "\n")
            listBox.delete(ANCHOR)


def addTask():
    task = taskEntry.get()
    taskEntry.delete(0, END)
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
            taskList.append(task)
            listBox.insert(END, task)


def openTaskFile():
    try:
        with open("tasklist.txt", "r") as taskfie:
            tasks = taskfie.readlines()
        for task in tasks:
            if task != '\n':
                taskList.append(task)
                listBox.insert(END, task)
    except:
        file = open("tasklist.txt", 'w')
        file.close()


# main icon
main_icon = PhotoImage(file="images/completed-task.png")
root.iconphoto(False, main_icon)
# #top bar icon
# topBar= PhotoImage(file="images/kindpng_87498.png")
# Label(root,image= topBar).place(x=20,y=0)
frameTopBar = Frame(root, width=400, height=70, bg="#1b95e8", border=0)
frameTopBar.place(x=0, y=0)
heading = Label(root, text="YoUr dAiLy TaSk", font="arial 20 bold", fg="white", bg="#075a93")
heading.place(x=85, y=20)
# noteImage = PhotoImage(file="images/completed-task.png")
#
# Label(frameTopBar,image=noteImage, bg="#32405b").place(x=200,y=10)
# main
frame = Frame(root, width=400, height=50, bg="#fff")
frame.place(x=0, y=100)
task = StringVar()
taskEntry = Entry(frame, width=18, font="arial 16", bd=0)
taskEntry.place(x=10, y=7)
taskEntry.focus()
# lets add button
addPng = PhotoImage(file="images/more1.png")
addBtn = Button(frame, text="ADD", bg="#075a93", fg="white", font="arial 17 bold", border=0, bd=0,
                command=addTask).place(x=330, y=0)
# Addbtn= Button(frame,image=addPng, font="20")
# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))
frame1.place(x=10, y=220)
listBox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#ccc", fg="white", cursor="hand2",
                  selectbackground="#075a93")
listBox.pack(side=LEFT, fill=BOTH, padx=3)
scroll = Scrollbar(frame1)
scroll.pack(side=RIGHT, fill=BOTH)
listBox.config(yscrollcommand=scroll.set)
scroll.config(command=listBox.yview)
openTaskFile()
Deleteimg = PhotoImage(file="images/delete1.png")
Button(root, image=Deleteimg, bd=0, command=Deletetask).pack(side=BOTTOM, pady=13)
root.mainloop()
