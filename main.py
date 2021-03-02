# Imports
import time
import datetime
from shutil import copyfile
# import itertools
# import threading
# import sys
# from typing import List
test: bool = False
emergency_stop: bool = False
sim: bool = True
blackbox: bool = True
# sensor_data = [Sensor 1, Sensor 2, Sensor 3, Sensor 4, Sensor 5, Sensor 6]
sensor_data: list[bool] = [True, False, False, False, False, True]
# Sensors 1 and 6 are set to true as when a train moves past them they just switch there input to avoid a
# train being stuck at the end.
# s1 = sensor_data[0]
# s2 = sensor_data[1]
# s3 = sensor_data[2]
# s4 = sensor_data[3]
# s5 = sensor_data[4]
# s6 = sensor_data[5]
r1: bool = False
r2: bool = False
signal_data: list[bool] = [False, False, False, False, False, False]
Point_A: int = 0
Point_B: int = 0
# For purposes of testing the wait time is 0.5 seconds
# However when the program is complete the time can be changed to the correct time
wait_time: float = 0.5
date: str = ''
date_file: str = ''
Sig_a: str = ''
Sig_b: str = ''
Sig_c: str = ''
Sig_d: str = ''
Sig_e: str = ''
Sig_f: str = ''
power_t1: int = 0
power_t2: int = 0
done: bool = False


# This is the sensor check for route one
def sensor_check_1():
    global r1
    r1 = False

    s2 = sensor_data[1]
    s4 = sensor_data[3]

    if s2 is False and s4 is False:
        print('Route one clear.')
        r1 = True
        return r1

    if s2 is True or s4 is True:
        print('Route one not clear.')
        r1 = False
        return r1


# This is the sensor check for route two
def sensor_check_2():
    global r2
    r2 = False
    s3 = sensor_data[2]
    s5 = sensor_data[4]

    if s3 is False and s5 is False:
        print('Route two clear.')
        r2 = True
        return r2
    if s3 is True or s5 is True:
        print('Route two not clear.')
        r2 = False
        return r2


def point_change():
    global Point_A
    global Point_B
    global emergency_stop

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
    if s2 is True and s4 is True:
        emergency_stop = True
    if s3 is True and s5 is True:
        emergency_stop = True
    if s1 is True and s2 is True:
        emergency_stop = True
    if s1 is True and s3 is True:
        emergency_stop = True
    if s6 is True and s4 is True:
        emergency_stop = True
    if s6 is True and s5 is True:
        emergency_stop = True
    print(Point_A)
    print(Point_B)


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


def find_date():
    global date
    x = datetime.datetime.today()
    date = x.strftime('%a %b %d %Y %H:%M:%S')
    # print(date)


def find_date_file_name():
    global date_file
    x = datetime.datetime.today()
    date_file = x.strftime('%b%d%Y-%H:%M:%S')


def signal_check():
    global Sig_a
    global Sig_b
    global Sig_c
    global Sig_d
    global Sig_e
    global Sig_f

    a = signal_data[0]
    b = signal_data[1]
    c = signal_data[2]
    d = signal_data[3]
    e = signal_data[4]
    f = signal_data[5]

    if a is False:
        Sig_a = 'RED'
    elif a is True:
        Sig_a = 'GREEN'
    if b is False:
        Sig_b = 'RED'
    elif b is True:
        Sig_b = 'GREEN'
    if c is False:
        Sig_c = 'RED'
    elif c is True:
        Sig_c = 'GREEN'
    if d is False:
        Sig_d = 'RED'
    elif d is True:
        Sig_d = 'GREEN'
    if e is False:
        Sig_e = 'RED'
    elif e is True:
        Sig_e = 'GREEN'
    if f is False:
        Sig_f = 'RED'
    elif f is True:
        Sig_f = 'GREEN'
    if Point_A == 0:
        Sig_c = 'RED'
    elif Point_A == 30:
        Sig_b = 'RED'
    if Point_B == 0:
        Sig_d = 'RED'
    elif Point_B == 30:
        Sig_e = 'RED'


