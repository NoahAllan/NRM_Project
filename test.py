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


class StringTransformation(object):
    def __init__(self, list_in):
        self.list_in = list_in

    @property
    def list_to_string(self):
        return self.list_in.replace('[', '').replace(']', '').replace('\\n', '').replace("'", '').replace(',', '\n').\
            replace('*--------------------------------------------*', '')


def list_to_string(list_to_replace):
    list_to_replace.replace('[', '')
    list_to_replace.replace(']', '')
    list_to_replace.replace('\n', '')
    list_to_replace.replace("'", '')
    list_to_replace.replace(',', '\n')
    return list_to_replace


f = open('blackbox.txt', 'r')
x = f.readlines()
info = str(x[-20:])

infp_ = StringTransformation(info)

print(infp_.list_to_string)

