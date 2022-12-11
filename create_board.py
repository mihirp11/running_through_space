import random
import csv

def shuffle(deck):
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def create_board():
    squares = []
    with open('board.csv') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            if row['type'] == 'wormhole':
                squares.append(row)
            squares.append(row)
    f.close()
    shuffle(squares)
    squares.append({'name': 'End', 'type': 'end'})
    squares.insert(0, {'name': 'Start', 'type': 'start'})
    for square in squares:
        square['position'] = squares.index(square)
    return squares

