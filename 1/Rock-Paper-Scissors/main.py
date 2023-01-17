from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title('Rock Paper Scissoors')

Label(root, text='Rock, Paper, Scissors', font='arial 20 bold').pack()

user = StringVar()
Label(root, text='Choose one: rock, paper, scissoors', font='arial 15 bold').place(x=20, y=70)
Entry(root, font = 'arial 15', textvariable=user).place(x=90, y=130)

comp_inp = random.randint(1,3)
if comp_inp == 1:
    comp_inp = 'rock'

elif comp_inp == 2:
    comp_inp = 'paper'

else:
    comp_inp = 'scissors'


result = StringVar()

def play():
    user_inp = user.get()
    if user_inp == comp_inp:
        result.set('Tie, No one won No one loose')
    elif user_inp == 'rock' and comp_inp == 'paper':
        result.set('You loose to paper.')
    elif user_inp == 'rock' and comp_inp == 'scissors':
        result.set('You won to scissors.')
    elif user_inp == 'paper' and comp_inp == 'rock':
        result.set('You lose to rock.')
    elif user_inp == 'paper' and comp_inp == 'scissors':
        result.set('You won to scissors.')
    elif user_inp == 'scissors' and comp_inp == 'rock':
        result.set('You lose to rock.')
    elif user_inp == 'scissors' and comp_inp == 'paper':
        result.set('You won to paper.')
    else:
        result.set('You need to select anyone - rock, paper, scissore')

def reset():
    result.set('')
    user.set('')

def exit():
    root.destroy()

Entry(root, font='arail 10 bold', textvariable= result, width=40).place(x=25,y =250)

Button(root, font='arial 13 bold', text = 'Play',width=10, padx = 5, command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='Reset',width=10, padx = 5, command=reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='Exit', width = 10, padx = 5, command=exit).place(x= 230, y=310)

root.mainloop()
