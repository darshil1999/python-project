from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound

###### UI ######
root = Tk()
root.geometry("350x300")
root.resizable(0,0)
root.config(bg='ghost white')
root.title('Text To Speech')

###### Heading ######
Label(root, text='Text To Speech', font='arail 20 bold', bg='white smoke').pack()

###### Label ######
Label(root, text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20,y=60)

###### Variable ######
msg = StringVar()

###### Input ######
txt_entry = Entry(root, textvariable=msg, width='50')
txt_entry.place(x=20,y=60)

######################
#                    #
#      Function      #
#                    #
######################
def text_to_speech():
    try:
        message = txt_entry.get()
        speech = gTTS(text=message)
        speech.save('audio.mp3')
    except:
        messagebox.showerror('Inpur Error','Input is null')
    

def exit():
    root.destroy()

def reset():
    msg.set('')

###### Button ######
Button(root, text = "Play", font='arial 15 bold', command=text_to_speech,width=4).place(x=25, y=140)
Button(root, text = 'Exit', font='arial 15 bold', command=exit, bg='OrangeRed1').place(x=100,y=140)
Button(root, text = 'Reset', font='arial 15 bold', command=reset).place(x=175,y=140)


###### mainloop ######
root.mainloop()