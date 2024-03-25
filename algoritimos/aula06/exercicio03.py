l = float(input('Digite o valor da largura metros: '))
c = float(input('Digite o valor do compriento metros: '))
a1 = (l * 2.8) * 2
a2 = (c * 2.8) * 2
ap = 2.10 * 0.8
lt = (a1 + a2 - ap) / 3
t1 = 1
t2 = 3.7
t3 = 18
print("Serão necessarios: ", lt, "litros de tinta para pintar o aposento")
if (lt / 1) <= 1:
    print('comprar 1 lata de 1 litro')
elif (lt / 1) <= 3:
    c = int((lt / 1) + 1)
    print('comprar', c, 'lata de 1 litro')
elif (lt / 3.7) <= 1:
    print('comprar 1 lata de 3.7 litro')
elif (lt / 3.7) <= 4:
    c = int((lt / 3.7) + 1)
    print('comprar', c, 'lata de 3,7 litros')
elif (lt / 18) >= 1:
    c = int((lt / 18) + 1)
    print('comprar', c, 'lata de 18 litros')