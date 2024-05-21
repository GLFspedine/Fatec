c = float(input(f'Digite o numero de cabeças: '))
p = (c * 3) + 3

print(f'Numero total de cabeças: ', c)
print(f'Numero total de pés: ', p)

coelhos = float((p - 2*c)/2)
patos = float(c - coelhos)

print(f'Total de Patos: ', patos)
print(f'Total de Coelhos: ', coelhos)
