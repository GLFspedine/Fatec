a = 80000
b = 200000
t = 0
while (a <= b):
    a = a*1.03
    b = b*1.015
    t = t + 1
print(f'Valor de anos necessarios para que a população de A ultrapasse A população de B: ', t)