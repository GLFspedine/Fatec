def eprimo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


x =  int(input("Digite um valor: "))
if eprimo(x):
    print("O valor digitado é primo!")
else:
    print("O valor digitado não é primo!")