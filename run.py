#Legends
# 'X' marks player guesses
# '&' marks my ships position
# '!' as placeholders

from random import randint

my_board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#my_list[0][4] = 'a'
#print(my_list)

#my_list[0][4] = '*'
#print(my_list)

#my_list[4][4] = 'X'
#print(my_list)

my_guesses = []
my_ships = []
#my_guesses.append((0, 0))


def guess_generator(x,y):
    """
    This function inserts 'X' inside the board on coordinates x and y. It creates a tuple containing x and y, and appends it to the my_guesses list.
    """
    my_board[x][y] = 'X'
    my_guesses.append((x,y))    
    return 

def ship_generator(x,y):
    """
    This function inserts '&' as a ship inside the board on coordinates x and y. It creates a tuple containing x and y and appends it to the my_ships list.
    """
    my_board[x][y] = '&'
    my_ships.append((x,y))    
    return

def random_number(size):
    return randint(0,size)
    





x = random_number(4)
print(x)

guess_generator(1,4)
guess_generator(2,1)
print(my_board)
print(my_guesses)

ship_generator(0,2)
ship_generator(3,0)
print(my_board)
print(my_ships)