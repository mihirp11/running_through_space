import unittest
from unittest.mock import patch
import main
import card_deck
from create_board import create_board

def prepare_deck():
    return [{'name': 'Move 1', 'function': 'move_1'}, {'name': 'Next Planet', 'function': 'next_planet'},
     {'name': 'Miss a turn', 'function': 'miss_a_turn'}]

def prepare_board():
    return [{'name': 'Start', 'type': 'start', 'position': 0}, {'name': 'Wormhole 3', 'type': 'wormhole', 'position': 1},
     {'name': 'Orion', 'type': 'star', 'position': 2}, {'name': "Cat's Eye", 'type': 'nebula', 'position': 3},
     {'name': 'Wormhole 1', 'type': 'wormhole', 'position': 4}, {'name': 'Earth', 'type': 'planet', 'position': 5},
     {'name': 'Polaris', 'type': 'star', 'position': 6},{'name': 'Mars', 'type': 'planet', 'position': 7},
     {'name': 'Little Ghost', 'type': 'nebula', 'position': 8}]

class Testtodo(unittest.TestCase):

    draw_again = '2'

    @patch('builtins.input', return_value=draw_again)
    def test_get_player_card_two(self, mock_input):
        deck = prepare_deck()
        card = main.get_player_card(deck)
        self.assertEqual(type(card), dict)
        self.assertEqual(card['name'], 'Next Planet')


    draw_again = '1'

    @patch('builtins.input', return_value=draw_again)
    def test_get_player_card(self, mock_input):
        deck = prepare_deck()
        card = main.get_player_card(deck)
        self.assertEqual(type(card), dict)
        self.assertEqual(card['name'], 'Move 1')


    def test_next_planet(self):
        board = prepare_board()
        position = card_deck.next_planet(0, board)
        self.assertEqual(board[position]['type'], 'planet')
        self.assertEqual(position, 5)

    def test_next_nebula(self):
        board = prepare_board()
        position = card_deck.next_nebula(0, board)
        self.assertEqual(board[position]['type'], 'nebula')
        self.assertEqual(position, 3)

    def test_closest_wormhole(self):
        board = prepare_board()
        position = card_deck.closest_wormhole(2, board)
        self.assertEqual(board[position]['type'], 'wormhole')
        self.assertEqual(position, 1)
        self.assertEqual(board[position]['name'], 'Wormhole 3')

    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), 50)
        self.assertEqual(board[0]['name'], 'Start')
        self.assertEqual(board[49]['name'], 'End')
