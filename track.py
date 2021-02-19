section_a = ['1', '2', '3', '4', '5']
section_b = ['6b', '7b', '8b', '9b', '10b', '11b', '12b',
             '13b', '14b', '15b', '16b', '17b', '18b',
             '19b', '20b', '21b', '22b', '23b', '24b', '25b']
section_c = ['6c', '7c', '8c', '9c', '10c', '11c', '12c',
             '13c', '14c', '15c', '16c', '17c', '18c',
             '19c', '20c', '21c', '22c', '23c', '24c', '25c']
section_d = ['26', '27', '28', '29', '30']
import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open('C:/Users/noaha/PycharmProjects/NRM/images/NRM_P1.png')
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.grid(row=0, column=1)
root.mainloop()



