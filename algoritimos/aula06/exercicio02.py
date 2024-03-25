v = float(input('Digite o valor da compra R$: '))
if v <= 0:
    print('Valor incorrento!')
elif v <= 1000:
    c = v * 0.1
elif v <= 5000:
    c = v * 0.2
else:
    c = v * 0.3
des = v - c
print("Seu desconto foi de R$: ", c, 'e o valor de sua compra final é R$: ', des)