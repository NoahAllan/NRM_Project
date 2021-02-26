# **NOTE**
# This file is to test the GUI before it is put into the main program (main.py)

# imports
import time
from shutil import copyfile
from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from track import *
from main import sensor_data
import threading

pos = ''
root = Tk()
w = 13
h = 8
global end_loop
stop_threads = False
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
v = 0.2
route_1 = section_a + section_c + section_d
route_two = section_a + section_b + section_d

route_2 = route_two[::-1]


def find_train_position():
    global pos
    f = open('train_data.txt', 'r')
    pos = f.readlines(0-1)
    f.close()


def raise_frame(tk_frame):
    tk_frame.tkraise()


f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
download = Frame(root)

for frame in (f0, f1, f2, f3, download):
    frame.grid(row=0, column=0, sticky='news')


def end_code():
    end_loop = True


def close():
    root.destroy()


def control_panel():
    pass


def black_box():
    pass


def test():
    pass


def constant_run():
    end_loop = False
    emergency_stop = False
    l3: bool = True
    try:
        find_train_position()
        scotsman_current_position = pos[0]
        mallard_current_position = pos[1]
        x = int(pos[0].replace('c', '').replace('b', '')) - 1
        y = int(pos[0].replace('c', '').replace('b', '')) - 1
    except:
        scotsman_current_position = 1
        mallard_current_position = 30
        x = 0
        y = 0
    while l3 is True:
        # x = 0
        # y = 0
        l4 = True
        l5 = True
        while l4 is True and emergency_stop is False:

            sensor_data[1] = False
            sensor_data[2] = False
            sensor_data[3] = False
            sensor_data[4] = False

            print(f'Scotsman is at position - {scotsman_current_position}')
            print(f'Mallard is at position - {mallard_current_position}')
            time.sleep(v)
            time.sleep(0.2)
            x += 1
            if x == 30:
                break
            scotsman_current_position = route_1[x]
            mallard_current_position = route_2[x]
            if scotsman_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif scotsman_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif scotsman_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif scotsman_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif scotsman_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif scotsman_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif scotsman_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif scotsman_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif scotsman_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif scotsman_current_position == '30':
                photo_1.configure(image=root.nrm30)
            if mallard_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif mallard_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif mallard_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif mallard_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif mallard_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif mallard_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif mallard_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif mallard_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif mallard_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif mallard_current_position == '30':
                photo_1.configure(image=root.nrm30)
            if scotsman_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif scotsman_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif scotsman_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif scotsman_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif scotsman_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif scotsman_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif scotsman_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif scotsman_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif scotsman_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif scotsman_current_position == '30':
                photo_1.configure(image=root.nrm30)
            if mallard_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif mallard_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif mallard_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif mallard_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif mallard_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif mallard_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif mallard_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif mallard_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif mallard_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif mallard_current_position == '30':
                photo_1.configure(image=root.nrm30)
            f = open('train_data.txt', 'a')
            f.truncate(0)
            f.writelines(f'{scotsman_current_position}\n{mallard_current_position}\n')
            f.close()
        x = 0
        y = 0
        if end_loop:
            break
        while l5 is True and emergency_stop is False:
            sensor_data[1] = False
            sensor_data[2] = False
            sensor_data[3] = False
            sensor_data[4] = False
            print(f'Scotsman is at position - {scotsman_current_position}')
            print(f'Mallard is at position - {mallard_current_position}')

            time.sleep(v)
            time.sleep(0.2)
            y += 1
            if y == 30:
                break
            scotsman_current_position = route_2[y]
            mallard_current_position = route_1[y]
            if scotsman_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif scotsman_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif scotsman_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif scotsman_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif scotsman_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif scotsman_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif scotsman_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif scotsman_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif scotsman_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif scotsman_current_position == '30':
                photo_1.configure(image=root.nrm30)
            if mallard_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif mallard_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif mallard_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif mallard_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif mallard_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif mallard_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif mallard_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif mallard_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif mallard_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif mallard_current_position == '30':
                photo_1.configure(image=root.nrm30)
            if scotsman_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif scotsman_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif scotsman_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif scotsman_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif scotsman_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif scotsman_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif scotsman_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif scotsman_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif scotsman_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif scotsman_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif scotsman_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif scotsman_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif scotsman_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif scotsman_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif scotsman_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif scotsman_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif scotsman_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif scotsman_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif scotsman_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif scotsman_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif scotsman_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif scotsman_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif scotsman_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif scotsman_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif scotsman_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif scotsman_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif scotsman_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif scotsman_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif scotsman_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif scotsman_current_position == '30':
                photo_1.configure(image=root.nrm30)
            if mallard_current_position == '1':
                photo_1.configure(image=root.nrm1)
            elif mallard_current_position == '2':
                photo_1.configure(image=root.nrm2)
            elif mallard_current_position == '3':
                sensor_data[0] = not sensor_data[0]
                photo_1.configure(image=root.nrm3)
            elif mallard_current_position == '4':
                photo_1.configure(image=root.nrm4)
            elif mallard_current_position == '5':
                photo_1.configure(image=root.nrm5)
            elif mallard_current_position == '6b':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '6c':
                photo_1.configure(image=root.nrm6)
            elif mallard_current_position == '7b':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '7c':
                photo_1.configure(image=root.nrm7)
            elif mallard_current_position == '8b':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '8c':
                photo_1.configure(image=root.nrm8)
            elif mallard_current_position == '9b':
                sensor_data[1] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '9c':
                sensor_data[2] = True
                photo_1.configure(image=root.nrm9)
            elif mallard_current_position == '10b':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '10c':
                photo_1.configure(image=root.nrm10)
            elif mallard_current_position == '11b':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '11c':
                photo_1.configure(image=root.nrm11)
            elif mallard_current_position == '12b':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '12c':
                photo_1.configure(image=root.nrm12)
            elif mallard_current_position == '13b':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '13c':
                photo_1.configure(image=root.nrm13)
            elif mallard_current_position == '14b':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '14c':
                photo_1.configure(image=root.nrm14)
            elif mallard_current_position == '15b':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '15c':
                photo_1.configure(image=root.nrm15)
            elif mallard_current_position == '16b':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '16c':
                photo_1.configure(image=root.nrm16)
            elif mallard_current_position == '17b':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '17c':
                photo_1.configure(image=root.nrm17)
            elif mallard_current_position == '18b':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '18c':
                photo_1.configure(image=root.nrm18)
            elif mallard_current_position == '19b':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '19c':
                photo_1.configure(image=root.nrm19)
            elif mallard_current_position == '20b':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '20c':
                photo_1.configure(image=root.nrm20)
            elif mallard_current_position == '21b':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '21c':
                photo_1.configure(image=root.nrm21)
            elif mallard_current_position == '22b':
                sensor_data[3] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '22c':
                sensor_data[4] = True
                photo_1.configure(image=root.nrm22)
            elif mallard_current_position == '23b':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '23c':
                photo_1.configure(image=root.nrm23)
            elif mallard_current_position == '24b':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '24c':
                photo_1.configure(image=root.nrm24)
            elif mallard_current_position == '25b':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '25c':
                photo_1.configure(image=root.nrm25)
            elif mallard_current_position == '26':
                photo_1.configure(image=root.nrm26)
            elif mallard_current_position == '27':
                photo_1.configure(image=root.nrm27)
            elif mallard_current_position == '28':
                sensor_data[5] = not sensor_data[5]
                photo_1.configure(image=root.nrm28)
            elif mallard_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif mallard_current_position == '30':
                photo_1.configure(image=root.nrm30)
            f = open('train_data.txt', 'a')
            f.truncate(0)
            f.writelines(f'{scotsman_current_position}\n{mallard_current_position}\n')
            f.close()


