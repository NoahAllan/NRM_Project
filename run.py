# imports
import time
import itertools
import threading
import sys
from track import *
from main import sensor_data
from main import point_change
from main import record_data

v = 0.2  # This number should be 17.8 for correct timings but is lower for testing purposes


route_1 = section_a + section_c + section_d
route_two = section_a + section_b + section_d

route_2 = route_two[::-1]


def outward_run():
    scotsman_current_position = route_1[0]
    mallard_current_position = route_2[0]
    l1: bool = True
    x = 0
    while l1:
        sensor_data[1] = False
        sensor_data[2] = False
        sensor_data[3] = False
        sensor_data[4] = False

        arrived = False
        print(f'Scotsman is at position - {scotsman_current_position}')
        print(f'Mallard is at position - {mallard_current_position}')

        def traveling():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if arrived:
                    break
                sys.stdout.write('\rtraveling ' + c)
                sys.stdout.flush()
                time.sleep(0.3)
            sys.stdout.write('\r \n')
        t = threading.Thread(target=traveling)
        t.start()
        time.sleep(v)
        arrived = True
        time.sleep(0.2)
        x += 1
        if x == 30:
            break
        scotsman_current_position = route_1[x]
        mallard_current_position = route_2[x]
        if scotsman_current_position == '3':
            sensor_data[0] = not sensor_data[0]
        elif scotsman_current_position == '9b':
            sensor_data[1] = True
        elif scotsman_current_position == '9c':
            sensor_data[2] = True
        elif scotsman_current_position == '22b':
            sensor_data[3] = True
        elif scotsman_current_position == '22c':
            sensor_data[4] = True
        elif scotsman_current_position == '28':
            sensor_data[5] = not sensor_data[5]
        if mallard_current_position == '3':
            sensor_data[0] = not sensor_data[0]
        elif mallard_current_position == '9b':
            sensor_data[1] = True
        elif mallard_current_position == '9c':
            sensor_data[2] = True
        elif mallard_current_position == '22b':
            sensor_data[3] = True
        elif mallard_current_position == '22c':
            sensor_data[4] = True
        elif mallard_current_position == '28':
            sensor_data[5] = not sensor_data[5]
        print(sensor_data)
        point_change()
        record_data()


def return_run():
    mallard_current_position = route_1[0]
    scotsman_current_position = route_2[0]
    l2 = True
    x = 0
    while l2:
        sensor_data[1] = False
        sensor_data[2] = False
        sensor_data[3] = False
        sensor_data[4] = False
        arrived = False
        print(f'Scotsman is at position - {scotsman_current_position}')
        print(f'Mallard is at position - {mallard_current_position}')

        def traveling():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if arrived:
                    break
                sys.stdout.write('\rtraveling ' + c)
                sys.stdout.flush()
                time.sleep(0.3)
            sys.stdout.write('\r \n')

        t = threading.Thread(target=traveling)
        t.start()
        time.sleep(v)
        arrived = True
        time.sleep(0.2)
        x += 1
        if x == 30:
            break
        scotsman_current_position = route_2[x]
        mallard_current_position = route_1[x]
        if scotsman_current_position == '3':
            sensor_data[0] = not sensor_data[0]
        elif scotsman_current_position == '9b':
            sensor_data[1] = True
        elif scotsman_current_position == '9c':
            sensor_data[2] = True
        elif scotsman_current_position == '22b':
            sensor_data[3] = True
        elif scotsman_current_position == '22c':
            sensor_data[4] = True
        elif scotsman_current_position == '28':
            sensor_data[5] = not sensor_data[5]
        if mallard_current_position == '3':
            sensor_data[0] = not sensor_data[0]
        elif mallard_current_position == '9b':
            sensor_data[1] = True
        elif mallard_current_position == '9c':
            sensor_data[2] = True
        elif mallard_current_position == '22b':
            sensor_data[3] = True
        elif mallard_current_position == '22c':
            sensor_data[4] = True
        elif mallard_current_position == '28':
            sensor_data[5] = not sensor_data[5]
        print(sensor_data)
        point_change()
        record_data()


