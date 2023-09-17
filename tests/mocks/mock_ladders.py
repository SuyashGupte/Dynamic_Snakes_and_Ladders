from unittest.mock import create_autospec
from src.ladder import Ladder
from mocks.mock_board import get_mock_board

def get_mock_ladder(type, start, end, board):
    mock_ladder = create_autospec(Ladder)(type, board)
    mock_ladder.type = type
    mock_ladder.start = start
    mock_ladder.end = end
    return mock_ladder

def get_6_mock_ladders():
    mock_board = get_mock_board(10)
    mock_ladder1 = get_mock_ladder("short", 22, 53, mock_board)
    mock_ladder2 = get_mock_ladder("short", 18, 41, mock_board)
    mock_ladder3 = get_mock_ladder("short", 34, 64, mock_board)
    mock_ladder4 = get_mock_ladder("short", 50, 70, mock_board)
    mock_ladder5 = get_mock_ladder("long", 60, 91, mock_board)
    mock_ladder6 = get_mock_ladder("long", 8, 65, mock_board)
    return [mock_ladder1,mock_ladder2,mock_ladder3,mock_ladder4,mock_ladder5,mock_ladder6]
