# f = open('shopping.txt') # We can also specify paths like '../spam/shopping.txt'

# data = f.read(15) # Reads first 15 chars
# data2 = f.read(10) # Reads first 10 chars

# data = f.readline() # Reads each line

# f.close()

# print(repr(data))

# print(repr(data2))

# READS THE FIRST LINE
# with open('shopping.txt') as asd: # Can use this to remove the need for open and closes
#     data = asd.readline()
#     print(repr(data))

# # PRINT EACH ITEM WITHOUT THE /n 
# with open('shopping.txt') as asd: 
#     for line in asd:
#         print(line.strip())

# TO CREATE A DICTIONARY:
# shopping_list = []
# with open('shopping.txt') as asd: 
#     for line in asd:
#         shopping_list.append(line.strip())

# print(shopping_list)

# WRITING A FILE
# shows = [
#     'The Devils Plan',
#     'Terrace House',
#     'Running Man',
#     'Transit Love'
# ]

# with open('tv-shows.txt', 'w') as f: # mode 'w' overwrites the file
#     # f.write('The X Files\n') # Creates a new file 
#     # f.write('The Witcher\n')
#     # f.write('\n'.join(shows))

#     # for s in shows:
#     #     f.write(f'{s}\n')

#     for i, s in enumerate(shows): # enumerate adds ordered list
#         f.write(f'{i + 1}. {s}\n')


item = input('What do you need to buy? ')
with open('shopping.txt', 'a') as f: # mode 'a' appends to the file
    f.write(f'\n{item}')