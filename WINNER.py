# -*- coding: utf-8 -*-
def blue_win(blue):
    move_blue_x = 1
    move_blue_y = 1
    move_blue_diagonal = 1
    blue.sort(key=lambda x: (x[0]))
    # print(blue)
    for i in blue:
        if (i[0] + 1, i[1]) in blue\
                and (i[0] + 2, i[1]) in blue\
                and (i[0] + 3, i[1]) in blue:
            move_blue_x += 1
            print(12)
        if move_blue_x == 2:
            print('Синий выйграл!')
            return
    for i in blue:
        if (i[0], i[1] + 1) in blue\
                and (i[0], i[1] + 2) in blue\
                and (i[0], i[1] + 3) in blue:

            move_blue_y += 1
            print(33)
        if move_blue_y == 2:
            print('Синий выйграл!')
            return
    for i in blue:
        if (i[0] + 1, i[1] + 1) in blue\
                and (i[0] + 2, i[1] + 2) in blue\
                and (i[0] + 3, i[1] + 3) in blue:
            move_blue_diagonal += 1
            print(22)
        if move_blue_diagonal == 2:
            print('Синий выйграл!')
            return

def yellow_win(yellow):
    move_yellow_x = 1
    move_yellow_y = 1
    move_yellow_diagonal = 1

    yellow.sort(key=lambda x: (x[0]))
    for i in yellow:
        if (i[0] + 1, i[1]) in yellow\
                and (i[0] + 2, i[1]) in yellow\
                and (i[0] + 3, i[1]) in yellow:

            move_yellow_x += 1
        if move_yellow_x == 4:
            print('Желтый выйграл!')
            return
    for i in yellow:
        if (i[0], i[1] + 1) in yellow\
                and (i[0], i[1] + 2) in yellow\
                and (i[0], i[1] + 3) in yellow:
            move_yellow_y += 1
        if move_yellow_y == 2:
            print('Желтый выйграл!')
            return
    for i in yellow:
        if (i[0] + 1, i[1] + 1) in yellow and (i[0] + 2, i[1] + 2) in yellow and (i[0] + 3, i[1] + 3) in yellow:

            move_yellow_diagonal += 1
        if move_yellow_diagonal == 2:
            print('Желтый выйграл!')
            return


def get_win(list_move):
    blue = []
    yellow = []
    count = 0
    move_blue = 1
    for i in list_move:
        count += 1
        if count % 2 == 0:
            yellow.append(i)
        else:
            blue.append(i)
    blue_win(blue)
    yellow_win(yellow)
            # break
    # print(blue)
    # print(yellow)

# [(6, 0), (4, 0), (6, 1), (3, 0), (5, 0), (2, 0), (6, 2), (3, 1)]
#
# get_win([(6, 0), (4, 0), (6, 1), (3, 0), (6, 2), (2, 0), (5, 0), (3, 1)])
