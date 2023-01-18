from plyer import notification
from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.geometry("300x300")
root.title("Countdown Timer and Notification")

def timer():
    try:
        timer_time = int(hour_entry.get())*3600 + int(min_entry.get())*60 + int(sec_entry.get())

    except:
        messagebox.showerror(message="Enter valid tim formate")

    if timer_time > 0:
        hour =0
        min = 0
        sec = 0

        while timer_time >= 0:
            min, sec = divmod(timer_time, 60)
            if min > 60:
                hour, min = divmod(min, 60)

            hours.set(hour)
            mins.set(min)
            secs.set(sec)
            time.sleep(1)
            root.update()
            timer_time -= 1

        notification.notify(
                title="Timer Alert",
                message="Set a timer for now and keep focus.",
                timeout = 30
            )

        messagebox.showinfo(message="Timer Complete!")

def h_click(event):
    hour_entry.delete(0,'end')

def m_click(event):
    min_entry.delete(0,'end')

def s_click(event):
    sec_entry.delete(0,'end')


Label(root, text="Countdown timer with notification", font=("Gayathri", 11)).pack()
Label(root, text="If not in use put '0' in fields", font=("Gayathri", 10)).pack()

hours = IntVar()
mins = IntVar()
secs = IntVar()

hour_entry = Entry(root, width=3, textvariable=hours, font=("Ubuntu Mono", 18))
min_entry = Entry(root, width=3, textvariable=mins, font=("Ubuntu Mono", 18))
sec_entry = Entry(root, width=3, textvariable=secs, font=("Ubuntu Mono", 18))

hour_entry.insert(0,00)
min_entry.insert(0,00)
sec_entry.insert(0,00)

hour_entry.place(x=80,y=40)
min_entry.place(x=130,y=40)
sec_entry.place(x=180,y=40)

hour_entry.bind("<1>", h_click)
min_entry.bind("<1>", m_click)
sec_entry.bind("<1>", s_click)

btn = Button(root, text ="Activate Timer", command=timer).pack(pady=40)

root.mainloop()