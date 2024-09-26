#Legend
# X for placing ship and hit battleship
# '-' for missed shot

from random import randint

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

        
    def populate_board(board):
        pass



