from src.board import Board
from src.player import Player
import time
import random
from typing import List

class Game():
    
    def __init__(self, game_type: str, players: List[Player], board: Board):
        if(len(players) == 0):
            raise Exception("Need atleast 1 player to play")     
        self.players = players
        self.board = board
        self.game_type = game_type
        self.rankings:list[Player] = []
        for player in players:
            self.__get_current_place(player)["players"][player.name] = player

    @staticmethod
    def __get_ranking_string(n:int) -> str:
        if(n%10==1 and  str(n)[-2:]!="11"):
            return "1st"
        if(n%10==2 and str(n)[-2:]!="12"):
            return "2nd"
        if(n%10==3 and str(n)[-2:]!="13"):
            return "3rd"
        return f"{n}th"

    def roll_die(self) -> int:
        if(self.game_type == "manual"):
            input("Press Enter to roll the die")
        #Each turn after 0.5 seconds
        elif(self.game_type =="auto-slowed"):
            time.sleep(0.5)
        return random.randint(1,6)
    
    def __print_stats(self):
        for i,player in enumerate(self.rankings):
            print(f"{player.name} finished {self.__get_ranking_string(i+1)} and it took {player.die_rolls} die rolls.")
            print(f"{player.name} was swallowed by {player.swallowed_by_snakes} snakes.")
            print(f"{player.name} climbed {player.climbed_ladders} ladders.\n")

    def __handle_finished(self, player:Player):
            self.rankings.append(player)
            player.finished = True
            print(f"{player.name} finished {self.__get_ranking_string(len(self.rankings))}.")
            player.history.append("Finished.")
            print("------------\n")

    def __get_current_place(self, player:Player) -> dict:
        return self.board.board[self.board.get_row(player.curr_position)][self.board.get_column(player.curr_position)]

    def __handle_snake_and_ladder(self, player: Player):
        place = self.__get_current_place(player)
        if(place["isSnake"]):
            player.swallowed(place["unit"])
            print(f"Oops! {player.name} was swallowed by a Snake!")
        elif(place["isLadder"]):
            player.climbed(place["unit"])
            print(f"Yay! {player.name} climmed a Ladder!")

    def start(self):
        # continue till all players have reached finished
        while (len(self.rankings) != len(self.players)):
            #go in order as players we added
            for player in self.players:
                if(not player.finished):
                    chance_complete = False
                    print(f"{player.name}'s turn")
                    #Player gets another turn on rolling 6.
                    while not chance_complete:
                        num = self.roll_die()
                        print(f"{player.name} rolled {num}")
                        #move from old position
                        place = self.__get_current_place(player)
                        del place["players"][player.name]
                        #stop at new position
                        player.move(num)
                        #check if finished
                        if(player.curr_position >= self.board.N * self.board.N):
                            self.__handle_finished(player)
                            break
                        
                        self.__handle_snake_and_ladder(player)
                        #update location on board
                        self.__get_current_place(player)["players"][player.name] = player
                        print(f"{player.name} at {player.curr_position}")

                        if(num!=6):
                            print("------------\n")
                            chance_complete = True
        self.__print_stats()
