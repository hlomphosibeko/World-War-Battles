#Legends
# 'X' marks a HIT
# '&' marks my ships position
# '!' as placeholders
#'-' marks a MISSED

from random import randint

class TheBoards:
    """
    It will set the board size, insert ships, 
    """
    def __init__(self, size, num_of_ships, player_name, game_type):
        self.size = size
        self.num_of_ships = num_of_ships
        self.player_name = player_name
        self.game_type = game_type
        self.my_board = [['!' for x in range(size)] for y in range(size)]
        self.my_guesses = []
        self.my_ships = []


    def print(self):
        for x in self.my_board:
            print("   ".join(x))

    
    def guess_generator(self,x,y):
        """
        This function inserts 'X' inside the board on coordinates x and y. It creates a tuple containing x and y, and appends it to the my_guesses list.
        """
        self.my_guesses.append((x,y)) 
        if (x,y) in self.my_ships:
            self.my_board[x][y] = 'X'
            print("Hit")
            return "Hit"
        else:
            print("Missed")
            self.my_board[x][y] = '-'
            return "Missed"


    def ship_generator(self,x,y):
        """
        This function inserts '&' as a ship inside the board on coordinates x and y. It creates a tuple containing x and y and appends it to the my_ships list.
        """
        self.my_board[x][y] = '&'
        self.my_ships.append((x,y))    
        return


    def random_number(self,size):
        """
        This function generates a random number between 0 and size.
        """
        return randint(0,size)


def run_game():
    name = input("Please insert your name: \n")
    print(f"Hello {name}, Welcome to World War Battles!!")
    ndalo_board = TheBoards(8,5,'Ndalo','Ndalo')
    ndalo_board.ship_generator(ndalo_board.random_number(int(input("Insert size: "))),ndalo_board.random_number(int(input("Insert size: "))))

run_game()  
#TheBoards.print(TheBoards(8,5,'Hlompho','Hlompho'))
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




