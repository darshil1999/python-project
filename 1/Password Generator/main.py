from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Password Generator")

heading = Label(root, text="PASSWORD GENERATOR", font='arial 15 bold').pack()


pass_label = Label(root, text="Password Length", font="arial 10 bold").pack()
pass_len = IntVar()
length = Spinbox(root, from_=7,to_=32, textvariable=pass_len, width=15).pack()


pass_str = StringVar()

def generate():
    password = ''
    for i in range(0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)

    for i in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)

    pass_str.set(password)

Button(root, text="Generate Password" , command=generate).pack(pady=5)

Entry(root, textvariable=pass_str).pack()

def  copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text="Copy Password to Clipboard", command=copy_password).pack(pady=5)


root.mainloop()