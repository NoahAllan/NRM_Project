# imports
import time
from shutil import copyfile
from tkinter import *
from PIL import Image, ImageTk  # pip install Pillow
from tkinter.font import Font
from track import *
from tkinter import messagebox
import threading
import datetime

# assinging all variables
stop_threads = False
sensor_data: list[bool] = [False, False, False, False, False, False]
signal_data: list[bool] = [False, False, False, False, False, False]
Point_A: int = 0
Point_B: int = 0
Sig_a: str = ''
Sig_b: str = ''
Sig_c: str = ''
Sig_d: str = ''
Sig_e: str = ''
Sig_f: str = ''
date = ''
pos = ''
v = 0.2  # Should be 18 for correct timing.

# Creating route
route_1 = section_a + section_c + section_d
route_two = section_a + section_b + section_d
route_2 = route_two[::-1]

# GUI spesific assingments
width = 13
h = 8
root = Tk()
root.title('NRM GUI')
root.geometry('400x300')
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
Green_Light = 'images/Green_Circle.png'
Red_Light = 'images/Red_Circle.png'
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
root.green = ImageTk.PhotoImage(Image.open(Green_Light))
root.red = ImageTk.PhotoImage(Image.open(Red_Light))
Verdana = Font(family='Verdana', size=12)
VerdanaL = Font(family='Verdana', size=8)

# Structure for changeing pages
f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
download = Frame(root)
sensor = Frame(root)
point = Frame(root)
signal = Frame(root)

for frame in (f0, f1, f2, f3, download, sensor, point, signal):
    frame.grid(row=0, column=0, sticky='news')


    
class StringTransformation(object):
    def __init__(self, list_in):
        self.list_in = list_in

    @property
    def list_to_string(self):
        return self.list_in.replace('[', '').replace(']', '').replace('\\n', '').replace("'", '').replace(',', '\n').\
            replace('*--------------------------------------------*', '')


def find_date():
    global date
    x = datetime.datetime.today()
    date = x.strftime('%a %b %d %Y %H:%M:%S')


def point_change():
    global Point_A
    global Point_B

    s1 = sensor_data[0]
    s2 = sensor_data[1]
    s3 = sensor_data[2]
    s4 = sensor_data[3]
    s5 = sensor_data[4]
    s6 = sensor_data[5]

    if s1 is True:
        Point_A = 30
    if s2 is True:
        Point_B = 30
    if s3 is True:
        Point_A = 0
    if s4 is True:
        Point_B = 30
    if s5 is True:
        Point_A = 0
    if s6 is True:
        Point_B = 0


def find_train_position():
    global pos
    f = open('train_data.txt', 'r')
    pos = f.readlines(0 - 1)
    f.close()


def raise_frame(tk_frame):
    tk_frame.tkraise()


def bool_change(bool_input):
    if bool_input is True:
        bool_input = False
    elif bool_input is False:
        bool_input = True
    else:
        print(f'{bool_input} is not valid input')
    return bool_input


def close():
    root.destroy()


def outward_run():
    try:
        find_train_position()
        scotsman_current_position = pos[0]
        mallard_current_position = pos[1]
        x = int(pos[0].replace('c', '').replace('b', '')) - 1
    except:
        scotsman_current_position = 1
        mallard_current_position = 30
    x = 0

    while x != 30:
        print(f'Scotsman is at position - {scotsman_current_position}')
        print(f'Mallard is at position - {mallard_current_position}')
        x += 1
        if x == 30:
            break
        time.sleep(v)
        sensor_data[0] = False
        sensor_data[1] = False
        sensor_data[2] = False
        sensor_data[3] = False
        sensor_data[4] = False
        sensor_data[5] = False
        scotsman_current_position = route_1[x]
        mallard_current_position = route_2[x]
        if scotsman_current_position == '1':
            photo_1.configure(image=root.nrm1)
        elif scotsman_current_position == '2':
            photo_1.configure(image=root.nrm2)
        elif scotsman_current_position == '3':
            sensor_data[0] = True
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
            sensor_data[5] = True
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
            sensor_data[0] = True
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
            sensor_data[5] = True
            photo_1.configure(image=root.nrm28)
        elif mallard_current_position == '29':
            photo_1.configure(image=root.nrm29)
        elif mallard_current_position == '30':
            photo_1.configure(image=root.nrm30)


