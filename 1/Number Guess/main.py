# import libraries

from tkinter import *
from tkinter import messagebox
import random

# variables
target = 0
score = 10
guess = 0

# clue functions
def add():
    return f"The sum of target and guess is {guess+target}"

def sub():
    return f"The difference of the target and guess is {target-guess}"

def mult():
    return f"The product of target and guess is {target*guess}"

def divi():
    return f"The division of target and guess is {target/guess}"

def greater_lesser():
    if target < guess:
        return "Target is less than the guess"
    elif target > guess:
        return "Target is greater than the guess"

# random clue generator
def clues():
    switcher = {
        0: add(),
        1: sub(),
        2: mult(),
        3: divi(),
        4: greater_lesser()
    }

    return switcher.get(random.randint(0,4))

# target value generate
def generate_target_number():
    global target
    target = random.randint(0,10)
    messagebox.showinfo(message="Random Number Generated; Start Guessing!! Starting score=10")

    random_num_btn['state'] = DISABLED

    guess_btn['state'] = NORMAL

def guess_score():
    global score
    global guess
    try:
        guess = 0

        guess = int(guess_entry.get())
    except:
        messagebox.showerror(message="Enter a number to guess and play")
        return

    if guess == target:
        messagebox.showinfo(message=f"Congratulations!! You guessed the number correct. Your score is {score}")

        random_num_btn['state'] = NORMAL
        guess_btn['state'] = DISABLED
        return

    elif score ==0:
        messagebox.showwarning(message="Oops! Out of guesses! Better luck next time")
        return
    else:
        score-=1

        message=clues()
        messagebox.showinfo(message=message)


root = Tk()
root.geometry("350x200")
root.title("Number Guessing Game")

title_label = Label(root, text="Number Guessing Game\nGuess a number between 1 to 50", font=('Ubuntu Mono',12))
title_label.pack()

random_num_btn = Button(root, text="Generate Random Number", command=generate_target_number)
random_num_btn.pack()

guess_label = Label(root, text="Enter your guess: ")
guess_label.pack()
guess_entry = Entry(root, width=3)
guess_entry.pack()

guess_btn = Button(root, text="Guess Me", command=guess_score, state=DISABLED)
guess_btn.pack()

root.mainloop()