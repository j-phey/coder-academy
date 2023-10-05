# print('What is your name?')
my_name = input('What is your name? ') 
# myName is not the accepted convention (camel). Snake is preferred _

# print('How old are you?')
my_age = int(input('How old are you? '))

# print('Hello, ' + my_name + ', you are ' + str(my_age + 10) +' years old in 10 years')

print(f'Hello, {my_name}, you are {my_age +10} years old in 10 years')

# {} calls a function [interpolation]
# {} automatically casts things as a str
# f is needed for function to use {}

# spam = 'Hello, world!'
# spam[0] gets the first character, spam[1] gets the second character, spam[-1] gets the last characterspam 
# spam[0:5] gets the first 6 characters
# spam[:5] gets the first 5 characters
# [Hello in spam] would be true
# spam.upper() converts str to upper case
# spam.lower() converts str to lower case
# len(spam) gets the str length