def constant_run():
    emergency_stop = False
    l3: bool = True
    try:
        find_train_position()
        scotsman_current_position = pos[0]
        mallard_current_position = pos[1]
        x = int(pos[0].replace('c', '').replace('b', '')) - 1
    except:
        scotsman_current_position = 1
        mallard_current_position = 30
        x = 0
    while l3 is True:
        l4 = True
        l5 = True
        while l4 is True and emergency_stop is False:
            sensor_data[0] = False
            sensor_data[1] = False
            sensor_data[2] = False
            sensor_data[3] = False
            sensor_data[4] = False
            sensor_data[5] = False

            print(f'Scotsman is at position - {scotsman_current_position}')
            print(f'Mallard is at position - {mallard_current_position}')
            time.sleep(v)
            x += 1
            if x != 30:
                scotsman_current_position = route_1[x]
                mallard_current_position = route_2[x]
                if scotsman_current_position == '1':
                    photo_1.configure(image=root.nrm1)
                elif scotsman_current_position == '2':
                    photo_1.configure(image=root.nrm2)
                elif scotsman_current_position == '3':
                    sensor_data[0] = True
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
                    sensor_data[5] = True
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
                    sensor_data[0] = True
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
                    sensor_data[5] = True
                    photo_1.configure(image=root.nrm28)
                elif mallard_current_position == '29':
                    photo_1.configure(image=root.nrm29)
                elif mallard_current_position == '30':
                    photo_1.configure(image=root.nrm30)
                f = open('train_data.txt', 'a')
                f.truncate(0)
                f.writelines(f'{scotsman_current_position}\n{mallard_current_position}\n')
                f.close()

                point_change()
                signal_check()

                Sensor_ONE_DATA.configure(text=f'{sensor_data[0]}')
                Sensor_TWO_DATA.configure(text=f'{sensor_data[1]}')
                Sensor_THREE_DATA.configure(text=f'{sensor_data[2]}')
                Sensor_FOUR_DATA.configure(text=f'{sensor_data[3]}')
                Sensor_FIVE_DATA.configure(text=f'{sensor_data[4]}')
                Sensor_SIX_DATA.configure(text=f'{sensor_data[5]}')

                Point_A_DATA.configure(text=f'{Point_A}°')
                Point_B_DATA.configure(text=f'{Point_B}°')

                record_data()

                continue
            break
        x = 0
        y = 0
        while l5 is True and emergency_stop is False:
            sensor_data[0] = False
            sensor_data[1] = False
            sensor_data[2] = False
            sensor_data[3] = False
            sensor_data[4] = False
            sensor_data[5] = False

            print(f'Scotsman is at position - {scotsman_current_position}')
            print(f'Mallard is at position - {mallard_current_position}')

            time.sleep(v)
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
                sensor_data[0] = True
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
                sensor_data[5] = True
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
                sensor_data[0] = True
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
                sensor_data[5] = True
                photo_1.configure(image=root.nrm28)
            elif mallard_current_position == '29':
                photo_1.configure(image=root.nrm29)
            elif mallard_current_position == '30':
                photo_1.configure(image=root.nrm30)
            f = open('train_data.txt', 'a')
            f.truncate(0)
            f.writelines(f'{scotsman_current_position}\n{mallard_current_position}\n')
            f.close()

            point_change()
            signal_check()

            Sensor_ONE_DATA.configure(text=f'{sensor_data[0]}')
            Sensor_TWO_DATA.configure(text=f'{sensor_data[1]}')
            Sensor_THREE_DATA.configure(text=f'{sensor_data[2]}')
            Sensor_FOUR_DATA.configure(text=f'{sensor_data[3]}')
            Sensor_FIVE_DATA.configure(text=f'{sensor_data[4]}')
            Sensor_SIX_DATA.configure(text=f'{sensor_data[5]}')
            Point_A_DATA.configure(text=f'{Point_A}°')
            Point_B_DATA.configure(text=f'{Point_B}°')

            record_data()

            continue


def run():
    Test['state'] = DISABLED
    p = threading.Thread(target=constant_run)
    p.daemon = True
    p.start()


def switch():
    Start_Sim.configure(command=lambda: [close()], text='STOP')


