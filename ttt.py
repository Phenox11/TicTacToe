import sys
import logging
from itertools import chain

a = 0
b = 0


class board:
    # b = [[" ", 1, 2, 3], ['A', 0, 0, 0], ['B', 0, 0, 0], ['C', 0, 0, 0]]
    b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def print_board():
    print("   0  1  2")
    for count, x in enumerate(board.b):
        print(count, x)


def user_input():
    global a
    global b
    a = input("enter column name\n")
    b = input('enter row number \n')
    return [int(a), int(b)]


def game_engine1():
    print('for user 1')
    x = user_input()
    # modify_board(a, b)
    if spot_checker() == True:
        board.b[int(b)][int(a)] = 1
        print_board()
        game_logic()
    else:
        print("can't place there")
        game_engine1()


def player2():
    print('for user 2')
    x = user_input()
    # modify_board(a, b)
    if spot_checker() == True:
        board.b[int(b)][int(a)] = 2
        print_board()
        game_logic()
    else:
        print("can't place there")
        player2()


def board_check():
    c = 0
    flat_list = []
    for sublist in board.b:
        for item in sublist:
            flat_list.append(item)
    if c not in flat_list:
        game_over()
    else:
        return True


def spot_checker():
    global a, b
    if board_check() == True:
        if board.b[int(b)][int(a)] == 0:
            return True
    else:
        return False


def game_logic():

    if horizontal_check() == 1:
        print('player 1 won')
        sys.exit()
    elif horizontal_check() == 2:
        print("player 2 won")
        sys.exit()
    else:
        pass
    vertical_check()


def horizontal_check():
    for r in board.b:
        result1 = all(elem == 1 for elem in r)
        result2 = all(elem == 2 for elem in r)
        if result1 == True:
            return 1
        else:
            pass
        if result2 == True:
            return 2
        else:
            pass


def vertical_check():
    flat_list = []
    c1 = []
    c2 = []
    c3 = []
    for sublist in board.b:
        for item in sublist:
            flat_list.append(item)
    c1 = flat_list[0::3]
    c2 = flat_list[1::3]
    c3 = flat_list[2::3]


def game_over():
    print("game_over()")


if __name__ == "__main__":
    x = game_logic()
    print_board()
    while x != True:
        game_engine1()
        player2()
