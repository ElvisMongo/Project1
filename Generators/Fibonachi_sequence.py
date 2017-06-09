# Последовательность Фибоначчи

n = int(input('Введите количество элементов последовательности: '))


def fibonachi(n):
    x = [0, 1]

    for i in range(0, n):
        if i == 0:
            yield x[i]

        if i == 1:
            yield x[i]

        if i >= 2:
            a = x[i - 2] + x[i - 1]
            x.insert(i, a)
            yield a

for i in fibonachi(n):
    print(i)


