class NegativeNumberError(Exception): # Create my own error class with the subclass Exception
    pass

try: # Try to run this code. Try pairs with except
    n = int(input('Enter a numerator: '))
    d = int(input('Enter a denominator: '))

    if n < 1 or d < 1: # Checks for negative numbers
        raise NegativeNumberError()
    
    q = n / d # Exception raised when trying to divide by zero

    print(q)

except ZeroDivisionError:
    print('You cannot divide by zero')

except ValueError: 
    print('Inputs must be integers')

except NegativeNumberError:
    print('Must be a positive number')

except Exception as e: # Must be called 'Exception'
    print('Something went wrong')
    print(e) # Takes on 'Exception', where 'Exception' is the detail of the error
    # Prints 'e' to the debug log / error file for a traceback