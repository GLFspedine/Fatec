def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if not (n%i):
            return False
    return True
def primos_lista(n):
    res = []
    i = 0
    c = 0
    while c < n:
        if primo(i):
            res.append(i)
            c+=1
        i += 1
    return len(res), res

Y = 16
N = Y*2+5
t, l = primos_lista(N)

print(f'Lista dos {N} primeiros numeros primos é: {l}')
print(f'soma dos numeros primos: {sum(l)}.')