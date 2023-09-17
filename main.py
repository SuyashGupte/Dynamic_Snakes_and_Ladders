from src.board import Board
from src.player import Player
from src.game import Game


print("Snakes & Ladders\n")
try:
    board_width = int(input("Enter Board Width (Default: 10): "))
except:
    board_width = 10

board = Board(board_width)

num_players = int(input("\nEnter number of players: "))
players = []
for i in range(num_players):
    done = False
    while(not done):
        player_name = input("Player name: ")
        player_colour = input("Player colour: ")
        try:
            players.append(Player(player_name, player_colour))
            done = True
        except Exception as err:
            print(f"\nError: {err}\n")

game_type = ["auto", "auto-slowed" ,"manual"]
choice = 0
while(True):
    print("\nGame Type: \n")
    print("1) Auto")
    print("2) Auto-Slowed")
    print("3) Manual")
    try:
        choice = int(input("Enter Choice:"))
    except:
        print("Enter a number")
    if(choice>0 and choice <= len(game_type)+1):
        break
    else:
        print("Enter valid choice")


game = Game(game_type[choice-1], players, board)
game.start()







