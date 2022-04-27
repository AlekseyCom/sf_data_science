# Import a library for generating random numbers.
import numpy as np

# The guessing function
def random_predict(number:int=1)->int:
    """We predict the number by limiting the scope of choice

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: Number of attemps
    """
    count = 0 
    
    min, max = 1, 100
    predict_number = max / 2
    
    while number != predict_number:
        count+=1
        # limiting the scope of choice
        if number > predict_number: 
            min = predict_number + 1.5
        
        elif number < predict_number: 
            max = predict_number - 1.5
        
        predict_number = round((max + min ) / 2) # splitting the new scope of choice in half   
    
    return(count)


''' The function is necessary to determine for how many attempts
the program guesses our number.
'''
def score_game(random_predict) -> int:
    """For how many attempts out of 1000 approach does our algorithm predict

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = [] # list to save number of attempts
    np.random.seed(1) # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(10000)) # made list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # calculate mean number of attempts
    print(f"Your algorithm guesses the number in an average of: {score} attepmts")

score_game(random_predict) 

