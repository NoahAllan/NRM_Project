# **NOTE**
# This file is to test the GUI before it is put into the main program (main.py)

# imports
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
root.nrm1 = ImageTk.PhotoImage(Image.open(NRM_1))
root.nrm2 = ImageTk.PhotoImage(Image.open(NRM_2))
root.nrm3 = ImageTk.PhotoImage(Image.open(NRM_3))
root.nrm4 = ImageTk.PhotoImage(Image.open(NRM_4))
root.nrm5 = ImageTk.PhotoImage(Image.open(NRM_5))
root.nrm6 = ImageTk.PhotoImage(Image.open(NRM_6))
root.nrm7 = ImageTk.PhotoImage(Image.open(NRM_7))
root.nrm8 = ImageTk.PhotoImage(Image.open(NRM_8))
root.nrm9 = ImageTk.PhotoImage(Image.open(NRM_9))
root.nrm10 = ImageTk.PhotoImage(Image.open(NRM_10))
root.nrm11 = ImageTk.PhotoImage(Image.open(NRM_11))
root.nrm12 = ImageTk.PhotoImage(Image.open(NRM_12))
root.nrm13 = ImageTk.PhotoImage(Image.open(NRM_13))
root.nrm14 = ImageTk.PhotoImage(Image.open(NRM_14))
root.nrm15 = ImageTk.PhotoImage(Image.open(NRM_15))
root.nrm16 = ImageTk.PhotoImage(Image.open(NRM_16))
root.nrm17 = ImageTk.PhotoImage(Image.open(NRM_17))
root.nrm18 = ImageTk.PhotoImage(Image.open(NRM_18))
root.nrm19 = ImageTk.PhotoImage(Image.open(NRM_19))
root.nrm20 = ImageTk.PhotoImage(Image.open(NRM_20))
root.nrm21 = ImageTk.PhotoImage(Image.open(NRM_21))
root.nrm22 = ImageTk.PhotoImage(Image.open(NRM_22))
root.nrm23 = ImageTk.PhotoImage(Image.open(NRM_23))
root.nrm24 = ImageTk.PhotoImage(Image.open(NRM_24))
root.nrm25 = ImageTk.PhotoImage(Image.open(NRM_25))
root.nrm26 = ImageTk.PhotoImage(Image.open(NRM_26))
root.nrm27 = ImageTk.PhotoImage(Image.open(NRM_27))
root.nrm28 = ImageTk.PhotoImage(Image.open(NRM_28))
root.nrm29 = ImageTk.PhotoImage(Image.open(NRM_29))
root.nrm30 = ImageTk.PhotoImage(Image.open(NRM_30))
root.error = ImageTk.PhotoImage(Image.open(Error_Screen))

Verdana = Font(family="Verdana", size=12)
VerdanaL = Font(family="Verdana", size=8)


def raise_frame(tk_frame):
    tk_frame.tkraise()


f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
download = Frame(root)

for frame in (f0, f1, f2, f3, download):
    frame.grid(row=0, column=0, sticky='news')


def change_pic():
    photo_.configure(image=root.nrm2)


def close():
    root.destroy()


def control_panel():
    pass


def black_box():
    pass


def test():
    pass


Control_Panel = Button(f0, text="CONTROL\nPANEL", width=w, height=h, command=lambda: raise_frame(f1), font=VerdanaL). \
    grid(row=3, column=0)
Black_Box = Button(f0, text="BLACK\nBOX", width=w, height=h, command=lambda: raise_frame(f2), font=VerdanaL). \
    grid(row=3, column=1)
Test = Button(f0, text="TEST", width=w, height=h, command=lambda: raise_frame(f3), font=VerdanaL).grid(row=3, column=2)
Quit = Button(f0, text="QUIT", width=w, height=h, command=close, font=VerdanaL).grid(row=3, column=3)
photo_ = Label(f0, image=root.nrm1)
photo_.grid(row=0, column=0, columnspan=4)

Check_Sensors = Button(f1, text="CHECK SENSORS", width=w, height=h, command=control_panel, font=VerdanaL). \
    grid(row=3, column=0)
Check_Points = Button(f1, text="CHECK POINTS", width=w, height=h, command=black_box, font=VerdanaL). \
    grid(row=3, column=1)
Check_Signals = Button(f1, text="CHECK SIGNALS", width=w, height=h, command=test, font=VerdanaL).grid(row=3, column=2)
Leave = Button(f1, text="RETURN", width=w, height=h, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=3)
photo_1 = Label(f1, image=root.error)
photo_1.grid(row=0, column=0, columnspan=4)

Read_last = Button(f2, text="READ LAST\nINPUT", width=w, height=h, command=control_panel, font=VerdanaL). \
    grid(row=3, column=0)
Download = Button(f2, text="DOWNLOAD ALL", width=w, height=h, command=lambda: raise_frame(download), font=VerdanaL). \
    grid(row=3, column=1)
Clear = Button(f2, text="CLEAR\nBLACK BOX", width=w, height=h, command=test, font=VerdanaL).grid(row=3, column=2)
Leave_1 = Button(f2, text="RETURN", width=w, height=h, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=3)
photo_2 = Label(f2, image=root.error)
photo_2.grid(row=0, column=0, columnspan=4)

Run_Through = Button(f3, text="Test System", width=27, height=h, command=control_panel, font=VerdanaL). \
    grid(row=3, column=0)
Leave_2 = Button(f3, text="RETURN", width=27, height=h, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=3)
photo_3 = Label(f3, image=root.error)
photo_3.grid(row=0, column=0, columnspan=4)


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

