import os
import time
import numpy
import math

board = [[3, 0, 0, 8, 0, 1, 0, 0, 2],
         [2, 0, 1, 0, 3, 0, 6, 0, 4],
         [0, 0, 0, 2, 0, 4, 0, 0, 0],
         [8, 0, 9, 0, 0, 0, 1, 0, 6],
         [0, 6, 0, 0, 0, 0, 0, 5, 0],
         [7, 0, 2, 0, 0, 0, 4, 0, 9],
         [0, 0, 0, 5, 0, 9, 0, 0, 0],
         [9, 0, 4, 0, 8, 0, 7, 0, 5],
         [6, 0, 0, 1, 0, 7, 0, 0, 3]]

# arrBoard = numpy.array(board)
arrBoard = numpy.zeros((9,9), dtype='int32')
arrEmptyTile = numpy.argwhere(arrBoard == 0)

# Enable this instead if you want to create sudoku with 0's
# arrEmptyTile = numpy.full_like(arrBoard, 0)


def print_board(delay = 0):
    if delay > 0:
        time.sleep(delay)
        os.system("cls")
    else:
        os.system("cls")

    for x, row in enumerate(arrBoard):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - - - - - ")
        for y, tile in enumerate(row):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")
            print(f" {tile} ", end="")
        print()


def get_small_board_square(index_y, index_x):
    start_slice_x = math.floor(index_x / 3) * 3
    start_slice_y = math.floor(index_y / 3) * 3

    result_array = arrBoard[start_slice_y:start_slice_y + 3, start_slice_x:start_slice_x + 3]

    return result_array


cursor = 0

print_board()
user_input = input("Solve it? ")

if user_input != 'y':
    exit()

while True:

    indexY, indexX = arrEmptyTile[cursor]

    if arrBoard[indexY][indexX] > 0:
        tryAnswerStartRange = arrBoard[indexY][indexX]
    else:
        tryAnswerStartRange = 1

    correctAnswer = False

    smallBoardSquare = get_small_board_square(indexY, indexX)

    for tryAnswer in range(tryAnswerStartRange, 10):

        if tryAnswer in arrBoard[indexY]:
            continue

        if tryAnswer in arrBoard[0:9, indexX]:
            continue

        if tryAnswer in smallBoardSquare:
            continue

        correctAnswer = True

        arrBoard[indexY][indexX] = tryAnswer

        if correctAnswer:
            break

    print_board()

    if not correctAnswer:
        arrBoard[indexY][indexX] = 0
        cursor -= 1
    else:
        cursor += 1

    if cursor == len(arrEmptyTile) or cursor < 0:
        break
