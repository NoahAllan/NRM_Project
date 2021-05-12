import time
from shutil import copyfile
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import threading
import datetime
import tkinter as tk
from PIL import Image, ImageTk

# import ImageTk

# DEFYING VARIABLES IN THIS ZONE

#


section_a = ['1', '2', '3', '4', '5']
section_b = ['6b', '7b', '8b', '9b', '10b',
             '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b',
             '21b', '22b', '23b', '24b', '25b', '26b', '27b', '28b', '29b', '30b',
             '31b', '32b', '33b', '34b', '35b', ]

section_d = ['36', '37', '38', '39', '40']

route_1 = section_a + section_b + section_d  # scotsman / straight ahead

Bsection_d = ['40', '39', '38', '37', '36']
Bsection_c = ['35c', '34c', '33c', '33c', '32c', '31c', '30c', '29c', '28c', '27c', '26c', '25c', '24c', '23c', '22c',
              '21c',
              '20c', '19c', '18c', '17c', '16c', '15c', '14c', '13c', '12c', '11c',
              '10c', '9c', '8c', '7c', '6c']
Bsection_a = ['5', '4', '3', '2', '1']

route_2 = Bsection_d + Bsection_c + Bsection_a  # mallard / above track

interval = 0.5  # interval for train updates


# DEFINING

def close():
    quit()


