# **NOTE**
# This file is only to test small parts of the program
# This will have no impact on the final program

def find_train_position():
    global pos
    f = open('train_data', 'r')
    pos = f.readlines(0-1)
    f.close()


find_train_position()
print(int(pos[0].replace('c', '').replace('b', '')) - 1)
print(int(pos[0].replace('c', '').replace('b', '')) - 1)
