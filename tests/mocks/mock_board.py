from unittest.mock import create_autospec
from src.board import Board

def get_mock_board(N):
    mock_board= create_autospec(Board)(N)
   
    mock_board.N = N
    board = []
    for i in range(N, 0, -1):
            if(i%2):
                board.append([( N*(i-1))+(j+1) for j in range(N)])
            else:
                board.append([(N*(i-1))+(j) for j in range(N, 0, -1)])
    
    board = [[{"position": position,"isSnake": False,"isLadder": False,"unit": None, "players": {}} for position in row] for row in board]
    mock_board.board = board
    mock_board.total_snakes = int(N/2) + 1
    mock_board.total_ladders = int(N/2) + 1
    def row_side_effect(pos):
        return N - int(pos/N) if pos % N == 0 else N - int(pos/N) - 1
    def column_side_effect(pos):
        row = row_side_effect(pos)
        direction = row % 2 != 0 if N % 2 == 0 else row % 2 == 0
        return (N + pos % N - 1) % N if direction else (N - pos % N) % N
    mock_board.get_row.side_effect = row_side_effect
    mock_board.get_column.side_effect = column_side_effect
    return mock_board