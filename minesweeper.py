import random

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# declare a two-dimension array (9 x 9) with each element value as 0
# -:Un-swapped; m:mine; 2:found-mine; 3:failed mine; 4; empty
rows, cols = (8, 8)
fieldArray = [['-' for i in range(cols)] for j in range(rows)]


def laying_mine(count):
    rate = rows * cols / count
    mined = 0
    while mined < count:
        for r in range(rows):
            for c in range(cols):
                if mined < count:
                    if fieldArray[r][c] != 'm':
                        if 1 == random.randint(0, rate.__round__()):
                            fieldArray[r][c] = 'm'
                            mined = mined + 1


def print_field(display_mine):
    head = []
    row_number = 0
    for i in range(cols):
        head.append(i)
    print('  ', end='')
    print(head)
    for line in fieldArray:
        print(row_number, end=': ')
        for e in line:
            if display_mine is False:
                if e == '-':
                    print('-'+', ',end='')
                if e == 'm':
                    print('-'+', ',end='')
                if e == 'r' or e == 'f':
                    print('P'+', ',end='')
                if e == 'u':
                    print('u' + ', ', end='')
                if e == 'b':
                    print('m' + ', ', end='')
                if str(e).isdigit() is True:
                    print(str(e) + ', ', end='')
            if display_mine is True:
                print(str(e) + ', ', end='')
        print('\n')
        row_number += 1


def is_num(value):
    try:
        value+1
    except TypeError:
        return False
    else:
        return True


def insert_m(x,y):
    if fieldArray[y][x] == '-':
        fieldArray[y][x] = 'f'  # false mine
    elif fieldArray[y][x] == 'f':
        fieldArray[y][x] = '-'
    if fieldArray[y][x] == 'm':
        fieldArray[y][x] = 'r'  # real mine
    elif fieldArray[y][x] == 'r':
        fieldArray[y][x] = 'm'


def count_mine_in_game():
    findmine = 0
    for i in range(rows):
        for j in range(cols):
            if 'm' == fieldArray[i][j]:
                findmine += 1
            if 'f' == fieldArray[i][j]:
                findmine += 1
    return findmine


def around_mine_num(x, y):
    minenum = 0
    if y >= 1 and x >= 1:  # top left
        if fieldArray[y - 1][x - 1] == 'm' or fieldArray[y - 1][x - 1] == 'r':
            minenum += 1
    if y >= 1:  # top
        if fieldArray[y - 1][x] == 'm' or fieldArray[y - 1][x] == 'r':
            minenum += 1
    if y >= 1 and x <= cols - 2:  # top right
        if fieldArray[y - 1][x + 1] == 'm' or fieldArray[y - 1][x + 1] == 'r':
            minenum += 1
    if x >= 1:  # left
        if fieldArray[y][x - 1] == 'm' or fieldArray[y][x - 1] == 'r':
            minenum += 1
    if x <= cols - 2:  # right
        if fieldArray[y][x + 1] == 'm' or fieldArray[y][x + 1] == 'r':
            minenum += 1
    if y <= rows - 2:  # down
        if fieldArray[y + 1][x] == 'm' or fieldArray[y + 1][x] == 'r':
            minenum += 1
    if x >= 1 and y <= rows - 2:  # down left
        if fieldArray[y + 1][x - 1] == 'm' or fieldArray[y + 1][x - 1] == 'r':
            minenum += 1
    if x <= cols - 2 and y <= rows - 2:  # down right
        if fieldArray[y + 1][x + 1] == 'm' or fieldArray[y + 1][x + 1] == 'r':
            minenum += 1
    return minenum


def insert_wrong_or_right(insertlist, rows, cols):
    wrong_input = 0
    if wrong_input == 0:
        if len(insertlist) != 3:
            print('wrong format!')
            wrong_input = 1
    if wrong_input == 0:
        if not insertlist[0].isdigit() or not insertlist[1].isdigit():
            print('not digit!')
            wrong_input = 1
        insertlist[0] = int(insertlist[0])
        insertlist[1] = int(insertlist[1])
    print(insertlist)
    if wrong_input == 0:
        if insertlist[0] > rows - 1 or insertlist[1] > cols - 1:
            print('out of limit!')
            wrong_input = 1
    if wrong_input == 0:
        if insertlist[2] != 'm' and insertlist[2] != 'n':
            print('not m or n!')
            wrong_input = 1
    if wrong_input == 0:
        return 1


def main_loop():
    win = 0
    while win == 0:
        insert_right = 0
        print_field(True)  # real value in list
        print_field(False)  # display value
        insert = input("Insert in num(y),num(x),n/m: ")
        insertlist = insert.split(',')
        insert_right = insert_wrong_or_right(insertlist,rows,cols)
        if insert_right == 1:
            y = int(insertlist[0])
            x = int(insertlist[1])
            mn = insertlist[2]
            print('correct input!')
            print(y, x, mn)
            if mn == 'n':
                if fieldArray[y][x] == 'm':
                    fieldArray[y][x] = 'b'  # boom
                    win = -1
                    print('game over')
                    print_field(True)
                if fieldArray[y][x] == '-':
                    fieldArray[y][x] = 'u'  # discovered
                    fieldArray[y][x] = around_mine_num(x,y)
            if mn == 'm':
                insert_m(x, y)
            if count_mine_in_game() == 0:
                print('Win !')
                win = 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = 0
    laying_mine(10)

    main_loop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
