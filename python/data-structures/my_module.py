something = 'Hello there!'
a_list = [10, 20, 30, 40, 50, 60, 70]
person = {'name':'John', 'age':21}

def foo(person):
    print(f"{person.get('name')} is {person.get('age')} years old")