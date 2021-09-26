# Author: Philip Beck
# Email: stoneroll6@gmail.com
# Date: 11/25/2020
# Description:
#    Unit testing for FocusGame.py
#    For educational use only,
#    Not for commercial use


import unittest
from FocusGame import FocusGame

class FocusGameTest(unittest.TestCase):
    """
    Contains unit tests for FocusGame.py
    """

    def test_winner_a(self):
        """Test checks if winner==PlayerA possible"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playera', (0, 0), (0, 1), 1)
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 2)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 3)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 4)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 5)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        game.move_piece('Playera', (0, 5), (1, 5), 5)
        game.move_piece('Playerb', (3, 0), (3, 1), 1)
        game.move_piece('Playera', (1, 5), (2, 5), 5)
        game.move_piece('Playerb', (3, 1), (3, 2), 1)
        game.move_piece('Playera', (2, 5), (3, 5), 5)
        game.move_piece('Playerb', (5, 1), (5, 2), 1)
        game.move_piece('Playera', (3, 5), (3, 4), 5)
        game.move_piece('Playerb', (5, 2), (4, 2), 1)
        game.move_piece('Playera', (3, 4), (4, 4), 5)
        game.move_piece('Playerb', (4, 2), (4, 3), 1)
        result = game.move_piece('Playera', (4, 4), (5, 4), 5)
        self.assertEqual(result, 'PlAyerA wins')

    def test_winner_b(self):
        """Test checks if winner==PlayerB possible"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 1)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 1)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 1)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (1, 5), (2, 5), 5)
        game.move_piece('Playera', (2, 1), (2, 2), 1)
        game.move_piece('Playerb', (2, 5), (3, 5), 5)
        game.move_piece('Playera', (2, 2), (2, 1), 1)
        game.move_piece('Playerb', (3, 5), (4, 5), 5)
        game.move_piece('Playera', (2, 1), (2, 0), 1)
        game.move_piece('Playerb', (4, 5), (4, 4), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (4, 4), (4, 0), 5)
        game.move_piece('Playera', (2, 1), (2, 0), 1)
        game.move_piece('Playerb', (4, 0), (4, 1), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (4, 1), (4, 3), 5)
        game.move_piece('Playera', (2, 1), (2, 0), 1)
        result = game.move_piece('Playerb', (4, 3), (3, 3), 5)
        self.assertEqual(result, 'PlaYerB wins')

    def test_winner_reserved(self):
        """Test checks if winner possible w/ reserved moves"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 3)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 4)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (1, 5), (2, 5), 5)
        game.move_piece('Playera', (2, 1), (2, 2), 1)
        game.move_piece('Playerb', (2, 5), (3, 5), 5)
        game.move_piece('Playera', (2, 2), (2, 1), 1)
        game.move_piece('Playerb', (3, 5), (4, 5), 5)
        game.move_piece('Playera', (2, 1), (2, 0), 1)
        game.reserved_move('Playerb', (0, 5))
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (0, 5), (0, 0), 5)
        game.move_piece('Playera', (2, 1), (2, 2), 2)
        game.move_piece('Playerb', (0, 0), (0, 2), 5)
        game.move_piece('Playera', (2, 2), (2, 3), 3)
        game.move_piece('Playerb', (0, 2), (0, 3), 5)
        game.move_piece('Playera', (2, 3), (2, 4), 4)
        game.move_piece('Playerb', (0, 3), (0, 4), 5)
        game.move_piece('Playera', (4, 0), (4, 1), 1)
        game.reserved_move('Playerb', (2, 4))
        game.move_piece('Playera', (4, 1), (4, 3), 2)
        result = game.move_piece('Playerb', (4, 5), (4, 3), 5)
        self.assertEqual(result, 'PlaYerB wins')

    def test_move_success_no_adjust(self):
        """Test checks if successful move returns message,
        no adjustments to piecestack <= 5"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playera', (0, 2), (0, 3), 1)
        result = game.move_piece('Playerb', (1, 1), (1, 2), 1)
        self.assertEqual(result, 'Successfully moved')

    def test_move_success_w_adjust(self):
        """Test checks if successful move returns message,
        w/ adjustments to piecestack > 5"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 3)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 4)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (1, 5), (2, 5), 5)
        game.move_piece('Playera', (2, 1), (2, 2), 1)
        result = game.move_piece('Playerb', (2, 5), (3, 5), 5)
        self.assertEqual(result, 'Successfully moved')

    def test_show_reserve(self):
        """Test checks if reserve is displaying and
        calculating correctly"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 3)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 4)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (1, 5), (2, 5), 5)
        game.move_piece('Playera', (2, 1), (2, 2), 1)
        game.move_piece('Playerb', (2, 5), (3, 5), 5)
        result = game.show_reserve('playerb')
        self.assertEqual(result, 2)

    def test_show_captured(self):
        """Test checks if captured is displaying and
        calculating correctly"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 3)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 4)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (1, 5), (2, 5), 5)
        game.move_piece('Playera', (2, 1), (2, 2), 1)
        game.move_piece('Playerb', (2, 5), (3, 5), 5)
        result = game.show_captured('pLayerb')
        self.assertEqual(result, 1)

    def test_adjust_piecestack(self):
        """Test checks if piecestacks adjusting to 5
        AND show_pieces displaying properly"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 3)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 4)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        game.move_piece('Playera', (2, 0), (2, 1), 1)
        game.move_piece('Playerb', (1, 5), (2, 5), 5)
        result = game.show_pieces((2, 5))
        self.assertEqual(result, ['G', 'R', 'R', 'G', 'G'])

    def test_no_reserve(self):
        """Test checks if reserved move returns error message
        if no pieces in reserve"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        game.move_piece('Playerb', (1, 2), (1, 3), 3)
        game.move_piece('Playera', (0, 3), (0, 4), 3)
        game.move_piece('Playerb', (1, 3), (1, 4), 4)
        game.move_piece('Playera', (0, 4), (0, 5), 4)
        game.move_piece('Playerb', (1, 4), (1, 5), 5)
        result = game.reserved_move('PlayEra', (0, 5))
        self.assertEqual(result, 'No pieces in reserve')

    def test_invalid_player(self):
        """Test checks if error message returned
        with invalid player name"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        result = game.move_piece('PlaASDFSADF', (1, 2), (1, 3), 3)
        self.assertEqual(result, 'Player not found')

    def test_invalid_turn(self):
        """Test checks if error message returned
        with player out of turn"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        result = game.move_piece('Playera', (0, 3), (1, 3), 3)
        self.assertEqual(result, 'Not your turn')

    def test_invalid_location(self):
        """Test checks if error message returned
        with wrong location"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        result = game.move_piece('Playerb', (0, 3), (1, 3), 3)
        self.assertEqual(result, 'Invalid location')

    def test_empty_source(self):
        """Test checks if error message returned
        with empty source"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        result = game.move_piece('Playerb', (1, 0), (1, 1), 1)
        self.assertEqual(result, 'Invalid location')

    def test_invalid_quantity(self):
        """Test checks if error message returned
        with invalid quantity of pieces"""
        game = FocusGame(('PlAyerA', 'R'), ('PlaYerB', 'G'))
        game.move_piece('Playerb', (1, 0), (1, 1), 1)
        game.move_piece('Playera', (0, 1), (0, 2), 1)
        game.move_piece('Playerb', (1, 1), (1, 2), 2)
        game.move_piece('Playera', (0, 2), (0, 3), 2)
        result = game.move_piece('Playerb', (1, 2), (1, 3), 5)
        self.assertEqual(result, 'Invalid number of pieces')


if __name__ == '__main__':
    unittest.main()
