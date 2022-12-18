import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice')

l0 = tkinter.Label(root, text="")
l0.pack()

l1 = tkinter.Label(root, text="Hey!", font = "Helvetica 16 bold italic")
l1.pack()

dice = ['d1.png', 'd2.png', 'd3.png', 'd4.png', 'd5.png', 'd6.png']

img1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=img1)
label1.image = img1

label1.pack( expand=True)

def dice_roll():
    img1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    
    label1.config(image=img1)
    
    label1.image = img1
    

btn = tkinter.Button(root, text='Roll the Dice', fg='blue', command=dice_roll)

btn.pack( expand=True)

root.mainloop()