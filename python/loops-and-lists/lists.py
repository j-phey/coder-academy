spam = ['cat', 'dog', 'bird']
eggs = [12, 78, 100, 54, 42]
foo = ['Jon', 32, '175']
tic_tac_toe = [
    ['', 'O', ''],
    ['X', 'O', ''],
    ['', 'X', '']
    ]

# index = 1

# for abcd in spam: # abcd could be anything
#     print(f'{index}. {abcd}')
#     index += 1

# ---- ENUMERATING

# # index = 1

# for index, animal in enumerate(spam): # enumerate takes care of pairings the index with the value
#     print(f'{index + 1}. {animal}')
# #     index += 1

# ----- APPENDING 

# spam.append('kangaroo') # adds 'kangaroo' to the list

# spam.extend(foo) # appends the elements of another list

# x = 'dog' in spam # use 'in' to determine if something is in a list
# print(x)

def display_person(person):
    # name = person[0]
    # age = person[1]
    # height = person[2]
    name, age, height = person
    print(f'{name} is {age} years old and {height}cm tall')

# display_person(foo)

spam.insert(1, 'kangaroo') # inserts a value at the index
# x = spam.pop() # removes and returns item in index (default last)
spam.sort() # sorts in ascending order. spam.sort(reverse=True) is descending 
print(spam)