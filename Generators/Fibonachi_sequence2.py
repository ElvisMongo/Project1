# Последовательность Фибоначчи

n = int(input('Введите количество элементов последовательности: '))


def fibonachi(n):
    x = 1
    y = 1

    for i in range(n):
        if (i == 0) or (i == 1):
            a = x
        else:
            a = x + y
            x = y
            y = a
            yield a

for i in fibonachi(n):
    print(i)