def record_data():
    f = open('blackbox.txt', 'a')
    f.write('\n\n')
    f.write('*--------------------------------------------*\n')
    f.write('SENSOR DATA:\n')
    find_date()
    f.write(f'Sensor 1 == {sensor_data[0]} at {date}\n')
    find_date()
    f.write(f'Sensor 2 == {sensor_data[1]} at {date}\n')
    find_date()
    f.write(f'Sensor 3 == {sensor_data[2]} at {date}\n')
    find_date()
    f.write(f'Sensor 4 == {sensor_data[3]} at {date}\n')
    find_date()
    f.write(f'Sensor 5 == {sensor_data[4]} at {date}\n')
    find_date()
    f.write(f'Sensor 6 == {sensor_data[5]} at {date}\n')
    f.write('\n')
    f.write('SIGNAL DATA:\n')
    find_date()
    f.write(f'Signal 1 == {signal_data[0]} at {date}\n')
    find_date()
    f.write(f'Signal 2 == {signal_data[1]} at {date}\n')
    find_date()
    f.write(f'Signal 3 == {signal_data[2]} at {date}\n')
    find_date()
    f.write(f'Signal 4 == {signal_data[3]} at {date}\n')
    find_date()
    f.write(f'Signal 5 == {signal_data[4]} at {date}\n')
    find_date()
    f.write(f'Signal 6 == {signal_data[5]} at {date}\n')
    f.write('\n')
    f.write('POINT DATA:\n')
    find_date()
    f.write(f'Point 1 == {Point_A}° at {date}\n')
    find_date()
    f.write(f'Point 2 == {Point_B}° at {date}\n')
    f.close()
    del_lines('blackbox.txt', 500, 26000)


def signal_check():
    if sensor_data[0] is True:
        signal_data[0] = True
        Signals_ONE_DATA.configure(image=root.green)
        signal_data[1] = False
        Signals_TWO_DATA.configure(image=root.red)
        signal_data[2] = False
        Signals_THREE_DATA.configure(image=root.red)
    if sensor_data[1] is True:
        pass
    if sensor_data[2] is True:
        signal_data[0] = False
        Signals_ONE_DATA.configure(image=root.red)
        signal_data[1] = True
        Signals_TWO_DATA.configure(image=root.green)
        signal_data[2] = False
        Signals_THREE_DATA.configure(image=root.red)
    if sensor_data[3] is True:
        signal_data[3] = True
        Signals_FOUR_DATA.configure(image=root.green)
        signal_data[4] = False
        Signals_FIVE_DATA.configure(image=root.red)
        signal_data[5] = False
        Signals_SIX_DATA.configure(image=root.red)
    if sensor_data[4] is True:
        pass
    if sensor_data[5] is True:
        signal_data[3] = False
        Signals_FOUR_DATA.configure(image=root.red)
        signal_data[4] = False
        Signals_FIVE_DATA.configure(image=root.red)
        signal_data[5] = True
        Signals_SIX_DATA.configure(image=root.green)


def del_lines(file, lines_from_top=500, when_to_del=5000):
    with open(file, 'r') as f:
        lines = f.readlines()
    if len(lines) > when_to_del:
        with open(file, 'w') as f:
            for line in lines[lines_from_top:]:
                f.write(line)


def find_date_file_name():
    x = datetime.datetime.today()
    date_file = x.strftime('_%d-%m-%Y_%H-%M')
    return date_file


def download_black_box(event):
    file_dst = event.widget.get()
    event.widget.delete(0, len(file_dst))
    if file_dst != 'Finland':
        src = 'blackbox.txt'
        dst = f'{file_dst}blackbox{find_date_file_name()}.txt'
        check(title='Download Black Box', text=f'Are you sure you want to download the black box to {dst}',
              icon_='warning', return_to=f2)
        try:
            f = open(dst, 'a')
            f.close()
            copyfile(src, dst)
        except Exception as e:
            print('Error: %s' % str(e))
    else:
        easter_egg = Tk()
        Label(easter_egg, text='Easter Egg coming soon').grid()
        Button(easter_egg, text='Exit', command=lambda: easter_egg.destroy()).grid()  # ToDo


def check(title='pop up', text='text goes here', icon_='warning', return_to=f0):
    global message_box
    message_box = messagebox.askquestion(title, text, icon=icon_)
    if message_box == 'yes':
        pass
    else:
        raise_frame(return_to)


def read_last_input():
    read_data_screen = Tk()
    read_data_screen.iconbitmap('C:/Users/noaha/PycharmProjects/NRM/images/StROMEROs_Logo.ico')
    read_data_screen.resizable(0, 0)
    Label(read_data_screen, text='Black Box Last Input', font=Font(family='Verdana')).grid(row=0, column=0)
    f = open('blackbox.txt', 'r')
    x = f.readlines()
    info = str(x[-20:])
    last_data_input = StringTransformation(info)
    display_info = str(last_data_input.list_to_string)
    black_box_last_input = Label(read_data_screen, text=display_info)
    black_box_last_input.grid(row=1, column=0, sticky='w')
    Button(read_data_screen, text='Exit', width=20, command=lambda: read_data_screen.destroy()).grid(row=2, column=0)


