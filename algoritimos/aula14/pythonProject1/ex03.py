def multi(n):
    s = sum([int(i) for i in n])
    p = 1
    for i in n:
        p *= int(i)
    return s, p

s, p = multi('3011392413016')

print(f'Multiplicação: ', p)
print(f'Soma: ', s)
