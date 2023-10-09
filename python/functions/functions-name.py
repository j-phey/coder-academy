# Defining functions
def hello(name, age):
    print(f'Hello, {name}, you are {age} years old!')

def goodbye():
    print('Goodbye!')

# Main
goodbye()
hello(age=32, name='Jon') # Use keywords as identifiers! They can be in any order 
hello(name=input('What is your name? '), age=input('How old are you? '))

