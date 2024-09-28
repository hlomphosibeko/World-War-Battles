#Legends
# 'X' marks a HIT
# '&' marks my ships position
# '!' as placeholders
#'-' marks a MISSED

from random import randint

my_board = [['!','!','!','!','!'],['!','!','!','!','!'],['!','!','!','!','!'],['!','!','!','!','!'],['!','!','!','!','!']]
#my_list[0][4] = 'a'
#print(my_list)

#my_list[0][4] = '*'
#print(my_list)

#my_list[4][4] = 'X'
#print(my_list)

my_guesses = []
my_ships = []
#my_guesses.append((0, 0))

def create_board(z):
    """
    This function generates the board z number of rows and z number of columns.
    """
    [['!' for x in range(z)] for y in range(z)]
    return 


def guess_generator(x,y):
    """
    This function inserts 'X' inside the board on coordinates x and y. It creates a tuple containing x and y, and appends it to the my_guesses list.
    """
    my_guesses.append((x,y)) 
    if (x,y) in my_ships:
        my_board[x][y] = 'X'
        print("Hit")
        return "Hit"
    else:
        print("Missed")
        my_board[x][y] = '-'
        return "Missed"
    

def ship_generator(x,y):
    """
    This function inserts '&' as a ship inside the board on coordinates x and y. It creates a tuple containing x and y and appends it to the my_ships list.
    """
    my_board[x][y] = '&'
    my_ships.append((x,y))    
    return

def random_number(size):
    """
    This function generates a random number between 0 and size.
    """
    return randint(0,size)
    


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
print(create_board(3))
