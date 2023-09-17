class Board():

    def __init__(self, board_width:int):
        assert board_width >= 10
        self.__N = board_width
        self.__board:list[list[dict]]= []
        for i in range(board_width, 0, -1):
            if(i%2):
                #increasing order
                self.__board.append([self.__get_board_unit((board_width*(i-1))+(j+1)) for j in range(board_width)])
            else:
                #decreasing order
                self.__board.append([self.__get_board_unit((board_width*(i-1))+(j)) for j in range(board_width, 0, -1)])
        self.__total_snakes = (int(board_width/2)+1)
        # 60% of snakes are short snakes
        self.__short_snakes = int(0.6 * self.total_snakes) if int(0.6 * self.total_snakes) > int(self.total_snakes/2) else int(0.6 * self.total_snakes) + 1
        self.__long_snakes = self.total_snakes - self.__short_snakes
        self.__total_ladders = self.__total_snakes
        self.__short_ladders = self.__short_snakes
        self.__long_ladders = self.__long_snakes
        self.add_snakes()
        self.add_ladders()

    @staticmethod
    def __get_board_unit(num) -> dict:
        return {
            "position": num,
            "isSnake": False,
            "isLadder": False,
            "unit": None,
            "players": {}
        }
    
    def get_row(self, pos: int) -> int:
        return self.__N - int(pos/self.__N) if pos%self.__N == 0 else self.__N - int(pos/self.__N) -1
    
    def get_column(self, pos: int) -> int:
        row = self.get_row(pos)
        direction = row%2 != 0 if self.__N%2==0 else row%2==0
        return (self.__N + pos%self.__N - 1)%self.__N if direction else (self.__N - pos%self.__N)%self.__N
    
    def add_snakes(self):
        from src.snake import Snake
        for i in range(0, self.short_snakes):
            snake=Snake("short", self)
            self.board[self.get_row(snake.head)][self.get_column(snake.head)]["isSnake"] = True
            self.board[self.get_row(snake.head)][self.get_column(snake.head)]["unit"] = snake
      
        for i in range(0, self.long_snakes):
            snake = Snake("long", self)
            self.board[self.get_row(snake.head)][self.get_column(snake.head)]["isSnake"] = True
            self.board[self.get_row(snake.head)][self.get_column(snake.head)]["unit"] = snake
  
    def add_ladders(self):
        from src.ladder import Ladder
        for i in range(0, self.short_ladders):
            ladder = Ladder("short", self)
            self.board[self.get_row(ladder.start)][self.get_column(ladder.start)]["isLadder"] = True
            self.board[self.get_row(ladder.start)][self.get_column(ladder.start)]["unit"] = ladder
    
        for i in range(0, self.long_ladders):
            ladder= Ladder("long", self)
            self.board[self.get_row(ladder.start)][self.get_column(ladder.start)]["isLadder"] = True
            self.board[self.get_row(ladder.start)][self.get_column(ladder.start)]["unit"] = ladder

    @property
    def board(self):
        return self.__board
    
    @property
    def short_snakes(self):
        return self.__short_snakes
    
    @property
    def long_snakes(self):
        return self.__long_snakes
    
    @property
    def short_ladders(self):
        return self.__short_ladders
    
    @property
    def long_ladders(self):
        return self.__long_ladders
    
    @property
    def N(self):
        return self.__N
    
    @property
    def total_snakes(self):
        return self.__total_snakes
    
    
    @property
    def total_ladders(self):
        return self.__total_ladders
