n = int(input("Digite um numero: "))
e = 0
for i in range(1,n+1):
    e = (2 ** i) + e
print(f'O valor final de E é: {e:5.2f}')

N = int(input("Digite um numero: "))
V = 0
E = 0
while V != n:
    V = V + 1
    E = (2 ** V) + E
print(f'O valor final de E é: {E:5.2f}')