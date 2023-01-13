#  import library

from tkinter import *
import datetime
import time
from playsound import playsound

def alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime('%H:%M:%S')
        date = current_time.strftime('%Y-%m-%d')
        print(f"The set date is: {date}")
        print(now)
        if now == set_alarm:
            print("Times Up!")

            # for linux 
            playsound('./sound.mp3')
            
            # ## for windows
            # import winsound
            # ## Make sure you have sound.wav in current working directory
            # winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

clock = Tk()
clock.title('Alarm Clock')
clock.geometry('400x200')
time_format = Label(clock, text="Enter TIme in 24 hour format!", fg="yellow", bg="black", font="arial").place(x=60, y=120)
addTime = Label(clock, text="Hour Min Sec",font=60).place(x=110)
setAlarm = Label(clock, text="Set time", fg="red" ,font=('Helevetica',7,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="blue", width="15").place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="blue", width="15").place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="blue", width="15").place(x=190, y=30)

submit = Button(clock, text="Set Alarm", fg="black", bg="black", width=10, command=actual_time).place(x=110, y=70)

clock.mainloop()