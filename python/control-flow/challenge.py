import math #likely need to import math due to using pi

shape = input('What shape? Square, Triangle or Circle?' )

if shape == 'Square':
    squareSides = input('How long is each side in cm?' )
    area = squareSides ^ 2

elif shape == 'Triangle':
    triangleHeight = input('What is the height in cm?' )
    triangleBase = input('What is the base in cm?')
    area = 0.5 * triangleHeight * triangleBase
    
# elif shape == 'Circle':

# else
#     print()