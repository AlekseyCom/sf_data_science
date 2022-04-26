import numpy as nm
number = nm.random.randint(1,101)
count = 0
while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: '))
    if predict_number > number:
        print('The number must be less then. Try again.')
    elif predict_number < number:
        print('The number must be greater then. Try again.')
    else:
        print(f'You guessed the number. This number = {number} in {count} attempts')
        break
        
    