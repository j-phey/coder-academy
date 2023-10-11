from my_module import foo as bar, person, something # if there's a naming conflict, you can use 'as'
import my_module # this now imports the whole module, instead of just specific variables

# print(dir(my_module)) # gives the directory of the module. Here we can see random imported from the module

def foo(x):
    print(x)

foo(person)
bar({'name':'Jon', 'age':'51'})

