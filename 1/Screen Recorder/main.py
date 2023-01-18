from PIL import ImageGrab
import cv2
import numpy as np
from tkinter import *

def record_screen():
    image = ImageGrab.grab()
    img_np_arr = np.array(image)
    shape =  img_np_arr.shape
    print(shape)

    screen_cap_writer = cv2.VideoWriter('screen_recorded.avi', cv2.VideoWriter_foutcc('M','J','P','G'), 50, (shape[1], shape[0]))

    scale_by_percent = 50
    width = int(shape[1] * scale_by_percent / 100)
    height = int(shape[0] * scale_by_percent / 100)

    new_dimension = (width, height)

    while True:
        image = ImageGrab.grab()
        img_np_arr = img_np_arr.array(image)
        final_image = cv2.cvtColor(img_np_arr, cv2.COLOR_RGB2BGR)

        screen_cap_writer.write(final_image)

        image = cv2.resize(final_image, (new_dimension))

        cv2.imshow("image", image)

        if cv2.waitkey(1) == ord('q'):
            break

        screen_cap_writer.release()
        cv2.destroyAllWindows()


root = Tk()
root.geometry("350x250")
root.title("Screen Recorder")

title_label = Label(root, text="Screen Recorder", font=("Ubuntu mono", 16))
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

info_label = Label(root, text="Enter 'q' to exit Screen Recording")
info_label.place(relx=0.5, rely=0.3, anchor=CENTER)

screen_button = Button(root, text="Record Screen", command=record_screen, relief=RAISED)
screen_button.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()