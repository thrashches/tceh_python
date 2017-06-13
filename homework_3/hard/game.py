# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
#import random
from random import shuffle
from os import system

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}
LEFT_WALL = range(0, 13, 4)
RIGHT_WALL = range(3, 16, 4)
TOP = range(0, 4)
BOTTOM = range(12,16)

def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    new_field = list(range(1, 16))
    new_field.append(EMPTY_MARK)
    shuffle(new_field)
    return new_field
    #pass


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """

    for item in range(0, 16, 4):
        r_item = item + 4
        print(field[item:r_item])
    #pass


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if field == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']:
        return True
    else:
        return False
    #pass


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """


    empty = field.index(EMPTY_MARK)
    try:    ###Я пока не придумал как проверить лучше. Мне не нравится этот if. Очень похоже на быдлокод.
        if (empty in LEFT_WALL and key == 'a') or (empty in RIGHT_WALL and key == 'd') or (empty in TOP and key == 'w') or (empty in BOTTOM and key == 's'):
            raise IndexError()
        for mv, val in MOVES.items():
            if key == mv:
                field[empty] = field[empty+val]
                field[empty+val] = EMPTY_MARK
        return field
    except IndexError:
        return None

    #pass


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    #move =
    move = str()
    while move not in ['w', 'a', 's', 'd']:
        print('Используйте только "w", "a", "s", "d"!')
        move = input('Ваш ход: ')
    else:
        return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    #field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'x', 14, 15]
    ##Uncomment line 114 for win check!
    print_field(field)
    #print(handle_user_input())
    while not is_game_finished(field):

        if perform_move(field, handle_user_input()) != None:
            system('clear')
            print_field(field)
        else:
            system('clear')
            print_field(field)
            print('За поля не заходить!')
    print('Победа!!!')
    #pass


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()