# **NOTE**
# This file is only to test small parts of the program
# This will have no impact on the final program


# def del_10000(file, lines_from_top=500, when_to_del=5000):
#     with open(file, 'r') as f:
#         lines = f.readlines()
#     if len(lines) > when_to_del:
#         with open(file, 'w') as f:
#             for line in lines[lines_from_top:]:
#                 f.write(line)
#
#
# # for x in range(20000):
# #     f = open('oof.txt', 'a')
# #     f.write(f'{x}\n')
# #     f.close()
# del_10000('oof.txt')

# data = [True, False, False, False, False, True]
#
#
# def bool_change(bool_input):
#     if bool_input is True:
#         bool_input = False
#     elif bool_input is False:
#         bool_input = True
#     else:
#         print(f'{bool_input} is not valid input')
#     return bool_input
#
#
# print(bool_change(data[0]))

import time

sensor_data: list[bool] = [False, False, False, False, False, False]
signal_data: list[bool] = [False, False, False, False, False, False]


def signal_check():
    if sensor_data[0] is True:
        signal_data[0] = True
        signal_data[1] = False
        signal_data[2] = False
    if sensor_data[1] is True:
        signal_data[0] = False
        signal_data[1] = False
        signal_data[2] = False
    if sensor_data[2] is True:
        signal_data[0] = False
        signal_data[1] = True
        signal_data[2] = False
    if sensor_data[3] is True:
        signal_data[3] = True
        signal_data[4] = False
        signal_data[5] = False
    if sensor_data[4] is True:
        signal_data[3] = False
        signal_data[4] = False
        signal_data[5] = False
    if sensor_data[5] is True:
        signal_data[3] = False
        signal_data[4] = False
        signal_data[5] = True
    print(f'{signal_data}')
    # sensor_data[0] = False
    # sensor_data[1] = False
    # sensor_data[2] = False
    # sensor_data[3] = False
    # sensor_data[4] = False
    # sensor_data[5] = False


for x in range(30):
    sensor_data[2] = True
    sensor_data[3] = True
    signal_check()
    time.sleep(1)
