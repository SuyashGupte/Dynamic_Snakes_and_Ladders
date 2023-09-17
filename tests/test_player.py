import unittest
from src.player import Player
from tests.mocks.mock_snakes import get_mock_snake
from tests.mocks.mock_ladders import get_mock_ladder
from tests.mocks.mock_board import get_mock_board


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("test_player", "blue")

    def tearDown(self):
        Player.reset()

    def test_initialize_player(self):
        self.assertTrue(self.player.name == "test_player")
        
    def test_colour_already_taken(self):
        self.assertRaises(Exception, Player, "test_player", "red")
        
    def test_name_already_taken(self):
        self.assertRaises(Exception, Player, "test_player_1", "blue")
        
    def test_player_starts_at_one(self):
        self.assertTrue(self.player.curr_position == 1)
        
    def test_player_moves_n_steps(self):
        prev_position = self.player.curr_position
        self.player.move(5)
        self.assertTrue(prev_position + 5 == self.player.curr_position)

    def test_player_cannot_move_more_than_6_steps(self):
        self.assertRaises(Exception, self.player.move, 7 )
        
    def test_player_swallowed_by_snake(self):
        snake = get_mock_snake("short", 78, 56, get_mock_board(10))
        self.player.swallowed(snake)
        self.assertTrue(self.player.curr_position == 56 )

    def test_player_climbed_ladder(self):
        ladder = get_mock_ladder("short", 56, 78, get_mock_board(10))
        self.player.climbed(ladder)
        self.assertTrue(self.player.curr_position == 78 )
        
    def test_player_history_is_updated(self):
        prev_history = self.player.history.copy() 
        self.player.move(4)
        self.assertTrue(len(self.player.history) == len(prev_history) + 1)
        self.assertEqual(self.player.history[-1], "Moved 4 steps. At 5.")

    def test_player_snake_swallow_count_is_updated(self):
        prev_count = self.player.swallowed_by_snakes
        snake = get_mock_snake("short", 91, 76, get_mock_board(10))
        self.player.swallowed(snake)   
        self.assertTrue(self.player.swallowed_by_snakes == prev_count + 1)

    def test_player_ladder_climbed_count_is_updated(self):
        prev_count = self.player.climbed_ladders
        ladder = get_mock_ladder("short", 23, 51, get_mock_board(10))
        self.player.climbed(ladder)
        self.assertTrue(self.player.climbed_ladders == prev_count + 1)

    def test_player_die_roll_count_is_updated(self):
        prev_count = self.player.die_rolls
        self.player.move(5)
        self.assertTrue(self.player.die_rolls == prev_count + 1)
