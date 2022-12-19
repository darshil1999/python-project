# Impotting libraries
from tkinter import *
import base64

# main root app for UI
root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title('Message Encoder and Decoder')

# label 1 fot title
Label(root, text="Message Encoder and Decoder", font='arial 20 bold').pack()

# defining variable
txt = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

# Encoding function
def Encoder(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc.append(chr(ord(msg[i]) + ord(key_c) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Decoding function
def Decoder(key,msg):
    dec=[]
    msg = base64.urlsafe_b64decode(msg).decode()
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(msg[i]) - ord(key_c)) % 256))
    return "".join(dec)

# Mode selection function
def mode_type():
    if (mode.get() == 'e'):
        result.set(Encoder(private_key.get(), txt.get()))
    elif (mode.get() == 'd'):
        result.set(Decoder(private_key.get(), txt.get()))
    else:
        result.set('Invalid Input Mode')

def exit():
    root.destroy()

# Reseting all values in app
def reset():
    txt.set('')
    private_key.set('')
    mode.set('')
    result.set('')

# for message       
Label(root, font = 'arial 12 bold', text = 'Message').place(x=60,y=60)
Entry(root, font = 'arial 12 bold', textvariable=txt, bg = 'ghost white').place(x = 290, y = 60)

# for key
Label(root, font='arial 12 bold', text='Key').place(x = 60, y = 90)
Entry(root, font = 'arial 12 bold', textvariable=private_key, bg = 'ghost white').place(x =290, y = 90)

# for mode
Label(root, font='arial 12 bold', text='Mode(e/d)').place(x = 60, y = 120)
Entry(root, font = 'arial 12 bold', textvariable=mode, bg = 'ghost white').place(x =290, y = 120)

# result
Entry(root, font = 'arial 10 bold', textvariable = result, bg ='ghost white').place(x=290, y = 150)

# result button
Button(root, font = 'arial 10 bold', text = 'RESULT', padx =2, bg ='LightGray', command = mode_type).place(x=60, y = 150)

#reset button
Button(root, font = 'arial 10 bold', text ='RESET', width =6, command = reset, bg = 'LimeGreen', padx=2).place(x=80, y = 190)

#exit button
Button(root, font = 'arial 10 bold', text= 'EXIT', width = 6, command = exit, bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

# hold the app
root.mainloop()