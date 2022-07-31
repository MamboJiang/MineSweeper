import random

# Provide several methods to distribute mines

######################################
# interface:
# bool lay_mine_methodName(field_2D_array, mine_number, except_coord)
# input:    field_2D_array, should be a rectangle
#           mine_number, how many mines should be laying
#           except_coordinate，this place can't set mine
# output:   laying successful or not
#           char 'm' in field_2D_array indicates mine
######################################

# The simplest algorithm is to randomly select a location,
# and if there is no mine, place a mine.
# This method is very similar to the physical means of mine in reality.
def lay_mine_random_place(field_2D_array, mine_number, except_coord):
    row_bound = len(field_2D_array) - 1
    column_bound = len(field_2D_array[0]) - 1

    lay_done_number = 0
    while lay_done_number < mine_number:
        row = random.randint(0, row_bound)
        col = random.randint(0, column_bound)
        exp_row, exp_col = except_coord
        if row != exp_row or col != exp_col:
            if field_2D_array[row][col] != 'm':
                field_2D_array[row][col] = 'm'
                lay_done_number += 1
