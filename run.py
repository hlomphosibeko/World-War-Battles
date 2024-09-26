#Legend
# X for placing ship and hit battleship
# '-' for missed shot

from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    This is the main board. It sets the board size, numbers of ships, and player's name. It also allows the player to play against the computer.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []


    def new_game():
        """
        Starts a new game. Sets the board size and number of the ships, resets the scores and initialises the boards.
        """

        size = 8
        num_ships = 5
        scores["computer"] = 0
        scores["player"] = 0
        print("Welcome to WORLD WAR BATTLESHIPS!!!")
        print(f"Board Size: {size}. Number of ships: {num_ships}")
        print("Top left corner is row: 0, col: 0")
        print("-" * 35)
        player_name = input("Please enter your name: \n")
        print("-" * 35)
        
        computer_board = Board(size, num_ships, "computer", type="computer")
        player_board = Board(size, num_ships, player_name, type="player1")

        for _ in range(num_ships):
            populate_board(player_board)
            populate_board(computer_board)
        
        play_game(computer_board, player_board)

       
    new_game()


