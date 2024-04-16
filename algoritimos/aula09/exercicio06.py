lista = []
lista1 = []
lista2 = []
for i in range(30000):
    from random import randint
    a = randint(1, 6)
    lista1.append(a)
    from random import randint
    b = randint(1, 6)
    lista2.append(b)
    c = a + b
    lista.append(c)

print(f'Resultado 2: {lista.count(2)}, Frequencia: {(lista.count(2)/30000)*100:6.2f}%')
print(f'Resultado 3: {lista.count(3)}, Frequencia: {(lista.count(3)/30000)*100:6.2f}%')
print(f'Resultado 4: {lista.count(4)}, Frequencia: {(lista.count(4)/30000)*100:6.2f}%')
print(f'Resultado 5: {lista.count(5)}, Frequencia: {(lista.count(5)/30000)*100:6.2f}%')
print(f'Resultado 6: {lista.count(6)}, Frequencia: {(lista.count(6)/30000)*100:6.2f}%')
print(f'Resultado 7: {lista.count(7)}, Frequencia: {(lista.count(7)/30000)*100:6.2f}%')
print(f'Resultado 8: {lista.count(8)}, Frequencia: {(lista.count(8)/30000)*100:6.2f}%')
print(f'Resultado 9: {lista.count(9)}, Frequencia: {(lista.count(9)/30000)*100:6.2f}%')
print(f'Resultado 10: {lista.count(10)}, Frequencia: {(lista.count(10)/30000)*100:6.2f}%')
print(f'Resultado 11: {lista.count(11)}, Frequencia: {(lista.count(11)/30000)*100:6.2f}%')
print(f'Resultado 12: {lista.count(12)}, Frequencia: {(lista.count(12)/30000)*100:6.2f}%')
