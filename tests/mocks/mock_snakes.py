from unittest.mock import create_autospec
from src.snake import Snake
from mocks.mock_board import get_mock_board

def get_mock_snake(type, head, tail, board):
    mock_snake = create_autospec(Snake)(type, board)
    mock_snake.type = type
    mock_snake.head = head
    mock_snake.tail = tail
    return mock_snake

def get_6_mock_snakes():
    mock_board = get_mock_board(10)
    mock_snake1 = get_mock_snake("short", 68, 45, mock_board)
    mock_snake2 = get_mock_snake("short", 79, 52, mock_board)
    mock_snake3 = get_mock_snake("short", 36, 17, mock_board)
    mock_snake4 = get_mock_snake("short", 89, 54, mock_board)
    mock_snake5 = get_mock_snake("long", 95, 27, mock_board)
    mock_snake6 = get_mock_snake("long", 57, 10, mock_board)
    return [mock_snake1, mock_snake2, mock_snake3, mock_snake4, mock_snake5, mock_snake6]