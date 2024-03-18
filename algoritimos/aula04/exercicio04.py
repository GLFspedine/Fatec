s = float(input("Digite seu salario: "))
a = float(input('digite o valor de aumento em %:'))
ns = s*((a/100)+1)
na = ns-s
print('Novo salario: ', ns)
print('Valor do aumento: ', na)

s = float(input("Digite seu salario: "))
a = float(input('digite o valor de aumento em %:'))
ns = s*((a/100)+1)
na = ns-s
print(f'Novo salario:R$  {ns:8.2f}')
print(f'Valor do aumento: R$  {na:8.2f}')
print(f'--------------------')