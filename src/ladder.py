import random
from src.board import Board

class Ladder():

    __ladders = []

    def __init__(self, ladder_type: str, game: Board):
        self.__type = ladder_type
        if(ladder_type == "short"):
            max_len = int(0.2*game.N)
            min_len = 1
        elif(ladder_type == "long"):
            max_len = int(0.6*game.N)
            min_len = int(0.2*game.N+1)
        else:
            raise Exception("Ladder Type can only be long or short!")

        self.__start = self.__generate_ladder_position(game, min_len + 1, game.N - 1)
        head_row = game.get_row(self.__start)
        self.__end = self.__generate_ladder_position(game, max(0, head_row - max_len - 1), head_row - min_len - 1)
        Ladder.__ladders.append(self)

    def __generate_ladder_position(self, game: Board, start_row:int, end_row:int) -> int:
        valid = False
        random_row = 0
        random_column = 0
        while not valid:
            random_row = random.randint(start_row, end_row)
            random_column = random.randint(0, game.N-1)
            valid = self.__validate_position(game, random_row, random_column) 
        return game.board[random_row][random_column]["position"]
    
    def __validate_position(self, game:Board, random_row:int, random_column:int) -> bool:
        position = game.board[random_row][random_column]["position"]
        ladders_in_row = 0
        ladders_in_column = 0
        valid = True
        # check if ladder is not at start or end of board
        if(position==1 or position==game.N*game.N):
            return False
        #check if any ladder doesn't overlap with current ladder
        for ladder in Ladder.__ladders:
            if(ladder.start == position or ladder.end == position):
                valid = False
                break
            # get number of ladders in same row and column
            if(game.get_row(ladder.start)== random_row):
                ladders_in_row = ladders_in_row + 1
            if(game.get_column(ladder.start) == random_column):
                ladders_in_column = ladders_in_column + 1
        if(not valid):
            return valid

        #check if any snake doesn't overlap with current ladder
        from src.snake import Snake
        for snake in Snake.snakes():
            if(snake.head == position or snake.tail == position):
                valid = False
                break
        if(not valid):
            return valid
        
        max_ladders_per_row_or_column = 0.2 * game.total_ladders
        if(ladders_in_row + 1 > max_ladders_per_row_or_column):
            valid = False
            
        if(ladders_in_column + 1 > max_ladders_per_row_or_column):
            valid = False
          
        return valid
    
    @property
    def type(self):
        return self.__type
    
    @property
    def start(self):
        return self.__start
    
    @property
    def end(self):
        return self.__end
    
    @classmethod
    def ladders(cls):
        return cls.__ladders
      
    @classmethod        
    def reset(cls):
        cls.__ladders = []
