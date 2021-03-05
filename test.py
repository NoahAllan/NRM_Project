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

# from pprint import pprint
# from tkinter.font import Font
# from tkinter import *
#
#
# class StringTransformation(object):
#     def __init__(self, list_in):
#         self.list_in = list_in
#
#     def list_to_string(self):
#         return self.list_in.replace('[', '').replace(']', '').replace('\\n', '').replace("'", '').replace(',', '\n').\
#             replace('*--------------------------------------------*', '')
#
#
# # def list_to_string(list_to_replace):
# #     list_to_replace.replace('[', '')
# #     list_to_replace.replace(']', '')
# #     list_to_replace.replace('\n', '')
# #     list_to_replace.replace("'", '')
# #     list_to_replace.replace(',', '\n')
# #     return list_to_replace
#
#
# def read_last_input():
#     f = open('blackbox.txt', 'r')
#     x = f.readlines()
#     info = str(x[-20:])
#
#     black_box_data_ = StringTransformation(info)
#
#     black_box_data_display = Tk()
#     bill = black_box_data_.list_to_string()
#     ty = Label(black_box_data_display, text=bill)
#     ty.grid(row=0, column=0)
#     ty.configure(font=Font(family='Verdana', size=8))
#     Button(black_box_data_display, text='Exit', command=lambda: black_box_data_display.destroy()).grid(row=1, column=0)
#
#     black_box_data_display.mainloop()
#
#
# # read_last_input()
