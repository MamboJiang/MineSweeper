import random

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# declare a two-dimension array (9 x 9) with each element value as 0
# -:Un-swapped; m:mine; 2:found-mine; 3:failed mine; 4; empty
rows, cols = (8, 8)
fieldArray = [['-' for i in range(cols)] for j in range(rows)]
y = 0
x = 0
mn = ''
minenum = 0

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
    rownumber = 0
    for i in range(cols):
        head.append(i)
    print('  ',end='')
    print(head)
    for line in fieldArray:
        print(rownumber,end=': ')
        for e in line:
            if display_mine == False:
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
                if str(e).isdigit() == True:
                    print(str(e) + ', ', end='')
            if display_mine == True:
                print(str(e) + ', ', end='')
        print('\n')
        rownumber += 1

def is_num(value):
    try:
        value+1
    except TypeError:
        return False
    else:
        return True

def main_loop():
    win = 0
    while win == 0:
        print_field(True)  # real value in list
        print_field(False)  # display value
        insert = input("Insert in num(y),num(x),n/m: ")
        insertlist = insert.split(',')
        if len(insertlist) != 3:
            print('wrong format!')
            continue
        if not insertlist[0].isdigit() or not insertlist[1].isdigit():
            print('not digit!')
            continue
        insertlist[0] = int(insertlist[0])
        insertlist[1] = int(insertlist[1])
        print(insertlist)
        if insertlist[0] > rows-1 or insertlist[1] > cols-1:
            print('out of limit!')
            continue
        if insertlist[2] != 'm' and insertlist[2] != 'n':
            print('not m or n!')
            continue
        else:
            y = int(insertlist[0])
            x = int(insertlist[1])
            mn = insertlist[2]
            print('correct input!')
            print(y, x, mn)
            if mn == 'n':
                if fieldArray[y][x] == 'm':
                    fieldArray[y][x] = 'b' #boom
                    win = -1
                    print('game over')
                    print_field(True)
                if fieldArray[y][x] == '-':
                    fieldArray[y][x] = 'u'  # discovered
                    minenum = 0
                    if y-1 < 0 and not x-1 < 0 and not x+1 > cols-1:  # top row
                        if fieldArray[y][x-1] == 'm' or fieldArray[y][x-1] == 'r':
                            minenum += 1
                        if fieldArray[y][x+1] == 'm'or fieldArray[y][x+1] =='r':
                            minenum += 1
                        if fieldArray[y+1][x-1] == 'm'or fieldArray[y+1][x-1] =='r':
                            minenum += 1
                        if fieldArray[y+1][x] == 'm'or fieldArray[y+1][x] == 'r':
                            minenum += 1
                        if fieldArray[y+1][x+1] == 'm'or fieldArray[y+1][x+1] == 'r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if y - 1 < 0 and x - 1 < 0:  # top left corner
                        if fieldArray[y][x + 1] == 'm'or fieldArray[y][x + 1] == 'r':
                            minenum += 1
                        if fieldArray[y + 1][x] == 'm'or fieldArray[y + 1][x] == 'r':
                            minenum += 1
                        if fieldArray[y + 1][x + 1] == 'm'or fieldArray[y + 1][x + 1] == 'r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if y-1 < 0 and x+1 > cols-1:  # top right corner
                        if fieldArray[y][x-1] == 'm'or fieldArray[y][x-1] == 'r':
                            minenum += 1
                        if fieldArray[y+1][x-1] == 'm'or fieldArray[y+1][x-1] == 'r':
                            minenum += 1
                        if fieldArray[y+1][x] == 'm'or fieldArray[y+1][x] =='r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if not y-1 < 0 and x-1 < 0 and not y+1 > rows-1:  # left col
                        if fieldArray[y-1][x] == 'm'or fieldArray[y-1][x] == 'r':
                            minenum += 1
                        if fieldArray[y-1][x+1] == 'm'or fieldArray[y-1][x+1] =='r':
                            minenum += 1
                        if fieldArray[y][x+1] == 'm'or fieldArray[y][x+1] == 'r':
                            minenum += 1
                        if fieldArray[y+1][x] == 'm'or fieldArray[y+1][x] =='r':
                            minenum += 1
                        if fieldArray[y+1][x+1] == 'm'or fieldArray[y+1][x+1] =='r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if not y-1 < 0 and not y+1 > rows-1 and x+1 > cols-1:  # right col
                        if fieldArray[y-1][x-1] == 'm'or fieldArray[y-1][x-1] =='r':
                            minenum += 1
                        if fieldArray[y-1][x] == 'm'or fieldArray[y-1][x] == 'r':
                            minenum += 1
                        if fieldArray[y][x-1] == 'm'or  fieldArray[y][x-1] == 'r':
                            minenum += 1
                        if fieldArray[y+1][x-1] == 'm'or fieldArray[y+1][x-1] =='r':
                            minenum += 1
                        if fieldArray[y+1][x] == 'm'or fieldArray[y+1][x] =='r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if not x-1 < 0 and y+1 > rows-1 and not x+1 > cols-1:  # down row
                        if fieldArray[y-1][x-1] == 'm'or fieldArray[y-1][x-1] =='r':
                            minenum += 1
                        if fieldArray[y-1][x] == 'm'or fieldArray[y-1][x] =='r':
                            minenum += 1
                        if fieldArray[y-1][x+1] == 'm'or fieldArray[y-1][x+1] =='r':
                            minenum += 1
                        if fieldArray[y][x-1] == 'm'or fieldArray[y][x-1] == 'r':
                            minenum += 1
                        if fieldArray[y][x+1] == 'm'or fieldArray[y][x+1] == 'r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if x-1 < 0 and y+1 > rows-1:  # down left corner
                        if fieldArray[y-1][x] == 'm'or fieldArray[y-1][x] =='r':
                            minenum += 1
                        if fieldArray[y][x+1] == 'm'or fieldArray[y][x+1] =='r':
                            minenum += 1
                        if fieldArray[y-1][x+1] == 'm'or fieldArray[y-1][x+1] == 'r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if x+1 > cols-1 and y+1 > rows-1:  # down right corner
                        if fieldArray[y-1][x] == 'm' or fieldArray[y-1][x] == 'r':
                            minenum += 1
                        if fieldArray[y-1][x-1] == 'm' or fieldArray[y-1][x-1] =='r':
                            minenum += 1
                        if fieldArray[y][x-1] == 'm' or fieldArray[y][x-1] == 'r':
                            minenum += 1
                        fieldArray[y][x] = minenum
                    if not x+1 > cols-1 and not y+1 > rows-1 and not x-1<0 and not y-1<0:
                        if fieldArray[y-1][x-1] == 'm'or fieldArray[y-1][x-1] =='r':
                            minenum += 1
                        if fieldArray[y-1][x] == 'm' or fieldArray[y-1][x] =='r':
                            minenum += 1
                        if fieldArray[y-1][x+1] == 'm' or fieldArray[y-1][x+1] =='r':
                            minenum += 1
                        if fieldArray[y][x-1] == 'm' or fieldArray[y][x-1] =='r':
                            minenum += 1
                        if fieldArray[y][x+1] == 'm' or fieldArray[y][x+1] == 'r':
                            minenum += 1
                        if fieldArray[y+1][x-1] == 'm' or fieldArray[y+1][x-1] =='r':
                            minenum += 1
                        if fieldArray[y+1][x+1] == 'm' or fieldArray[y+1][x+1] == 'r':
                            minenum += 1
                        if fieldArray[y+1][x] == 'm' or fieldArray[y+1][x] =='r':
                            minenum += 1
                        fieldArray[y][x] = minenum
            if mn == 'm':
                if fieldArray[y][x] == '-':
                    fieldArray[y][x] = 'f' #false mine
                elif fieldArray[y][x] == 'f':
                    fieldArray[y][x] = '-'
                if fieldArray[y][x] == 'm':
                    fieldArray[y][x] = 'r' #real mine
                elif fieldArray[y][x] == 'r':
                    fieldArray[y][x] = 'm'
            findmine = 0
            for i in range(rows):
                for j in range(cols):
                    if 'm' == fieldArray[i][j]:
                        findmine += 1
                    if 'f' == fieldArray[i][j]:
                        findmine += 1
            if findmine == 0:
                print('Win !')
                win = 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    win = 0
    laying_mine(5)

    main_loop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
