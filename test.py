# **NOTE**
# This file is only to test small parts of the program
# This will have no impact on the final program


def del_10000(file, lines_from_top=500, when_to_del=5000):
    with open(file, 'r') as f:
        lines = f.readlines()
    if len(lines) > when_to_del:
        with open(file, 'w') as f:
            for line in lines[lines_from_top:]:
                f.write(line)


# for x in range(20000):
#     f = open('oof.txt', 'a')
#     f.write(f'{x}\n')
#     f.close()
del_10000('oof.txt')
