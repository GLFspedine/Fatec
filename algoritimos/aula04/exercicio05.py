d = float(input("Digite seu depósito: "))
a = float(input('Digite o valor da taxa em %:'))
t = float(input('Digite o tempo em messes:'))
m = d*((a/100)+1)**t
r = m-d
print('Valor do rendimento: ', r)
print('Montante final: ', m)