import random
from src.board import Board

class Snake():

    __snakes = []
    def __init__(self, snake_type: str, game: Board):
        self.__type = snake_type
        if(snake_type == "short"):
            max_len = int(0.2*game.N)
            min_len = 1
        elif(snake_type == "long"):
            max_len = int(0.6*game.N)
            min_len = int(0.2*game.N+1)
        else:
            raise Exception("Snake Type can only be long or short!")

        self.__head = self.__generate_snake_position(game, 0, game.N - 2 - min_len)
        head_row = game.get_row(self.__head)
        self.__tail = self.__generate_snake_position(game, head_row + min_len + 1, min(game.N - 1, head_row + max_len + 1))
        Snake.__snakes.append(self)

    def __generate_snake_position(self, game:Board, start_row:int, end_row:int):
        valid = False
        random_row = 0
        random_column = 0
        while not valid:
            random_row = random.randint(start_row, end_row)
            random_column = random.randint(0, game.N-1)
            valid = self.__validate_position(game, random_row, random_column) 
        return game.board[random_row][random_column]["position"]
    
    def __validate_position(self, game:Board, random_row:int, random_column:int):
        position = game.board[random_row][random_column]["position"]
        snakes_in_row = 0
        snakes_in_column = 0
        valid = True
        # check if snake is not at start or end of board
        if(position==1 or position==game.N * game.N):
            return False
        # check if any snake doesn't overlap with current snake
        for snake in Snake.__snakes:
            if(snake.head == position or snake.tail == position):
                valid = False
                break
            # get total snakes in current row and column
            if(game.get_row(snake.head)== random_row):
                snakes_in_row = snakes_in_row + 1
            if(game.get_column(snake.head) == random_column):
                snakes_in_column = snakes_in_column + 1

        if(not valid):
            return valid
        
        max_snakes_per_row_or_column = 0.2 * game.total_snakes
        if(snakes_in_row + 1 > max_snakes_per_row_or_column):
            valid = False
        if(snakes_in_column + 1 > max_snakes_per_row_or_column):
            valid = False 
        return valid
    
    @property
    def type(self):
        return self.__type
    
    @property
    def head(self):
        return self.__head
    
    @property
    def tail(self):
        return self.__tail
    
    @classmethod
    def snakes(cls):
        return cls.__snakes
          
    @classmethod        
    def reset(cls):
        cls.__snakes = []
