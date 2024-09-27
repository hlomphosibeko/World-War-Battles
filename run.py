from random import randint

my_list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
my_list[0][4] = 'a'
#print(my_list)

my_list[0][4] = '*'
#print(my_list)

my_list[4][4] = 'X'
print(my_list)

my_guesses = [(0, 4), (4, 0)]
my_guesses.append((0, 0))
print(my_guesses)

def random_number(size):
    return randint(0, size - 1)
    



x = random_number(4)
print(x)