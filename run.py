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
    my_board[x][y] = 'X'
    my_guesses.append((x,y))    
    return 

def ship_generator(x,y):
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