n1 = 0
n2 = 1
n3 = 0
soma = 0
for i in range(1,50):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        soma = soma + n3
print(f'soma total é: {soma} ')