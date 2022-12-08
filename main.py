import card_deck
from create_board import create_board
import random
import csv


def get_player_card(deck):
    card = deck[0]
    print('You drew: ' + card['name'])
    deck.pop(0)
    print('1. Accept \n2. Draw Again \n')
    x = True
    while x:
        draw_choice = input()
        if draw_choice == '1':
            return card
        elif draw_choice == '2':
            card = deck[0]
            deck.pop(0)
            print('You drew: ' + card['name'])
            return card
        else:
            print('Please enter either 1 or 2 to get your card:')


def initial_display(board):
    squares = []
    for square in board:
        squares.append(square['name'])
    reverse_squares = squares[::-1]
    print('{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}'.format(*squares[0:10]))
    print(' '*125 + '|')
    print(' '*125 + '|')
    print('{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}'.format(*reverse_squares[30:40]))
    print(' '*4 + '|')
    print(' '*4 + '|')
    print('{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}'.format(*squares[20:30]))
    print(' '*125 + '|')
    print(' '*125 + '|')
    print('{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}'.format(*reverse_squares[10:20]))
    print(' '*4 + '|')
    print(' '*4 + '|')
    print('{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}-->{:^10}'.format(*squares[40:50]))


def player_turn(player, position, deck, board):
    card = get_player_card(deck)
    new_pos = make_move(card, position, board)
    if new_pos < 0:
        print("You get another card since you can't go behind the start")
        return player_turn(player, position, deck, board)

    elif new_pos < 50:
        new_square = board[new_pos]
        if new_square['type'] == 'wormhole':
            for index, square in enumerate(board):
                if square['name'] == new_square['name'] and new_pos != index:
                    new_pos = index
        print(player, 'You are now at the ', new_square['type'], new_square['name'] + ',', 49-new_pos, 'squares away from the end.')
    return new_pos


def play_game(p1, p2):
    deck = card_deck.create_cards()
    board = create_board()
    initial_display(board)
    round = 1
    p1_position = 0
    p2_position = 0
    while p1_position < 49 and p2_position < 49:
        print('---- Round ', round, '----')
        print('Player ' + p1['player name'] + "'s turn: ")
        p1_position = player_turn(p1['player name'], p1_position, deck, board)
        if p1_position >= 49:
            break
        print('Player ' + p2['player name'] + "'s turn: ")
        p2_position = player_turn(p2['player name'], p2_position, deck, board)
        round += 1
    if p1_position > p2_position:
        return p1
    else:
        return p2


def make_move(card, player, board):
    card_function = getattr(card_deck, card['function'])
    return card_function(player, board)


def find_in_winners(p1, p2):
    with open('player_history.csv') as f:
        csv_reader = csv.DictReader(f)
        winners_list = []
        wincount = []
        for row in csv_reader:
            winners_list.append(row['player name'])
            x = int(row['wins'])
            wincount.append({'player name': row['player name'], 'wins': x})
        print(winners_list)
        f.close()
        p1 = p1.lower()
        p2 = p2.lower()
        print(p1)
        if p1 not in winners_list:
            wincount.append({'player name': p1, 'wins': 0})
        if p2 not in winners_list:
            wincount.append({'player name': p2, 'wins': 0})
    return wincount


def main():
    p3 = input('Input Player 1 username: ')
    p4 = input('Input Player 2 username: ')
    if random.randint(1, 2) == 1:
        print('By random selection ' + p3 + ' is chosen to go first...')
        p1 = p3.strip()
        p2 = p4.strip()
    else:
        print('By random selection ' + p4 + ' is chosen to go first...')
        p2 = p3
        p1 = p4
    win_data = find_in_winners(p1, p2)
    for i in win_data:
        if i['player name'] == p1:
            p1 = i
        elif i['player name'] == p2:
            p2 = i
    print(p1, p2)
    winner = play_game(p1, p2)
    x = find(win_data, 'player name', winner['player name'])
    win_data[x]['wins'] += 1
    print(winner['player name'] + ' wins!\n',  winner['player name'] + ' now has a total of {} wins'.format(win_data[x]['wins']))
    update_win_file(win_data)
    print('1. Play Again \n2. Exit \n')
    loop = True
    while loop:
        x = input()
        if x == '1':
            main()
            break
        elif x == '2':
            print()
            break
        else:
            print('Input needs to be 1 or 2')
    print('Saving data and exiting')


def update_win_file(win_list):
    f = open('player_history.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['player name', 'wins'])
    for dictionary in win_list:
        writer.writerow(dictionary.values())
    f.close()


def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


if __name__ == '__main__':
    main()