# LOOPS - WHILE

# spam = 0

# while spam < 5: # like if, but keeps going whilst True
#     print('Hello!')
#     spam += 1 # spam = spam + 1, iterates each round

# print('Done')

# ----------------------------------------------------------

# LOOPS - FOR IN

# For loops initialises the variable (i.e. spam = 0)
# It initialises it to the first number of the range (i.e. 0)
# Then it takes on the next number in the range
# It stops when there's no more values in the range()

# for spam in range(5): # range generates a range of values from 0 to x (not inclusive). Can also do range(2,5)
#     print(f'Hello {spam}')

# ----------------------------------------------------------

# LOOPS - RANGE WITH RANDOM LIBRARY

import random

count = int(input('How many random integers?'))
for i in range(count): # Could also write 'for spam'
    print(random.randint(1,100))