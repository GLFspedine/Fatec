lista = []
for i in range(6000):
    from random import randint
    a = randint(1, 6)
    lista.append(a)

print(f'Resultado 1: {lista.count(1)}, Frequencia: {(lista.count(1)/6000)*100:6.2f}%')
print(f'Resultado 2: {lista.count(2)}, Frequencia: {(lista.count(2)/6000)*100:6.2f}%')
print(f'Resultado 3: {lista.count(3)}, Frequencia: {(lista.count(3)/6000)*100:6.2f}%')
print(f'Resultado 4: {lista.count(4)}, Frequencia: {(lista.count(4)/6000)*100:6.2f}%')
print(f'Resultado 5: {lista.count(5)}, Frequencia: {(lista.count(5)/6000)*100:6.2f}%')
print(f'Resultado 6: {lista.count(6)}, Frequencia: {(lista.count(6)/6000)*100:6.2f}%')