def trains():
    scotsmanpos = 0  # this is scotsman

    mallardpos = 0  # this is mallard

    loopon = True

    while loopon == True:
        time.sleep(interval)  # change this for update interval
        if scotsmanpos > 39:
            break
        # print(route_1[scotsmanpos])
        scotsmanpos += 1

        if mallardpos > 39:
            break

        # print(route_2[mallardpos])
        mallardpos += 1

        # 0= untriggered
        # 1= triggered

        signal_1 = 0  # A
        signal_2 = 0  # B
        signal_3 = 0  # E
        signal_4 = 0  # F
        signal_5 = 0  # D
        signal_6 = 0  # C

        if scotsmanpos == 1:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM1)

        elif scotsmanpos == 2:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM2)
            oof.configure(image=root.nrm2)

        elif scotsmanpos == 3:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM3)

        elif scotsmanpos == 4:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM4)

        elif scotsmanpos == 5:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM5)

        elif scotsmanpos == 6:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM6)
            f = open('blackbox.txt', 'a')
            find_date()
            f.write(f'\nscotsman has triggered sensor 1. \nsensor = 1 at {date}\n')
            f.close()

        elif scotsmanpos == 7:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM7)

        elif scotsmanpos == 8:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM8)

        elif scotsmanpos == 9:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM9)

        elif scotsmanpos == 10:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM10)

        elif scotsmanpos == 11:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM11)

        elif scotsmanpos == 12:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM12)

        elif scotsmanpos == 13:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM13)

        elif scotsmanpos == 14:
            print("scotsman is at position ", scotsmanpos)  # (image=root.NRM14)

        elif scotsmanpos == 15:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM15)

        elif scotsmanpos == 16:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM16)

        elif scotsmanpos == 17:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM17)

        elif scotsmanpos == 18:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM18)

        elif scotsmanpos == 19:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM19)

        elif scotsmanpos == 20:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM20)
            f = open('blackbox.txt', 'a')
            find_date()
            f.write(f'scotsman has triggered sensor 2. \nsensor = 1 at {date}\n')
            f.close()

        elif scotsmanpos == 21:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM21)

        elif scotsmanpos == 22:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM22)

        elif scotsmanpos == 23:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM23)

        elif scotsmanpos == 24:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM24)

        elif scotsmanpos == 25:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM25)

        elif scotsmanpos == 26:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM26)

        elif scotsmanpos == 27:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM27)

        elif scotsmanpos == 28:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM28)

        elif scotsmanpos == 29:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM29)

        elif scotsmanpos == 30:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM30)

        elif scotsmanpos == 31:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM31)

        elif scotsmanpos == 32:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM32)

        elif scotsmanpos == 33:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM33)

        elif scotsmanpos == 34:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM34)

        elif scotsmanpos == 35:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM35)
            f = open('blackbox.txt', 'a')
            find_date()
            f.write(f'scotsman has triggered sensor 3. \nsensor = 1 at {date}\n')
            f.close()

        elif scotsmanpos == 36:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM36)

        elif scotsmanpos == 37:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM37)

        elif scotsmanpos == 38:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM38)

        elif scotsmanpos == 39:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM39)

        elif scotsmanpos == 40:
            print("scotsman is at position  ", scotsmanpos)  # (image=root.NRM40)

        elif scotsmanpos > 40:
            print("invalid")  # (image=root.NRMERROR404)

        #############################################################

        if mallardpos == 1:
            print("mallard is at position ", mallardpos)  # (image=root.NRM1)

        elif mallardpos == 2:
            print("mallard is at position ", mallardpos)  # (image=root.NRM2)

        elif mallardpos == 3:
            print("mallard is at position ", mallardpos)  # (image=root.NRM3)

        elif mallardpos == 4:
            print("mallard is at position ", mallardpos)  # (image=root.NRM4)

        elif mallardpos == 5:
            print("mallard is at position ", mallardpos)  # (image=root.NRM5)

        elif mallardpos == 6:
            print("mallard is at position ", mallardpos)  # (image=root.NRM6)
            f = open('blackbox.txt', 'a')
            find_date()
            f.write(f'mallard has triggered sensor 4. \nsensor = 1 at {date}\n')
            f.close()

        elif mallardpos == 7:
            print("mallard is at position ", mallardpos)  # (image=root.NRM7)

        elif mallardpos == 8:
            print("mallard is at position ", mallardpos)  # (image=root.NRM8)

        elif mallardpos == 9:
            print("mallard is at position ", mallardpos)  # (image=root.NRM9)

        elif mallardpos == 10:
            print("mallard is at position ", mallardpos)  # (image=root.NRM10)

        elif mallardpos == 11:
            print("mallard is at position ", mallardpos)  # (image=root.NRM11)

        elif mallardpos == 12:
            print("mallard is at position ", mallardpos)  # (image=root.NRM12)

        elif mallardpos == 13:
            print("mallard is at position ", mallardpos)  # (image=root.NRM13)

        elif mallardpos == 14:
            print("mallard is at position ", mallardpos)  # (image=root.NRM14)

        elif mallardpos == 15:
            print("mallard is at position ", mallardpos)  # (image=root.NRM15)

        elif mallardpos == 16:
            print("mallard is at position ", mallardpos)  # (image=root.NRM16)

        elif mallardpos == 17:
            print("mallard is at position ", mallardpos)  # (image=root.NRM17)

        elif mallardpos == 18:
            print("mallard is at position ", mallardpos)  # (image=root.NRM18)

        elif mallardpos == 19:
            print("mallard is at position ", mallardpos)  # (image=root.NRM19)

        elif mallardpos == 20:
            print("mallard is at position ", mallardpos)  # (image=root.NRM20)
            f = open('blackbox.txt', 'a')
            find_date()
            f.write(f'scotsman has triggered sensor 5. \nsensor = 1 at {date}\n')
            f.close()

        elif mallardpos == 21:
            print("mallard is at position ", mallardpos)  # (image=root.NRM21)

        elif mallardpos == 22:
            print("mallard is at position ", mallardpos)  # (image=root.NRM22)

        elif mallardpos == 23:
            print("mallard is at position ", mallardpos)  # (image=root.NRM23)

        elif mallardpos == 24:
            print("mallard is at position ", mallardpos)  # (image=root.NRM24)

        elif mallardpos == 25:
            print("mallard is at position ", mallardpos)  # (image=root.NRM25)

        elif mallardpos == 26:
            print("mallard is at position ", mallardpos)  # (image=root.NRM26)

        elif mallardpos == 27:
            print("mallard is at position ", mallardpos)  # (image=root.NRM27)

        elif mallardpos == 28:
            print("mallard is at position ", mallardpos)  # (image=root.NRM28)

        elif mallardpos == 29:
            print("mallard is at position ", mallardpos)  # (image=root.NRM29)

        elif mallardpos == 30:
            print("mallard is at position ", mallardpos)  # (image=root.NRM30)

        elif mallardpos == 31:
            print("mallard is at position ", mallardpos)  # (image=root.NRM31)

        elif mallardpos == 32:
            print("mallard is at position ", mallardpos)  # (image=root.NRM32)

        elif mallardpos == 33:
            print("mallard is at position ", mallardpos)  # (image=root.NRM33)

        elif mallardpos == 34:
            print("mallard is at position ", mallardpos)  # (image=root.NRM34)

        elif mallardpos == 35:
            print("mallard is at position ", mallardpos)  # (image=root.NRM35)
            f = open('blackbox.txt', 'a')
            find_date()
            f.write(f'scotsman has triggered sensor 6. \nsensor = 1 at {date}\n')
            f.close()

        elif mallardpos == 36:
            print("mallard is at position ", mallardpos)  # (image=root.NRM36)

        elif mallardpos == 37:
            print("mallard is at position ", mallardpos)  # (image=root.NRM37)

        elif mallardpos == 38:
            print("mallard is at position ", mallardpos)  # (image=root.NRM38)

        elif mallardpos == 39:
            print("mallard is at position ", mallardpos)  # (image=root.NRM39)

        elif mallardpos == 40:
            print("mallard is at position ", mallardpos)  # (image=root.NRM40)

        elif mallardpos > 40:
            print("invalid")  # (image=root.NRMERROR404)


