import unittest
from unittest.mock import  patch
from tests.mocks.mock_board import get_mock_board
from tests.mocks.mock_snakes import get_6_mock_snakes
from src.snake import Snake
from src.ladder import Ladder


class TestLadder(unittest.TestCase):
    def setUp(self):
        self.mock_board = get_mock_board(10)

    def tearDown(self):
        Ladder.reset()

    def test_short_ladder_generation(self):
        ladder_type = "short"
        ladder = Ladder(ladder_type, self.mock_board)
        self.assertTrue(ladder.type == "short")

    def test_long_ladder_generation(self):
        ladder_type = "long"
        ladder = Ladder(ladder_type, self.mock_board)
        self.assertTrue(ladder.type == "long")

    def test_only_long_amd_short_ladder_as_valid_types(self):
        ladder_type = "extra_long"
        self.assertRaises(Exception, Ladder, ladder_type, self.mock_board)

    def test_ladder_start_position_less_than_end_position(self):
        ladder_type = "long"
        ladder = Ladder(ladder_type, self.mock_board)
        self.assertTrue(ladder.start < ladder.end)

    def test_ladder_position_do_not_overlap(self):
        ladder1 = Ladder("long", self.mock_board)
        ladder2 = Ladder("long", self.mock_board)
        self.assertNotEqual(ladder1.start, ladder2.start)
        self.assertNotEqual(ladder1.start, ladder2.end)
        self.assertNotEqual(ladder1.end, ladder2.start)
        self.assertNotEqual(ladder1.end, ladder2.end)

    @patch('src.snake.Snake.snakes', return_value=get_6_mock_snakes())
    def test_ladder_do_not_overlap_with_snake(self, mocked_snakes):
        ladder = Ladder("long", self.mock_board)
        for snake in Snake.snakes():
            self.assertTrue(ladder.start != snake.head)
            self.assertTrue(ladder.start != snake.tail)
            self.assertTrue(ladder.end != snake.head)
            self.assertTrue(ladder.end != snake.tail)

    def test_short_ladders_are_short(self):
        ladder = Ladder("short", self.mock_board)
        self.assertTrue( 3 >= self.mock_board.get_row(ladder.start) - self.mock_board.get_row(ladder.end) >=2)

    def test_long_ladders_are_long(self):
        ladder = Ladder("long", self.mock_board)
        self.assertTrue( 7 >= self.mock_board.get_row(ladder.start) - self.mock_board.get_row(ladder.end) >= 2)
