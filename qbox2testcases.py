from random import randint
for i in range(10):
    l = randint(500, 1000)
    w = randint(500, 1000)
    n = randint(2000, (l*w)//100)
    m = randint(0, n*3)
    print(l, w, n, m)
    with open(f'./test{i}.txt', 'w') as file:
        file.write(f'{l} {w}\n')
        file.write(f'{n} {m}\n')
        x, y = 2, 2
        for _ in range(n):
            x += 10
            if x > (l - 2):
                x = 2
                y += 10
            file.write(f'{x} {y}\n')


        for _ in range(m):
            x = randint(0, l-1)
            y = randint(0, w-1)
            file.write(f'{x} {y}\n')

