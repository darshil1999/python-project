from tkinter import *
import parser
from math import factorial

##### UI ######
root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(rows=1, columnspan=6,sticky=N+E+W+S)

Button(root, text="1",command= lambda : get_variables(1)).grid(row=2, column=0,sticky=N+S+E+W)
Button(root, text="2",command= lambda : get_variables(2)).grid(row=2, column=1,sticky=N+S+E+W)
Button(root, text="3",command= lambda : get_variables(3)).grid(row=2, column=2,sticky=N+S+E+W)

Button(root, text="4",command= lambda : get_variables(4)).grid(row=3, column=0,sticky=N+S+E+W)
Button(root, text="5",command= lambda : get_variables(5)).grid(row=3, column=1,sticky=N+S+E+W)
Button(root, text="6",command= lambda : get_variables(6)).grid(row=3, column=2,sticky=N+S+E+W)

Button(root, text="7",command= lambda : get_variables(7)).grid(row=4, column=0,sticky=N+S+E+W)
Button(root, text="8",command= lambda : get_variables(8)).grid(row=4, column=1,sticky=N+S+E+W)
Button(root, text="9",command= lambda : get_variables(9)).grid(row=4, column=2,sticky=N+S+E+W)

Button(root, text="AC",command= lambda : clear_all()).grid(row=5, column=0,sticky=N+S+E+W)
Button(root, text="0",command= lambda : get_variables(8)).grid(row=5, column=1,sticky=N+S+E+W)
Button(root, text=".",command= lambda : get_variables(9)).grid(row=5, column=2,sticky=N+S+E+W)

Button(root, text="+",command= lambda : get_operation("+")).grid(row=2, column=3,sticky=N+S+E+W)
Button(root, text="-",command= lambda : get_operation("-")).grid(row=3, column=3,sticky=N+S+E+W)
Button(root, text="*",command= lambda : get_operation("*")).grid(row=4, column=3,sticky=N+S+E+W)
Button(root, text="/",command= lambda : get_operation("/")).grid(row=5, column=3,sticky=N+S+E+W)

Button(root, text="pi",command= lambda : get_operation("*3.14")).grid(row=2, column=4,sticky=N+S+E+W)
Button(root, text="%",command= lambda : get_operation("%")).grid(row=3, column=4,sticky=N+S+E+W)
Button(root, text="(",command= lambda : get_operation("(")).grid(row=4, column=4,sticky=N+S+E+W)
Button(root, text="Exp",command= lambda : get_operation("**")).grid(row=5, column=4,sticky=N+S+E+W)

Button(root, text="<-",command= lambda : undo()).grid(row=2, column=5,sticky=N+S+E+W)
Button(root, text="X!",command= lambda : fact()).grid(row=3, column=5,sticky=N+S+E+W)
Button(root, text=")",command= lambda : get_operation(")")).grid(row=4, column=5,sticky=N+S+E+W)
Button(root, text="^2",command= lambda : get_operation("**2")).grid(row=5, column=5,sticky=N+S+E+W)
Button(root, text="**2",command= lambda : get_operation("**2")).grid(row=5, column=5,sticky=N+S+E+W)
Button(root, text="=",command= lambda : calculate()).grid(columnspan=6,sticky=N+S+E+W)

root.mainloop()

###### Global Variable ######
i = 0

###### Get Values ######
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

###### Calculating Input Values ######
def calculate():
    entire_values = display.get()
    try:
        a = parser.expr(entire_values).compile()
        result = eval(a)
        clear_all()
        display.set(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

###### Clear Display ######
def clear_all():
    display.delete(0, END)

###### Undo Functions ######
def undo():
    entire_values = display.get()
    if len(entire_values):
        new_value = entire_values[::-1]
        clear_all()
        display.insert(0, new_value)
    else:
        clear_all()
        display.insert(0, "Error")

###### Mathematical Operations ######
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

###### Factorial Function ######
def fact():
    entire_value = display.get()
    try:
        result = factorial(int(entire_value))
        clear_all()
        display.insert(0,result)
    except:
        clear_all()
        display.insert(0,"Error")