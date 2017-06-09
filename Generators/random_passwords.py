import random
from string import ascii_letters, digits

m = int(input('Введите длину пароля: '))
k = int(input('Введите количество паролей: '))


def p_w_generator(m, k):
    v_v = list(ascii_letters + digits)
    for j in range(k):
        x = []
        while len(x) < m:
            a = random.choice(v_v)
            x.insert(0, a)
        x = ''.join(x)
        yield x

gen = p_w_generator(m, k)

for l in gen:
    print(l)