def main():
    emergency_stop = False
    while sim and emergency_stop is not True:
        print('*----------------------------------------------------*')
        print('1. Control Panel')
        print('2. Black Box')
        print('3. Test')
        print('4. Quit')
        print('Enter digit to continue:')
        o1 = input()
        if o1 == '1':
            o2 = '1'
            while o2 != '4':
                # from run import constant_run
                # constant_run()
                print('Control Panel')
                print('1. Check Sensors')
                print('2. Check Points')
                print('3. Check Signals')
                print('4. Leave')
                print('')
                print('HIT ENTER FOR EMERGENCY STOP')
                o2 = input()
                if o2 == '1':
                    # The line bellow is there for testing purposes
                    sensor_data[1] = True
                    sensor_check_1()
                    sensor_check_2()
                    print(f'Route one is clear - {r1} Route two is clear - {r2}')
                    record_data()
                elif o2 == '2':
                    print(f'Point A is at {Point_A}°\n'
                          f'Point B is at {Point_B}°\n')
                    record_data()
                elif o2 == '3':
                    signal_check()
                    print(f'Signal 1 - {Sig_a}\n'
                          f'Signal 2 - {Sig_b}\n'
                          f'Signal 3 - {Sig_c}\n'
                          f'Signal 4 - {Sig_d}\n'
                          f'Signal 5 - {Sig_e}\n'
                          f'Signal 6 - {Sig_f}\n')
                    record_data()
                elif o2 == '':
                    record_data()
                    f = open('blackbox.txt', 'a')
                    find_date()
                    f.write(f'\n\n***EMERGENCY STOP AT {date}***\n')
                    f.close()
                    emergency_stop = True
                    break

        elif o1 == '2':
            print('Black Box Menu')
            print('1. Read Last Input')
            print('2. Download Black Box')
            print('3. Clear Black Box')
            print('4. Leave')
            o3 = input()
            while o3 != '4':
                if o3 == '1':
                    f = open("blackbox.txt", "r")
                    file = f.read()
                    f.close()
                    print(file[-750:])
                    # If more information is recorded in each cycle the code above must be changed
                if o3 == '2':
                    print('Please input where you want the file downloaded to.')
                    print('i.e C:/Users/johnsmith/')
                    file_dst = input()
                    src = 'blackbox.txt'
                    find_date_file_name()
                    dst = f'{file_dst}blackbox{date_file}.txt'

                    try:
                        f = open(dst, 'a')
                        f.close()
                        copyfile(src, dst)
                    except Exception as e:
                        print('Error: %s' % str(e))
                if o3 == '3':
                    f = open('blackbox.txt', 'r')
                    x = f.read()
                    f.close()
                    print('Are you sure you want to delete all data?')
                    print('Once deleted data cannot be restored')
                    print(f'Last delete was on {x[:24]}')
                    print('y/n')
                    delete = input().lower()
                    if delete == 'yes' or 'y':
                        f = open('blackbox.txt', 'a')
                        f.truncate(0)
                        find_date()
                        f.write(f'{date}\n')
                        f.close()
                    elif delete == 'no' or 'n':
                        pass

        elif o1 == '3':
            o4 = ''
            while o4 != 2:
                print('Test Menu')
                print('1. Full run')
                print('2. Leave')
                o4 = input()
                if o4 == '1':
                    print('Starting Simulation')
                    power_t1 = 10
                    power_t2 = 10
                    if power_t1 != 0 and power_t2 != 0:
                        print(f'The Scotsman is traveling at {power_t1}')
                        print(f'The Mallard is traveling at {power_t2}')
                        from run import outward_run
                        test = True
                        outward_run()
                        point_change()
                        time.sleep(2)
                        from run import return_run
                        return_run()
                elif o4 == '2':
                    break

        elif o1 == '4':
            print('Type 1 to quit type 2 to return')
            q1 = input()
            if q1 == '1':
                break
            else:
                pass

    time.sleep(wait_time)


if __name__ == '__main__':
    main()
