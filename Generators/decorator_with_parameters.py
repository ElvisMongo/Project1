import time
from math import ceil, log


def time_delay(pause):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(pause)
            print('Информационный объём строки - {} бит'.format(result))
            return result

        return wrapper
    return decorator

pause = int(input('Введите время задержки работы функции: '))
string = input('Введите строку: ')
alphabet = int(input('Введите размер алфавита: '))


# реализация работы формулы Хартли
@time_delay(pause)
def quantity_of_information():
    return ceil(len(string)*(log(alphabet, 2)))

quantity_of_information()


