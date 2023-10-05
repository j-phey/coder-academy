# COMPARING X AND Y

# x  = int(input('What is X? '))
# y = int(input('What is Y? '))

# if x < y:
#     print("X is less than Y")
# # indenting is important in Python!

# elif x > y: # elif = else if, can have as many elifs
#     print("X is greater than Y")

# else: # can only have one else, and it has to be at the end
#     print("X is equal to Y")


# COMPARING ASSIGNMENT SCORES
# score = int(input('Score: '))

# if score >= 90:
#     print('HD')

# elif score >= 80:
#     # technically we can also write and score > 90:
#     print('D')

# elif score >= 70:
#     print('CR')

# elif score >= 50:
#     print('P')

# else:
#     print('F')


# COMPARING names

name = input('What is your name? ')

# if name == 'Harry' or 'Ron' or 'Hermoine':
#     print('Gryffindor')
# # elif name == 'Ron':
# #     print('Gryffindor')
# # elif name == 'Hermoine':
# #     print('Gryffindor')
# elif name == 'Draco':
#     print('Slytherin')
# else:
#     print('You Mudblood!')

# match name:
#     case 'Harry':
#         print('Gryffindor')
#     case 'Ron':
#         print('Gryffindor')
#     case 'Hermoine':
#         print('Gryffindor')
#     case 'Draco':
#         print('Slytherin')
#     case _:
#         print('Mudblood...')

match name:
    case 'Harry' | 'Ron' | 'Hermoine':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Mudblood...')
