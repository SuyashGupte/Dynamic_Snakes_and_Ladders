import unittest
from tests.mocks.mock_board import get_mock_board
from tests.mocks.mock_players import get_2_mock_players
from src.game import Game
import io
import sys

class TestGame(unittest.TestCase):

    def setUp(self):
        self.mock_board = get_mock_board(10)
        self.game = Game("auto", get_2_mock_players(), self.mock_board)

    def test_game_initialized(self):
        self.assertTrue(self.game.board.board == self.mock_board.board)

    def test_game_players_not_zero(self):
        self.assertRaises(Exception, Game, "auto", [], self.mock_board)

    def test_die_roll(self):
        num = self.game.roll_die()
        self.assertIn(num, [1,2,3,4,5,6])
    
    def test_all_players_start_at_one(self):
        self.assertTrue(len(self.game.board.board[9][0]["players"]) == len(self.game.players))

    def test_players_crossed_finish_do_not_roll_again(self):
        players = get_2_mock_players()
        players[0].finished = True
        game = Game("auto", players, self.mock_board)
        game.rankings.append(players[0])
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        game.start()                                  
        sys.stdout = sys.__stdout__                     
        self.assertTrue(f"{players[0].name}'s turn" not in capturedOutput.getvalue())

    def test_all_players_play(self):
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        self.game.start()                                  
        sys.stdout = sys.__stdout__
        for player in get_2_mock_players():                    
            self.assertTrue(f"{player.name}'s turn" in capturedOutput.getvalue())
