# my_dog = {'name':'Chipp', 'age':15, 'breed': 'Maltese'}

# CREATING A NEW CLASS CALLED DOG

class Dog: # A class defines the structure of a data type and its methods
    def __init__(self, name, age): # always have to use self. init method initialises
        self.name = name # creates a new attribute called self.name and a paramater called name
        self.age = age
    
    def greet(self, prefix): # greet method
        # print(f'spam: {spam}')
        print(f'{prefix}, {self.name}!') # name is an attribute of the object. prefix is not an attribute so it doesn't need self - it's a parameter


# attribute = variable attached to an object (i.e. a container). Object is Dog