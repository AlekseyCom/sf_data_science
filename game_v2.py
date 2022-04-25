"""The game 'Predict the number'. 
PC itself makes and guesses number
"""
import numpy as np

def random_predict(number:int=1)->int:
    """Guess number randomly

    Args:
        number (int, optional):The hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,500) # guessed number
        if number == predict_number:
            break # exit the loop if guessed right
    return (count)


def score_game(random_predict)->int:
    """For how many attempts out of 1000 approach does our algorithm guess

    Args:
        random_predict (_type_): guessing function
    Returns:
        : average number of attempts
    """
    count_ls = [] # list to save number of attempts
    np.random.seed(1) # fix the seed for reproducibility
    random_array = np.random.randint(1,101,size=(1000)) # made list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # calculate mean number of attempts
    print(f'Your algorithm guesses the number in an average of: {score} attepmts')    
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)
    
