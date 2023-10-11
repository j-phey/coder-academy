my_dog = {'name':'Chipp', 'age':15, 'breed': 'Maltese'}

my_dog['age'] = 16

# dogs = [
#     {'name':'Chipp', 'age':15, 'breed': 'Maltese'},
#     {'name':'Pudding', 'age':1, 'breed': 'Akita'}
# ]

my_dog['owner'] = 'Jon'

# for k, v in my_dog.items():
#     print(f'The value of "{k}" is {v}')

print (my_dog.values()) # prints the values in the dict

# print(my_dog.items()) # prints the items inside the my_dog dictionary

print(my_dog.get('state', 'Unknown'))