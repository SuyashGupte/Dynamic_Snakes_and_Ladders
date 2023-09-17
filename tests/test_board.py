import unittest
from unittest.mock import patch
from src.board import Board
from src.ladder import Ladder

@patch('src.board.Board.add_snakes', return_value=None)
@patch('src.board.Board.add_ladders', return_value=None)
class TestBoard(unittest.TestCase):

    def test_board_is_sqaure(self, mocked_add_snakes, mocked_Add_ladders):
        N=10
        board = Board(N)
        playing_board = board.board
        self.assertTrue(len(playing_board) == N and len(playing_board[0]) == N)

    def test_board_width_is_greater_than_ten(self, mocked_add_snakes, mocked_add_ladders):
        N=7
        self.assertRaises(AssertionError, Board, N)

    def test_board_starts_with_one(self, mocked_add_snakes, mocked_add_ladders):
        N=13
        board = Board(N)
        playing_board = board.board
        self.assertTrue(playing_board[N-1][0]["position"] == 1)

    def test_board_ends_with_N_squared(self, mocked_add_snakes, mocked_add_ladders):
        N=11
        board = Board(N)
        playing_board = board.board
        self.assertTrue(playing_board[0][N - 1]["position"] == 121)

    def test_short_long_snakes_60_40_split(self, mocked_add_snakes, mocked_add_ladders):
        N=10
        board = Board(N)
        self.assertTrue(board.short_snakes == 4 and board.long_snakes == 2)

    def test_total_snakes_are_one_more_than_half_board_width(self, mocked_add_snakes, mocked_add_ladders):
        N=10
        board = Board(N)
        self.assertTrue(board.total_snakes == 6)

    def test_short_long_ladders_60_40_split(self, mocked_add_snakes, mocked_add_ladders):
        N=10
        board = Board(N)
        self.assertTrue(board.short_ladders == 4 and board.long_ladders == 2)

    def test_total_ladders_are_one_more_than_half_board_width(self, mocked_add_snakes, mocked_add_ladders):
        N=11
        board = Board(N)
        self.assertTrue(board.total_ladders == 6)
