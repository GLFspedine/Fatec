n = int(input("digite um numero inteiro entre maior que zero e menor que 1000"))

if n <= 0 or n >= 1000:
    print("Não é um numero inteiro entre 1 e 1000 ")
else:
    cent = n // 100
