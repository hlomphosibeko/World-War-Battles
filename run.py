#Legends
# 'X' marks a HIT
# '&' marks my ships position
# 'O' as placeholders
#'-' marks a MISSED

from random import randint
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
        self.my_ships = []


    def print(self):
        for row in self.player_board: 
            print("   ".join(row))

    
    def guess_generator(self,x,y,player_name):
        """
        This function inserts 'X' inside the board on coordinates
        x and y. It creates a tuple containing x and y, and appends
        it to the my_guesses list.
        """
        self.my_guesses.append((x,y))

        if (x,y) in self.my_ships:
            self.player_board[x][y] = 'X'
            print(f"{player_name} hit the ship!!")
            scores[player_name] += 1
            return "Hit"
        else:
            print(f"{player_name} unfortunately missed the ship!")
            self.player_board[x][y] = '-'
            return "Missed"


    def ship_generator(self,x,y,player_name):
        """
        This function inserts '&' as a ship inside the board on
        coordinates x and y. It creates a tuple containing x and
        y and appends it to the my_ships list.
        """
        if player_name == 'Computer':
            return self.my_ships.append((x,y)) 
        else:
            self.player_board[x][y] = '&'
            self.my_ships.append((x,y))    
            return


    def random_number(self,size):
        """
        This function generates a random number between 0 and size.
        """
        return randint(0,size-1)

def valid_name(x):
    """
    This function checks if the name inserted is a valid one.
    """
    while True:
        try:
            if type(x) != str:
                raise ValueError(f"Sorry, {x} is not a proprt name. Please add add a valid name")
                return x
        except ValueError as e:
            print(f"You unfortunately entered {e} which is not a valid name. Please enter a valid name.")
            return False
        return True


def valid_number(x):
    """
    This function checks if the number inserted is a valid one.
    """
    while True:
        try:
            x = int(input("Please insert board size: "))
            return x
        except ValueError as x:
            print(f"You unfortunately entered {x} which is not a valid number. Please enter a valid number.")
            
def valid_coordinates(x, y, board):
    """
    validate that the cordinates inputs that validates that not yet guessed.
    Validate that they are not outside our board.
    """
    list_range = [0, 1, 2, 3, 4, 5, 6, 7]
    try:
        if x not in list_range:
            raise ValueError(f"Sorry you entered invalid input {x}!")
    except ValueError as err:
        print(f"Invalid guess: {err}, which is outside the range, please try any of the following numbers 0, 1, 2, 3, 4, 5, 6, 7\n")
        return False
    try:
        if y not in list_range:
            raise ValueError(f"Sorry you entered invalid input {y}!")
    except ValueError as err:
        print(f"Invalid guess: {err}, which is outside the range, please try one of the following numbers 0, 1, 2, 3, 4, 5, 6, 7\n")
        return False
    try:
        if (x, y) in board.my_guesses:
            raise ValueError(f"Sorry you have already guessed {(x,y)}!")
    except ValueError as err:
        print(f"Invalid guess:{err},please try again.\n")
        return False
    try:
        if type(x) is str:
            raise ValueError(f"Sorry you have supplied a string {x}!")
    except ValueError as err:
        print(f"Invalid guess: {err}, please try one of the following numbers 0, 1, 2, 3, 4, 5, 6, 7\n")
        return False
    return True       

def valid_int(x):
    """
    check if input is a number
    """
    while True:
        try:
            x = int(input('Enter your number:'))
            return x
        except ValueError as x:
            print(f"Sorry you have supplied: {x} Which is not a Whole Number! please try one of the following numbers 0, 1, 2, 3, 4, 5, 6, 7\n")

def make_guess(board):
    """
    if it is computer guess it choses random column and a rondom column.
    if it is a player guess then it promts the input.
    """
    x = None
    y = None
    if board.player_name == 'Player':
        while True:
            x = valid_int(x)
            y = valid_int(y)
            if (valid_coordinates(x, y, board)):
                break
        return board.guess_generator(x, y,board.player_name)
    else:
        return board.guess_generator(board.random_number(5),board.random_number(5),board.player_name)

def run_game():
    """
    This function runs game.
    """
    print("."*35)
    print("This Is World War Battles")
    player_name = input("Please insert your name: \n")
    #x = input("Please insert your name: \n")
    #player_name = valid_name(x)
    print(f"Hello {player_name}, Welcome to World War Battles!!")
    print("."*35)
    my_size = 5
    num_of_ships = my_size
    hlompho_board = Board(my_size,num_of_ships,'Computer','Player')
    computer_board = Board(my_size,num_of_ships,'Player','Computer')
    for x in range(my_size):
        hlompho_board.ship_generator(hlompho_board.random_number(num_of_ships),hlompho_board.random_number(num_of_ships), player_name)
        computer_board.ship_generator(computer_board.random_number(num_of_ships),computer_board.random_number(num_of_ships), 'Computer')

    print(f"{player_name}'s initial board.")
    hlompho_board.print()
    print("."*35)
    print("Computer's initial board")
    
    computer_board.print()
    print("."*35)
    print("."*35)
    print("<<<<<----- First round.----->>>>>")
    print(f"score on this round: Computer: {scores['Computer']} || {player_name}: {scores['Player']}")
    print("."*35)
    for x in range(my_size):
        print("."*35)
        print("Computer Board")
        #computer_board.ship_generator(computer_board.random_number(num_of_ships),computer_board.random_number(num_of_ships), 'Computer')
        #computer_board.guess_generator(int(input("Please insert a row number of where ship is located: ")),int(input("Please insert a column number of where ship is located: ")), 'Player')
        make_guess(computer_board)
        computer_board.print()
        print("."*35)
        print(f"{player_name}'s Board")
        #hlompho_board.ship_generator(hlompho_board.random_number(num_of_ships),hlompho_board.random_number(num_of_ships), player_name)
        #make_guess.guess_generator(hlompho_board.random_number(num_of_ships), hlompho_board.random_number(num_of_ships), 'Computer')
        make_guess(hlompho_board)
        hlompho_board.print()
        print("."*35)
        print(f"Score on this round: Computer: {scores['Computer']} || {player_name}: {scores['Player']}")
        
    print("."*35)
    print("."*35)
    print("You have used all your turns.")

run_game()  
