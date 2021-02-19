# **NOTE**
# This file is only to test small parts of the program
# This will have no impact on the final program

from shutil import copyfile
from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font

root = Tk()
w = 13
h = 8
root.title('NRM GUI')
root.geometry("400x300")
root.resizable(0, 0)
root.iconbitmap('C:/Users/noaha/PycharmProjects/NRM/images/StROMEROs_Logo.ico')
NRM_1 = 'images/NRM_P1.png'
NRM_2 = 'images/NRM_P2.png'
NRM_3 = 'images/NRM_P3.png'
NRM_4 = 'images/NRM_P4.png'
NRM_5 = 'images/NRM_P5.png'
NRM_6 = 'images/NRM_P6.png'
NRM_7 = 'images/NRM_P7.png'
NRM_8 = 'images/NRM_P8.png'
NRM_9 = 'images/NRM_P9.png'
NRM_10 = 'images/NRM_P10.png'
NRM_11 = 'images/NRM_P11.png'
NRM_12 = 'images/NRM_P12.png'
NRM_13 = 'images/NRM_P13.png'
NRM_14 = 'images/NRM_P14.png'
NRM_15 = 'images/NRM_P15.png'
NRM_16 = 'images/NRM_P16.png'
NRM_17 = 'images/NRM_P17.png'
NRM_18 = 'images/NRM_P18.png'
NRM_19 = 'images/NRM_P19.png'
NRM_20 = 'images/NRM_P20.png'
NRM_21 = 'images/NRM_P21.png'
NRM_22 = 'images/NRM_P22.png'
NRM_23 = 'images/NRM_P23.png'
NRM_24 = 'images/NRM_P24.png'
NRM_25 = 'images/NRM_P25.png'
NRM_26 = 'images/NRM_P5.png'
NRM_27 = 'images/NRM_P4.png'
NRM_28 = 'images/NRM_P3.png'
NRM_29 = 'images/NRM_P2.png'
NRM_30 = 'images/NRM_P1.png'
Error_Screen = 'images/ERROR_404.png'

Verdana = Font(family="Verdana", size=12)
VerdanaL = Font(family="Verdana", size=8)


def raise_frame(frame):
    frame.tkraise()


f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
download = Frame(root)

for frame in (f0, f1, f2, f3, download):
    frame.grid(row=0, column=0, sticky='news')


def close():
    root.destroy()


def control_panel():
    pass


def black_box():
    pass


def test():
    pass


Control_Panel = Button(f0, text="CONTROL\nPANEL", width=w, height=h, command=lambda: raise_frame(f1), font=VerdanaL).\
    grid(row=3, column=0)
Black_Box = Button(f0, text="BLACK\nBOX", width=w, height=h, command=lambda: raise_frame(f2), font=VerdanaL).\
    grid(row=3, column=1)
Test = Button(f0, text="TEST", width=w, height=h, command=lambda: raise_frame(f3), font=VerdanaL).grid(row=3, column=2)
Quit = Button(f0, text="QUIT", width=w, height=h, command=close, font=VerdanaL).grid(row=3, column=3)
image1 = Image.open(NRM_1)
image_ = ImageTk.PhotoImage(image1)
x = Label(f0, image=image_).grid(row=0, column=0, columnspan=4)


Check_Sensors = Button(f1, text="CHECK SENSORS", width=w, height=h, command=control_panel, font=VerdanaL).\
    grid(row=3, column=0)
Check_Points = Button(f1, text="CHECK POINTS", width=w, height=h, command=black_box, font=VerdanaL).\
    grid(row=3, column=1)
Check_Signals = Button(f1, text="CHECK SIGNALS", width=w, height=h, command=test, font=VerdanaL).grid(row=3, column=2)
Leave = Button(f1, text="RETURN", width=w, height=h, command=lambda: raise_frame(f0), font=VerdanaL).\
    grid(row=3, column=3)
image11 = Image.open(Error_Screen)
image_1 = ImageTk.PhotoImage(image11)
x1 = Label(f1, image=image_1).grid(row=0, column=0, columnspan=4)


Read_last = Button(f2, text="READ LAST\nINPUT", width=w, height=h, command=control_panel, font=VerdanaL).\
    grid(row=3, column=0)
Download = Button(f2, text="DOWNLOAD ALL", width=w, height=h, command=lambda: raise_frame(download), font=VerdanaL).\
    grid(row=3, column=1)
Clear = Button(f2, text="CLEAR\nBLACK BOX", width=w, height=h, command=test, font=VerdanaL).grid(row=3, column=2)
Leave_1 = Button(f2, text="RETURN", width=w, height=h, command=lambda: raise_frame(f0), font=VerdanaL).\
    grid(row=3, column=3)
image12 = Image.open(Error_Screen)
image_2 = ImageTk.PhotoImage(image12)
x2 = Label(f2, image=image_2).grid(row=0, column=0, columnspan=4)


Run_Through = Button(f3, text="Test System", width=27, height=h, command=control_panel, font=VerdanaL).\
    grid(row=3, column=0)
Leave_2 = Button(f3, text="RETURN", width=27, height=h, command=lambda: raise_frame(f0), font=VerdanaL).\
    grid(row=3, column=3)
image13 = Image.open(Error_Screen)
image_3 = ImageTk.PhotoImage(image13)
x3 = Label(f3, image=image_3).grid(row=0, column=0, columnspan=4)


def download_black_box(event):
    file_dst = event.widget.get()
    event.widget.delete(0, len(file_dst))
    src = 't1'
    dst = f'{file_dst}blackbox.txt'
    try:
        f = open(dst, 'a')
        f.close()
        copyfile(src, dst)
    except Exception as e:
        print('Error: %s' % str(e))


lab = Label(download, text="Enter Location for Download:", font=Verdana)
lab.grid(row=0, column=0, pady=100, padx=100)

ent = Entry(download)
ent.grid(row=1, column=0)
ent.bind('<Return>', download_black_box)

raise_frame(f0)
root.mainloop()

