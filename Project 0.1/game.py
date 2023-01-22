import numpy as np

def guess_number(number:int=1) -> int:
    """Функция поиска заданного числа

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: кол-во попыток, за которое компьютер угадал число
    """
    random_num = np.random.randint(1, 101)  # загадали число, которое удолжен угадать компьютер
    count = 0 # количество попыток
    upper_limit=101 #устанавливаем первоначальную верхню границу для отбора
    lower_limit=1 #устанавливаем первоначальную нижнюю границу для отбора   
    
    while True: #запишем поиск с помощью безконечного цикла 
        count+=1
        predict_number = np.random.randint(lower_limit, upper_limit) # предполагаемое число
        
        if random_num > predict_number:
            lower_limit=predict_number+1 #устанавливаем новую нижнюю границу генерации
            
        elif random_num < predict_number:
            upper_limit=predict_number #устанавливаем новую верхнюю границу генерации
            
        else:
            print(f'Число угадано за {count} попыток. Загаданное число - {random_num}') #печатаем полученный результат
            break
    return (count)


def score_game() -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(guess_number(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game()

        