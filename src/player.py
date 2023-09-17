from src.ladder import Ladder
from src.snake import Snake

class Player():
    
    __players = []
    def __init__(self, player_name:str, player_colour:str):
        self.__name =  player_name
        self.__colour = player_colour
        self.__curr_position:int = 1
        self.__history:list[str] = []
        self.finished:bool = False
        self.__swallowed_by_snakes:int = 0
        self.__climbed_ladders:int = 0
        self.__die_rolls:int = 0
        self.__check_if_name_and_colour_available()
        Player.__players.append(self)
    
    def __check_if_name_and_colour_available(self):
        for player in Player.__players:
            if(player.colour == self.colour):
                raise Exception("Colour Taken")
            if(player.name == self.name):
                raise Exception("Player name already used")
            
    def move(self, n:int):
        if(n > 6):
            raise Exception("Player can't move more than 6 steps without a snake or ladder.")
        self.__curr_position = self.__curr_position + n
        self.__die_rolls = self.__die_rolls + 1
        self.__history.append(f"Moved {n} steps. At {self.curr_position}.")

    def climbed(self, ladder:Ladder):
        self.__curr_position = ladder.end
        self.__climbed_ladders = self.__climbed_ladders + 1
        self.__history.append(f"Climed Ladder. At {self.curr_position}.")

    def swallowed(self, snake: Snake):
        self.__curr_position = snake.tail
        self.__swallowed_by_snakes = self.__swallowed_by_snakes + 1
        self.__history.append(f"swallowed by snake. Back at {self.curr_position}.")

    @property
    def name(self):
        return self.__name
    
    @property
    def colour(self):
        return self.__colour

    @property
    def curr_position(self):
        return self.__curr_position
    
    @property
    def history(self):
        return self.__history
    
    @property
    def swallowed_by_snakes(self):
        return self.__swallowed_by_snakes
    
    @property
    def climbed_ladders(self):
        return self.__climbed_ladders

    @property
    def die_rolls(self):
        return self.__die_rolls

    @classmethod
    def get_players(cls):
        return cls.__players
    
    @history.setter
    def history(self, value):
        self.__history.append(value)
     
    @classmethod        
    def reset(cls):
        cls.__players = []