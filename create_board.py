import random


def shuffle(deck):
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def create_board():
    squares = []
    f = open("board.txt", "r")
    lines = f.read().splitlines()
    for line in lines:
        square_id = line.split(",")
        d = {
            'name': square_id[0],
            'type': square_id[1]
        }
        if d['type'] == 'wormhole':
            squares.append(d)
        squares.append(d)
    f.close()
    shuffle(squares)
    squares.append({'name': 'End', 'type': 'end'})
    squares.insert(0, {'name': 'Start', 'type': 'start'})
    for square in squares:
        square['position'] = squares.index(square)
    return squares

