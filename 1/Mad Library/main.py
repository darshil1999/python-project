#  import modules

from tkinter import *

#  window

root = Tk()
root.geometry('300x300')
root.title('Mad Lib Generator')
Label(root, text='Mad Lib Generator \n Enjoy!', font='arial 20 bold').pack()
Label(root, text='Select any One: ', font='arial 16 bold').place(x=40, y=80)

# necessary functions

def madlib1():
    animal= input("Enter your favourite animal: ")
    profession = input("Enter your profession: ")
    cloth = input("Enter your favourite cloth: ")
    thing = input("Enter your favourite thing: ")
    name = input("Enter your name: ")
    place = input("Enter your favourite place: ")
    verb = input("Enter your favourite verb: ")
    food = input("Enter your favourite food: ")
    
    print(f"Say {food}, the photographer said as the camera flashed! {name} and I had gone to {place} to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as {animal} pretending to be a {profession}. When we saw the second photo, it was exactly what I wanted. We both looked like {thing} wearing {cloth} and {verb} --exactly what I had in mind")

def madlib2():
    adj = input('Enter adjactive: ')
    color = input("enter a color: ")
    thing = input("Enter a thing: ")
    place = input("Enter a place: ")
    person = input("Enter a person name: ")
    adj1 = input("Enter an adjactive: ")
    insect = input("Enter a insect name: ")
    food = input("Enter a food name: ")
    verb = input("Enter a verb: ")
    
    print(f"Last night I dreamed I was a {adj} butterfly with {color} splocthes tha looked like {thing}. I flew to {place} with my bestfriend and {person} who was a {adj1} {insect}. We ate some {food} when we got there and then decided to {verb} and the dream ended when I said --let's {verb}.")

def madlib3():
    person = input("Enter person name: ")
    color = input("Enter color: ")
    food = input("Enter food: ")
    adj = input("Enter adjactive: ")
    thing = input("Enter thing: ")
    place = input("Enter place: ")
    verb = input("Enter verb: ")
    adverb = input("Enter adverb: ")
    food1 = input("Enter food: ")
    thing1 = input("Enter thing: ")
    
    print(f"Today we picked apple from {person}'s orchad. I had no idea there were so many different varieties of apples. I ate {color} apples straight off the tree that tested like {food}. Then there was {adj} apple that looked like a {thing}. When our bag were full, we went on a free hay ride to {place} and back. It ended at a hay pile where we got to {verb} {adverb}. I can hardly wait to get home and cook with the apples. We are going to make appple {food1} and {thing1} pies!.")

#  necessary buttons

Button(root, text='The photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)
Button(root, text='apple and apple', font='arial 15', command=madlib2, bg='ghost white').place(x=70, y=180)
Button(root, text='The butterfly', font='arial 15', command=madlib3, bg='ghost white').place(x=80, y=240)


root.mainloop()