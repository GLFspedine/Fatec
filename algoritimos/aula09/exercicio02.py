lista = []
for i in range(5):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)
m = max(lista)

print(f'Maior numero: {m}, Sua posição é: {lista.index(m)}')