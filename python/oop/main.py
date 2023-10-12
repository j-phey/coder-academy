import dog

# dog1 = dog.create('Chipp', 15, 'Maltese')
# dog2 = dog.create('Puddles', 1, 'Akita')

# dog.walk(dog1)
# dog.walk(dog2)

dog1 = dog.Dog('Chipp', 15) # I want to create a new instance of this Dog class, via a method called Dog()
# dog1.name = 'Chippy' # this created the name attribute in dog

# A method is a function attached to a class
# An attribute is a variable attached to an object

dog2 = dog.Dog('Puddles', 2)

# use print(dir(dog1)) to see the methods in dog1
print(f'dog1: {dog1.__dict__}')  # __dict__ grabs the attributes
print(f'dog2: {dog2.__dict__}')
dog1.greet('Hi')
# print(dog2.greet())