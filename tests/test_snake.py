import unittest
from unittest.mock import create_autospec
from src.board import Board
from src.snake import Snake


class TestSnake(unittest.TestCase):

    def setUp(self):
        self.mock_board_class = create_autospec(Board)
        N = 10
        self.mock_game = self.mock_board_class(N)
        self.mock_game.N = N
        board = [[100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
                 [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
                 [80, 79, 78, 77, 76, 75, 74, 73, 72, 71],
                 [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                 [60, 59, 58, 57, 56, 55, 54, 53, 52, 51],
                 [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                 [40, 39, 38, 37, 36, 35, 34, 33, 32, 31],
                 [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                 [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        
        board = [[{"position": position,"isSnake": False,"isLadder": False,"unit": None} for position in row] for row in board]
        self.mock_game.board = board
        self.mock_game.total_snakes = 6
        self.mock_game.snakes = []

        def row_side_effect(pos):
            return N - int(pos/N) if pos % N == 0 else N - int(pos/N) - 1

        def column_side_effect(pos):
            row = row_side_effect(pos)
            direction = row % 2 != 0 if N % 2 == 0 else row % 2 == 0
            return (N + pos % N - 1) % N if direction else (N - pos % N) % N

        self.mock_game.get_row.side_effect = row_side_effect
        self.mock_game.get_column.side_effect = column_side_effect

    def tearDown(self):
        Snake.reset()

    def test_short_snake_generation(self):
        snake_type = "short"
        snake = Snake(snake_type, self.mock_game)
        self.assertTrue(snake.type == "short")

    def test_long_snake_generation(self):
        snake_type = "long"
        snake = Snake(snake_type, self.mock_game)
        self.assertTrue(snake.type == "long")

    def test_only_long_amd_short_snake_as_valid_types(self):
        snake_type = "extra_long"
        self.assertRaises(Exception, Snake, snake_type, self.mock_game)

    def test_snake_head_position_greater_than_tail_position(self):
        snake_type = "long"
        snake = Snake(snake_type, self.mock_game)
        self.assertTrue(snake.head > snake.tail)

    def test_snake_position_do_not_overlap(self):
        snake1 = Snake("long", self.mock_game)
        self.mock_game.snakes = [snake1]
        snake2 = Snake("long", self.mock_game)
        self.mock_game.snakes = []
        self.assertNotEqual(snake1.head, snake2.head)
        self.assertNotEqual(snake1.head, snake2.tail)
        self.assertNotEqual(snake1.tail, snake2.head)
        self.assertNotEqual(snake1.tail, snake2.tail)

    def test_short_snakes_are_short(self):
        snake = Snake("short", self.mock_game)
        self.assertTrue(3 >= self.mock_game.get_row(
            snake.tail) - self.mock_game.get_row(snake.head) >= 2)

    def test_long_snakes_are_long(self):
        snake = Snake("long", self.mock_game)
        self.assertTrue(7 >= self.mock_game.get_row(
            snake.tail) - self.mock_game.get_row(snake.head) >= 4)