def run():
    global p
    p = threading.Thread(target=constant_run)
    p.daemon = True
    p.start()


def switch():
    Start_Sim.configure(command=lambda: [return_train(), close()], text='STOP')


def return_train():
    f = open('train_data.txt', 'a')
    f.truncate(0)
    f.writelines(f'1\n30\n')
    f.close()


w1 = 27
h1 = 11
Control_Panel = Button(f0, text="CONTROL\nPANEL", width=w1, height=h1, command=lambda: raise_frame(f1),
                       font=VerdanaL).grid(row=0, column=0, sticky='nsew')
Black_Box = Button(f0, text="BLACK\nBOX", width=w1, height=h1, command=lambda: raise_frame(f2), font=VerdanaL). \
    grid(row=0, column=1, sticky='nsew')
Test = Button(f0, text="TEST", width=w1, height=h1, command=lambda: raise_frame(f3), font=VerdanaL).\
    grid(row=1, column=0, sticky='nsew')
Quit = Button(f0, text="QUIT", width=w1, height=h1, command=close, font=VerdanaL).grid(row=1, column=1, sticky='nsew')

Check_Sensors = Button(f1, text="CHECK\nSENSORS", width=w, height=h, command=control_panel, font=VerdanaL). \
    grid(row=3, column=0)  # TODO: Write code to check sensors and display it in the GUI
Check_Points = Button(f1, text="CHECK\nPOINTS", width=w, height=h, command=test, font=VerdanaL). \
    grid(row=3, column=1)  # TODO: Write code to check points and display it in the GUI
Start_Sim = Button(f1, text="START", width=w, height=h, command=lambda: [run(), switch()], state=NORMAL, font=VerdanaL)
Start_Sim.grid(row=3, column=2)
Leave = Button(f1, text="RETURN", width=w, height=h, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=3)
photo_1 = Label(f1, image=root.error)
photo_1.grid(row=0, column=0, columnspan=4)

Read_last = Button(f2, text="READ LAST\nINPUT", width=w, height=h, command=control_panel, font=VerdanaL). \
    grid(row=3, column=0)   # TODO: Write code to read last input and display it in the GUI
Download = Button(f2, text="DOWNLOAD ALL", width=w, height=h, command=lambda: raise_frame(download), font=VerdanaL). \
    grid(row=3, column=1)    # TODO: Write code to download the black box
Clear = Button(f2, text="CLEAR\nBLACK BOX", width=w, height=h, command=test, font=VerdanaL).grid(row=3, column=2)
# TODO: Write code to clear black box
Leave_1 = Button(f2, text="RETURN", width=w, height=h, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=3)
photo_2 = Label(f2, image=root.error)
photo_2.grid(row=0, column=0, columnspan=4)

Run_Through = Button(f3, text="Test System", width=27, height=h, command=control_panel, font=VerdanaL). \
    grid(row=3, column=0)
# TODO: Write code to test whole system and display it in the GUI (use code from constant run)
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