from create_board import shuffle


def create_cards():
    cards = []
    f = open("cards.txt", "r")
    lines = f.read().splitlines()
    for line in lines:
        card = line.split(",")
        function = card[0].lower().replace(' ', '_')
        d = {
            'name': card[0],
            'function': function
        }
        for i in range(0, int(card[1])):
            cards.append(d)
    shuffle(cards)
    return cards


def give_next_type(position, board, type):
    for index, square in enumerate(board[position:50]):
        if square['type'] == type:
            return position + index
    print("No" + type + "  left, next player's turn: ")
    return position


def next_planet(position, board):
    return give_next_type(position, board, 'planet')


def next_nebula(position, board):
    return give_next_type(position, board, 'nebula')


def next_star(position, board):
    return give_next_type(position, board, 'star')


def move_5(position, b):
    return position + 5


def move_4(position, b):
    return position + 4


def move_3(position, b):
    return position + 3


def move_2(position, b):
    return position + 2


def move_1(position, b):
    return position + 1


def move_back_2(position, b):
    return position - 2


def move_back_1(position, b):
    return position - 1


def miss_a_turn(position, b):
    return position


def closest_wormhole(position, board):
    for index, square in enumerate(board[position:]):
        if square['type'] == 'wormhole':
            indexf = index
            break
        indexf = 50
    for index, square in enumerate(board[position::-1]):
        if square['type'] == 'wormhole':
            indexb = index
            break
        indexb = 50
    if indexf <= indexb:
        return position + indexf
    else:
        return position - indexb


def last_planet(position, board):
    for index, square in enumerate(board[::-1]):
        if square['type'] == 'planet':
            index = 50 - index
            return index


    