def clear_black_box(file):
    check('Are you sure you want to continue?',
          'By continuing you will delete ALL black box data which may be useful in the future.', return_to=f2)
    try:
        if message_box == 'yes':
            f = open(file, 'w')
            f.truncate(0)
            f.close()
            print(f'{file} was cleared')
        else:
            print(f'{file} was NOT cleared')
    except Exception as e:
        print('Error: %s' % str(e))


# Home Page
w1 = 27
h1 = 11
Control_Panel = Button(f0, text='CONTROL\nPANEL', width=w1, height=h1, command=lambda: raise_frame(f1),
                       font=VerdanaL).grid(row=0, column=0, sticky='w')
Black_Box = Button(f0, text='BLACK\nBOX', width=w1, height=h1, command=lambda: raise_frame(f2), font=VerdanaL). \
    grid(row=0, column=1, sticky='e')
Test = Button(f0, text='TEST', width=w1, height=h1, command=lambda: raise_frame(f3), font=VerdanaL)
Test.grid(row=1, column=0, sticky='w')
Quit = Button(f0, text='QUIT', width=w1, height=h1, command=close, font=VerdanaL).grid(row=1, column=1, sticky='e')

# Control Panel
w2 = 10
h2 = 8
Check_Sensors = Button(f1, text='CHECK\nSENSORS', width=w2, height=h2, command=lambda: raise_frame(sensor),
                       font=VerdanaL).grid(row=3, column=0)
Check_Points = Button(f1, text='CHECK\nPOINTS', width=w2, height=h2, command=lambda: raise_frame(point),
                      font=VerdanaL).grid(row=3, column=1)
Check_Signals = Button(f1, text='CHECK\nSIGNALS', width=w2, height=h2, command=lambda: raise_frame(signal),
                       font=VerdanaL).grid(row=3, column=2)
Start_Sim = Button(f1, text='START', width=w2, height=h2, command=lambda: [run(), switch()], state=NORMAL,
                   font=VerdanaL)
Start_Sim.grid(row=3, column=3)
Leave = Button(f1, text='RETURN', width=w2, height=h2, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=4)
photo_1 = Label(f1, image=root.error)
photo_1.grid(row=0, column=0, columnspan=5)

Sensor_ONE = Label(sensor, text=f'Sensor 1 reads ', font=Verdana, padx=0, pady=7).grid(row=0, column=0)
Sensor_ONE_DATA = Label(sensor, text=f'{sensor_data[0]}', font=Verdana, padx=0, pady=7)
Sensor_ONE_DATA.grid(row=0, column=1)
Sensor_TWO = Label(sensor, text=f'Sensor 2 reads ', font=Verdana, padx=0, pady=7).grid(row=1, column=0)
Sensor_TWO_DATA = Label(sensor, text=f'{sensor_data[1]}', font=Verdana, padx=0, pady=7)
Sensor_TWO_DATA.grid(row=1, column=1)
Sensor_THREE = Label(sensor, text=f'Sensor 3 reads ', font=Verdana, padx=0, pady=7).grid(row=2, column=0)
Sensor_THREE_DATA = Label(sensor, text=f'{sensor_data[2]}', font=Verdana, padx=0, pady=7)
Sensor_THREE_DATA.grid(row=2, column=1)
Sensor_FOUR = Label(sensor, text=f'Sensor 4 reads ', font=Verdana, padx=0, pady=7).grid(row=3, column=0)
Sensor_FOUR_DATA = Label(sensor, text=f'{sensor_data[3]}', font=Verdana, padx=0, pady=7)
Sensor_FOUR_DATA.grid(row=3, column=1)
Sensor_FIVE = Label(sensor, text=f'Sensor 5 reads ', font=Verdana, padx=0, pady=7).grid(row=4, column=0)
Sensor_FIVE_DATA = Label(sensor, text=f'{sensor_data[4]}', font=Verdana, padx=0, pady=7)
Sensor_FIVE_DATA.grid(row=4, column=1)
Sensor_SIX = Label(sensor, text=f'Sensor 6 reads ', font=Verdana, padx=0, pady=7).grid(row=5, column=0)
Sensor_SIX_DATA = Label(sensor, text=f'{sensor_data[5]}', font=Verdana, padx=0, pady=7)
Sensor_SIX_DATA.grid(row=5, column=1)
Sensor_return = Button(sensor, text='RETURN', font=VerdanaL, height=5, width=56, padx=8, pady=7,
                       command=lambda: raise_frame(f1)).grid(columnspan=2)
