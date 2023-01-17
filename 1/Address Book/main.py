from tkinter import *

###### UI ######

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Address Book")

name = StringVar()
num = StringVar()

frame = Frame(root)
frame.pack(side= RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=10)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

###### Functions ######

contact_lst =[]

def selected():
    return int(select.curselection()[0])

def select_set():
    contact_lst.sort()
    select.delete(0,END)
    for name, num in contact_lst:
        select.insert(END, name)

def addcontact():
    contact_lst.append([name.get(), num.get()])
    select_set()

def editcontact():
    contact_lst[selected()] = [name.get(), num.get()]
    select_set()

def deletecontact():
    del contact_lst[selected()]
    select_set()

def viewcontact():
    name, num = contact_lst[selected()]
    name.set(name)
    num.set(num)

def exit():
    root.destroy()

def reset():
    name.set("")
    num.set("")

select_set()

Label(root, text="Name", font='arial 12 bold').place(x=30, y=20)
Entry(root, textvariable= name).place(x = 100, y =20)

Label(root, text="Number", font='arial 12 bold').place(x=30, y=70)
Entry(root, textvariable= num).place(x = 100, y =70)

Button(root, text="Add", font='arial 12 bold', width=5, command=addcontact).place(x=50, y=110)
Button(root, text="Edit", font='arial 12 bold', width=5, command=editcontact).place(x=50, y=260)
Button(root, text="Delete", font='arial 12 bold', width=5, command=deletecontact).place(x=50, y=210)
Button(root, text="View", font='arial 12 bold', width=5, command=viewcontact).place(x=50, y=160)
Button(root, text="Exit", font='arial 12 bold', width=5, command=exit).place(x=300, y=320)
Button(root, text="Reset", font='arial 12 bold', width=5, command=reset).place(x=50, y=310)

root.mainloop()
