from unittest.mock import create_autospec
from src.player import Player

def get_mock_player(player_name, player_colour):
    mock_player = create_autospec(Player)(player_name,player_colour)
    mock_player.name = player_name
    mock_player.colour = player_colour
    mock_player.curr_position=1
    mock_player.finished = False
    mock_player.history = []
    mock_player.swallowed_by_snakes = 0
    mock_player.climbed_ladders = 0
    mock_player.die_rolls = 0
    def move_side_effect(n):
        mock_player.curr_position = mock_player.curr_position + n

    def swallowed_side_effect(snake):
        mock_player.curr_position = snake.tail

    def climbed_side_effect(ladder):
        mock_player.curr_position = ladder.end

    mock_player.move.side_effect = move_side_effect
    mock_player.swallowed.side_effect = swallowed_side_effect
    mock_player.climbed.side_effect = climbed_side_effect
    return mock_player

def get_2_mock_players():
    mock_player1 = get_mock_player("test_player_1", "red")
    mock_player2 = get_mock_player("test_player_2", "blue")
    return [mock_player1, mock_player2]