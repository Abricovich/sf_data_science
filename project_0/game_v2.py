'''Игра угадай число
Компьютер сам загадывает число и сам его угадывает
'''

import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    max_number = 101
    min_number = 0
    
    while True:
        count+=1
        predict = round((max_number + min_number) / 2)  # предполагаемое число
        
        
        if predict > number:
            max_number = predict
        elif predict < number:
            min_number = predict
        else:
            predict == number
            break  # выход из цикла если угадали
    return count 

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает функция

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score


score_game(random_predict)
    
 
    
    
    
    
    
    
    