nom = 42
nox = 42
Point_A_ = Label(point, text='POINT A IS AT ', font=Verdana).grid(column=0, row=0, padx=nom, pady=nox)
Point_B_ = Label(point, text='POINT B IS AT ', font=Verdana).grid(column=0, row=1, padx=nom, pady=nox)
Point_A_DATA = Label(point, text=f'{Point_A}°', font=Verdana)
Point_A_DATA.grid(column=1, row=0)
Point_B_DATA = Label(point, text=f'{Point_B}°', font=Verdana)
Point_B_DATA.grid(column=1, row=1)
Point_return = Button(point, text='RETURN', font=VerdanaL, height=5, width=56, padx=8, pady=7,
                      command=lambda: raise_frame(f1)).grid(columnspan=2, sticky='s')

Signals_ONE = Label(signal, text=f'Signal 1 reads ', font=Verdana, padx=0, pady=7).grid(row=0, column=0)
Signals_ONE_DATA = Label(signal, image=root.red, padx=0, pady=7)
Signals_ONE_DATA.grid(row=0, column=1)
Signals_TWO = Label(signal, text=f'Signal 2 reads ', font=Verdana, padx=0, pady=7).grid(row=1, column=0)
Signals_TWO_DATA = Label(signal, image=root.red, padx=0, pady=7)
Signals_TWO_DATA.grid(row=1, column=1)
Signals_THREE = Label(signal, text=f'Signal 3 reads ', font=Verdana, padx=0, pady=7).grid(row=2, column=0)
Signals_THREE_DATA = Label(signal, image=root.red, padx=0, pady=7)
Signals_THREE_DATA.grid(row=2, column=1)
Signals_FOUR = Label(signal, text=f'Signal 4 reads ', font=Verdana, padx=0, pady=7).grid(row=3, column=0)
Signals_FOUR_DATA = Label(signal, image=root.red, padx=0, pady=7)
Signals_FOUR_DATA.grid(row=3, column=1)
Signals_FIVE = Label(signal, text=f'Signal 5 reads ', font=Verdana, padx=0, pady=7).grid(row=4, column=0)
Signals_FIVE_DATA = Label(signal, image=root.red, padx=0, pady=7)
Signals_FIVE_DATA.grid(row=4, column=1)
Signals_SIX = Label(signal, text=f'Signal 6 reads ', font=Verdana, padx=0, pady=7).grid(row=5, column=0)
Signals_SIX_DATA = Label(signal, image=root.red, padx=0, pady=7)
Signals_SIX_DATA.grid(row=5, column=1)
Signal_return = Button(signal, text='RETURN', font=VerdanaL, height=5, width=56, padx=8, pady=7,
                       command=lambda: raise_frame(f1)).grid(columnspan=2, sticky='s')

# Black Box
Read_last = Button(f2, text='READ LAST\nINPUT', width=width, height=h, command=read_last_input, font=VerdanaL). \
    grid(row=3, column=0)
Download = Button(f2, text='DOWNLOAD ALL', width=width, height=h, command=lambda: raise_frame(download),
                  font=VerdanaL).grid(row=3, column=1)
Clear = Button(f2, text='CLEAR\nBLACK BOX', width=width, height=h, command=lambda: clear_black_box('train_data.txt'),
               font=VerdanaL).grid(row=3, column=2)
Leave_1 = Button(f2, text='RETURN', width=width, height=h, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=3)
photo_2 = Label(f2, image=root.error)
photo_2.grid(row=0, column=0, columnspan=4)

lab = Label(download, text='Enter Location for Download:', font=Verdana)
lab.grid(row=0, column=0, pady=78, padx=78)
example = Label(download, text='i.e C:/Users/johnsmith/', font=VerdanaL).grid(row=1, column=0)
ent = Entry(download, width=66)
ent.grid(row=2, column=0, sticky='w')
ent.bind('<Return>', download_black_box)
Download_return = Button(download, text='RETURN', font=VerdanaL, height=5, width=56, padx=8, pady=7,
                         command=lambda: raise_frame(f2)).grid(row=3, column=0)

# System testing
Run_Through = Button(f3, text='Test System', width=27, height=h, command=outward_run, font=VerdanaL). \
    grid(row=3, column=0)
# working_on_it
Leave_2 = Button(f3, text='RETURN', width=27, height=h, command=lambda: raise_frame(f0), font=VerdanaL). \
    grid(row=3, column=3)
photo_3 = Label(f3, image=root.error)
photo_3.grid(row=0, column=0, columnspan=4)

raise_frame(f0)
root.mainloop()
