n1 = float(input(f'Digite o primeiro numero: '))
n2 = float(input(f'Digite o segundo numero: '))
n3 = float(input(f'Digite o terceiro numero: '))
a = 0
if (n1 == n2) or (n1 == n3) or (n2 == n3):
    print('Atribuiu valores iguais para duas entradas, favor começar novamente!')
    if (n1 > n2) and (n1 > n3):
        print(n1)
        a = n1
        if (a == n1) and (n2 > n3):
            print(n2)
            print(n3)
        elif (a == n1) and (n3 > n2):
            print(n3)
            print(n2)
    elif (n2 > n1) and (n2 > n3):
        print(n2)
        a = n2
        if (a == n2) and (n1 > n3):
            print(n1)
            print(n3)
        elif (a == n2) and (n3 > n1):
            print(n3)
            print(n1)
    elif (n3 > n1) and (n3 > n2):
        print(n3)
        a = n3
        if (a == n3) and (n1 > n2):
            print(n1)
            print(n2)
        elif (a == n3) and (n2 > n1):
            print(n2)
            print(n1)
