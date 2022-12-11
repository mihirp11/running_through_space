import unittest
from unittest.mock import patch
import main


def prepare_deck():
    return [{'name': 'Move 1', 'function': 'move_1'}, {'name': 'Next Planet', 'function': 'next_planet'},
     {'name': 'Miss a turn', 'function': 'miss_a_turn'}]


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


