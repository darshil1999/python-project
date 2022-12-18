import tkinter
from PIL import Image, ImageTk
import random

# main window of application
root = tkinter.Tk()
root.geometry('800x800')
root.title('Roll the Dice')

# Blank label for space 
l0 = tkinter.Label(root, text="")
l0.pack()

# Label window
l1 = tkinter.Label(root, text="Hey!", font = "Helvetica 16 bold italic")
l1.pack()

# Image list
dice = ['d1.png', 'd2.png', 'd3.png', 'd4.png', 'd5.png', 'd6.png']
# Using random function selecting a random image from 1-6 numbers on dice
img1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# label for image
label1 = tkinter.Label(root, image=img1)
label1.image = img1
label1.pack( expand=True)

# function to define a command which selects image
def dice_roll():
    img1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # Updating image
    label1.config(image=img1)
    label1.image = img1
    
# button for roll the dice
btn = tkinter.Button(root, text='Roll the Dice', fg='blue', command=dice_roll)
btn.pack( expand=True)

# Mainloop which keeps the window open
root.mainloop()