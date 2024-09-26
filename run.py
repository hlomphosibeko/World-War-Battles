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

    def play_game(computer_board, player_board):
        """
        Playing the game.
        """
        for i in range(5):
            print(f"{player_board.name}'s Board")
            player_board.print()
            print(f"{computer_board.name}'s Board")
            computer_board.print()
            results = make_guess(computer_board)
            print(f"{player_board.name} guessed: {computer_board.guesses[-1]}")
            print(f"{player_board.name} {results}ed!!!")

            if results == "Hit":
                scores["player1"] = scores["player1"]+1
            answer = make_guess(player_board)
            print(f"{computer_board.name} guessed: {player_board.guesses[-1]}")

            if answer =="Hit":
                scores["computer"] = scores["computer"]+1
            print(18*"--")
            print("After this round, the scores are:")
            print(f"{player_board.name}: {scores[player1]}.{computer_board.name}: {scores['computer']}")
            print(18*"--")

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


