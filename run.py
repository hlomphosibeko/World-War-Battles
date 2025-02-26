# Legends
# 'X' marks a HIT
# '&' marks my ships position
# 'O' as placeholders
# '-' marks a MISSED

from random import randint
import os
scores = {"Computer": 0, "Player": 0}


class Board:
    """
    It will set the board size, insert ships, prompt a player
    to insert their name, create a board for both the player
    and computer.
    """
    def __init__(self, size, num_of_ships, player_name, game_type):
        self.size = size
        self.num_of_ships = num_of_ships
        self.player_name = player_name
        self.game_type = game_type
        self.player_board = [['O' for x in range(size)] for y in range(size)]
        self.my_guesses = []
        self.my_ships = set()

    def print(self):
        """
        This function prints the board.
        """
        for row in self.player_board:
            print("   ".join(row))

    def guess_gen(self, x, y):
        """
        This function generates a guess.
        It inserts 'X' inside the board on coordinates
        x and y. It creates a tuple containing x and y, and appends
        it to the my_guesses list.
        """
        self.my_guesses.append((x, y))

        if (x, y) in self.my_ships:
            self.player_board[x][y] = 'X'
            return "Hit"
        else:
            self.player_board[x][y] = '-'
            return "Missed"

    def ship_gen(self, x, y):
        """
        This function generates the ships.
        It inserts '&' as a ship inside the board on
        coordinates x and y. It creates a tuple containing x and
        y and appends it to the my_ships list.
        """
        if self.game_type == 'Computer':
            return self.my_ships.add((x, y))
        else:
            self.player_board[x][y] = '&'
            self.my_ships.add((x, y))

    def random_num(self):
        """
        This function generates a random number between 0 and size.
        """
        return randint(0, self.size-1)


class BoardMixin:
    """
    Handles the defense mechanism of the game.
    """
    def description():
        """
        This function describes what the game is about.
        """
        print("""
World War Battles is a Python terminal game,
which runs in the Code Institute mock terminal on Heroku.
It is a strategy type guessing game,
where a player is playing against the computer
to find its hidden ships.
All ships have to be sunk to win the game.
It is a strategy type guessing game for two players.
The rows read from 0 up to but not including
the size number, eg: row 0 is the first row, 
and row 1 is the second row and etc. Similarly,
column 0 is the first column, and column 1 is 
the second column and etc.""")

    def valid_name(name):
        """
        This function checks if the name inserted is a valid name.
        """
        while True:
            try:
                name = name.encode('ascii')
            except UnicodeError as e:
                print(
                    f"The name {e.object} has a character at position {e.start} that cannot be encoded in {e.encoding} due to {e.reason} '\n You may continue with the game...")
            return name

    def valid_size():
        """
        check if input is a number
        """
        while True:
            try:
                x = int(input('Insert the size of the board:'))
                return x
            except ValueError as err:
                print(f"{err} is not a Whole Number! Enter valid number...")

    def valid_int(prompt):
        """
        check if row and column input is a number
        """
        while True:
            try:
                x = int(input(prompt))
                return x
            except ValueError:
                print("This is not a Whole Number! Enter valid number...")

    def valid_coordinates(x, y, board):
        """
        It validates the input is not repeated.
        Validate that they are not outside our board.
        """
        while True:
            try:
                if x >= board.size:
                    raise ValueError(f"Sorry you entered invalid input {x}!")
            except ValueError as err:
                print(f"{err} is more than board size.")
                return False
            try:
                if y >= board.size:
                    raise ValueError(f"Sorry you entered invalid input {y}!")
            except ValueError as err:
                print(f"{err} is more than board size.")
                return False
            try:
                if (x, y) in board.my_guesses:
                    raise ValueError(
                        f"Sorry you have already guessed {(x,y)}!")
            except ValueError as err:
                print(f"Invalid guess:{err},please try again.\n")
                return False
            return True


def wedge(lines=1, length=35):
    for x in range(lines):
        print("." * length)


def make_guess(board):
    """
    if it is computer guess it choses random column and a random column.
    if it is a player guess then it prompts the input.1
    """

    if board.player_name == 'Computer':
        while True:
            x = BoardMixin.valid_int('Insert row number of ship location: ')
            y = BoardMixin.valid_int('Insert column number of ship location: ')
            if (BoardMixin.valid_coordinates(x, y, board)):
                break
        return board.guess_gen(x, y)
    else:
        return board.guess_gen(board.random_num(), board.random_num())


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def play_game(computer_board, my_board):
    wedge(1, 35)
    for x in range(my_board.size):
        print(f"<<<<<----- Round {x +1}.----->>>>>")
        wedge(1, 35)
        resc = make_guess(computer_board)
        resi = make_guess(my_board)
        clear_terminal()
        print(f"{computer_board.player_name}'s Board")
        computer_board.print()
        print(
            f"{my_board.player_name} Guessed {computer_board.my_guesses[-1]}")
        if resc == "Hit":
            print(
                f"{my_board.player_name} Bombed {computer_board.player_name}'s ship!!!!")
            scores['Player'] += 1
        else:
            print(
                f"{my_board.player_name} Missed {computer_board.player_name}'s ship!!!!")
        wedge(2, 35)
        print(f"{my_board.player_name}'s Board")
        my_board.print()
        print(
            f"{computer_board.player_name} Guessed {my_board.my_guesses[-1]}")
        if resi == "Hit":
            print(
                f"{computer_board.player_name} Bombed {my_board.player_name}'s ship!!!!")
            scores['Computer'] += 1
        else:
            print(
                f"{computer_board.player_name} Missed the {my_board.player_name}'s ship!!!!")
        wedge(2, 35)
        print("Updated scores: ")
        print(
            f"Computer: {scores[computer_board.player_name]} {my_board.player_name}: {scores['Player']}"
        )
    wedge(2, 35)
    print("You have used all your turns.")
    print("The game is over!!.")


def start_game():
    """
    This function runs game.
    """
    wedge(1, 80)
    print("WORLD WAR BATTLES!!")
    BoardMixin.description()
    wedge(2, 80)
    player_name = None
    while True:
        y = input("Please insert your name:")
        x = len(y)
        if x <= 0 or y.isnumeric():
            print(
                f"Sorry you entered '{y}' which is not a valid name.")
        else:
            player_name = y
            break
    BoardMixin.valid_name(player_name)
    clear_terminal()
    print(f"Hello {player_name}, Welcome to World War Battles!!")
    wedge(1, 35)
    size = BoardMixin.valid_size()
    num_ships = size-1
    my_board = Board(size, num_ships, player_name, 'Player')
    computer_board = Board(size, num_ships, 'Computer', 'Computer')
    while len(my_board.my_ships) < size:
        my_board.ship_gen(my_board.random_num(), my_board.random_num())
        computer_board.ship_gen(
            computer_board.random_num(), computer_board.random_num())
    print("Computer's initial board: ")
    computer_board.print()
    wedge(1, 35)
    print(f"{player_name}'s initial board:")
    my_board.print()
    wedge(1, 35)
    play_game(computer_board, my_board)


start_game()
