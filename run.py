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


def run_game():
    """
    This function runs game.
    """
    print("."*35)
    print("This Is World War Battles")
    player_name = input("Please insert your name: \n")
    print(f"Hello {player_name}, Welcome to World War Battles!!")
    print("."*35)
    my_size = int(input("Please insert board size: "))
    num_of_ships = my_size
    hlompho_board = Board(my_size,num_of_ships,'Hlompho','Hlompho')
    computer_board = Board(my_size,num_of_ships,'Computer','Computer')
    for x in range(my_size):
        hlompho_board.ship_generator(hlompho_board.random_number(num_of_ships),hlompho_board.random_number(num_of_ships), player_name)
        computer_board.ship_generator(computer_board.random_number(num_of_ships),computer_board.random_number(num_of_ships), 'Computer')

    print("Hlompho's initial board.")
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
        computer_board.guess_generator(int(input("Please insert a row number of where ship is located: ")),int(input("Please insert a column number of where ship is located: ")), 'Player')
        computer_board.print()
        print("."*35)
        print(f"{player_name}'s Board")
        #hlompho_board.ship_generator(hlompho_board.random_number(num_of_ships),hlompho_board.random_number(num_of_ships), player_name)
        hlompho_board.guess_generator(hlompho_board.random_number(num_of_ships), hlompho_board.random_number(num_of_ships), 'Computer')
        hlompho_board.print()
        print("."*35)
        print(f"Score on this round: Computer: {scores['Computer']} || {player_name}: {scores['Player']}")
        
    print("."*35)
    print("."*35)
    print("You have used all your turns.")

run_game()  


    






# TheBoards.print(TheBoards(8,5,'Hlompho','Hlompho'))
#ndalo_board = TheBoards(8,5,'Ndalo','Ndalo')
#ndalo_board.guess_generator(2,2)
#ndalo_board.print()
#hlompho_board = TheBoards(8,5,'Hlompho','Hlompho')
#hlompho_board.ship_generator(4,2)
#hlompho_board.guess_generator(4,2)
#hlompho_board.print()
#b = TheBoards.ship_generator(TheBoards(8,5,'Hlompho','Hlompho'),2,5)
#TheBoards.print(b)
#my_board = [['!','!','!','!','!'],['!','!','!','!','!'],['!','!','!','!','!'],['!','!','!','!','!'],['!','!','!','!','!']]
#my_list[0][4] = 'a'
#print(my_list)

#my_list[0][4] = '*'
#print(my_list)

#my_list[4][4] = 'X'
#print(my_list)


#my_guesses.append((0, 0))


#ship_generator(random_number(int(input("Insert size: "))),random_number(int(input("Insert size: "))))
#ship_generator(3,0)
#print(my_board)
#print(my_ships)
#print(my_guesses[0])


#x = random_number(4)
#print(x)

#guess_generator(int(input("Insert a row: ")), int(input("Insert a column: ")))
#guess_generator(2,1)
#print(my_board)
#print(my_guesses)

#create_board(3)
#print(create_board(3))