def find_date():
    global date
    x = datetime.datetime.today()
    date = x.strftime('%a %b %d %Y %H:%M:%S')

    # signal_1 = 0 #A
    # signal_2 = 0 #B
    # signal_3 = 0 #E
    # signal_4 = 0 #F
    # signal_5 = 0 #D
    # signal_6 = 0 #C


def blackbox():
    f = open("blackbox.txt", "r")
    print(f.read())


def blackboxbeta():
    f = open('blackbox.txt', 'a')
    f.write('\n')
    f.write('*==========================================*\n')
    f.write('SENSOR DATA:\n')
    f.write('1 EQUALS TRIGGERED , 2 EQUALS UNTRIGGERED')
    find_date()
    f.write(f'Sensor 1 = , signal_1, \n')
    find_date()
    f.write(f'Sensor 2 == signal_2 at {date}\n')
    find_date()
    f.write(f'Sensor 3 == signal_3 at {date}\n')
    find_date()
    f.write(f'Sensor 4 == signal_4 at {date}\n')
    find_date()
    f.write(f'Sensor 5 == signal_5 at {date}\n')
    find_date()
    f.write(f'Sensor 6 == signal_6 at {date}\n')
    f.write('\n')


######################################################################

######################################################################

def run():
    p = threading.Thread(target=trains)
    p.daemon = True
    p.start()
    f = open('blackbox.txt', 'a')
    f.truncate(0)
    f.close()


######################################################################

root = Tk()

root.nrm1 = ImageTk.PhotoImage(Image.open('C:/Users/noaha/PycharmProjects/NRM/images/NRM_P1.png'))
root.nrm2 = ImageTk.PhotoImage(Image.open('C:/Users/noaha/PycharmProjects/NRM/images/NRM_P2.png'))

root.title('NRM PROJECT')
root.geometry('1300x800')
root.resizable(0, 0)
# img = PhotoImage(file='C:/Users/noaha/PycharmProjects/NRM/images/NRM_P1.png')
# img2 = PhotoImage(file='C:/Users/noaha/PycharmProjects/NRM/images/NRM_P1.png')
oof = Label(root, image=root.nrm1)
oof.grid(row=1, column=0)
Button(text='START', command=run).grid(row=2, column=0)
Button(text='BLACK BOX', command=blackbox).grid(row=3, column=0)
Button(text='EXIT', command=close).grid(row=4, column=0)

root.mainloop()