def constant_run():
    from main import emergency_stop
    from main import record_data
    from main import point_change
    scotsman_current_position = route_1[0]
    mallard_current_position = route_2[0]
    l3: bool = True
    while l3 is True:
        x = 0
        y = 0
        l4: bool = True
        l5: bool = True
        while l4 is True and emergency_stop is False:
            sensor_data[1] = False
            sensor_data[2] = False
            sensor_data[3] = False
            sensor_data[4] = False

            arrived = False
            print(f'Scotsman is at position - {scotsman_current_position}')
            print(f'Mallard is at position - {mallard_current_position}')

            def traveling():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if arrived:
                        break
                    sys.stdout.write('\rtraveling ' + c)
                    sys.stdout.flush()
                    time.sleep(0.3)
                sys.stdout.write('\r \n')

            t = threading.Thread(target=traveling)
            t.start()
            time.sleep(v)
            arrived: bool = True
            time.sleep(0.2)
            x += 1
            if x == 30:
                break
            scotsman_current_position = route_1[x]
            mallard_current_position = route_2[x]
            if scotsman_current_position == '3':
                sensor_data[0] = not sensor_data[0]
            elif scotsman_current_position == '9b':
                sensor_data[1] = True
            elif scotsman_current_position == '9c':
                sensor_data[2] = True
            elif scotsman_current_position == '22b':
                sensor_data[3] = True
            elif scotsman_current_position == '22c':
                sensor_data[4] = True
            elif scotsman_current_position == '28':
                sensor_data[5] = not sensor_data[5]
            if mallard_current_position == '3':
                sensor_data[0] = not sensor_data[0]
            elif mallard_current_position == '9b':
                sensor_data[1] = True
            elif mallard_current_position == '9c':
                sensor_data[2] = True
            elif mallard_current_position == '22b':
                sensor_data[3] = True
            elif mallard_current_position == '22c':
                sensor_data[4] = True
            elif mallard_current_position == '28':
                sensor_data[5] = not sensor_data[5]
            print(sensor_data)
            point_change()
            record_data()
        while l5 is True and emergency_stop is False:
            sensor_data[1] = False
            sensor_data[2] = False
            sensor_data[3] = False
            sensor_data[4] = False
            arrived = False
            print(f'Scotsman is at position - {scotsman_current_position}')
            print(f'Mallard is at position - {mallard_current_position}')

            def traveling():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if arrived:
                        break
                    sys.stdout.write('\rtraveling ' + c)
                    sys.stdout.flush()
                    time.sleep(0.3)
                sys.stdout.write('\r \n')

            t = threading.Thread(target=traveling)
            t.start()
            time.sleep(v)
            arrived = True
            time.sleep(0.2)
            y += 1
            if y == 30:
                break
            scotsman_current_position = route_2[y]
            mallard_current_position = route_1[y]
            if scotsman_current_position == '3':
                sensor_data[0] = not sensor_data[0]
            elif scotsman_current_position == '9b':
                sensor_data[1] = True
            elif scotsman_current_position == '9c':
                sensor_data[2] = True
            elif scotsman_current_position == '22b':
                sensor_data[3] = True
            elif scotsman_current_position == '22c':
                sensor_data[4] = True
            elif scotsman_current_position == '28':
                sensor_data[5] = not sensor_data[5]
            if mallard_current_position == '3':
                sensor_data[0] = not sensor_data[0]
            elif mallard_current_position == '9b':
                sensor_data[1] = True
            elif mallard_current_position == '9c':
                sensor_data[2] = True
            elif mallard_current_position == '22b':
                sensor_data[3] = True
            elif mallard_current_position == '22c':
                sensor_data[4] = True
            elif mallard_current_position == '28':
                sensor_data[5] = not sensor_data[5]
            print(sensor_data)
            point_change()
            record_data()
