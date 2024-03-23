from math import sqrt
a = float(input("Digite um Valor para a: "))
b = float(input("Digite um Valor para b: "))
c = float(input("Digite um Valor para c: "))
delta =(b**2)-(4*a*c)
x1 = (-b + (delta)**0.5)/(2*a)
x2 = (-b - (delta)**0.5)/(2*a)
if a == 0:
    print("Não é uma equação de segundo grau")
elif delta < 0:
    print("A equação não possui raizes reais")
elif delta == 0:
    if x1 > 0:
        print("A equação possui só uma raiz real: ",x1 )
    else:
        print("A equação possui só uma raiz real: ", x2)
elif delta > 0:
    print("A equação possui duas raizes reais:", 'x1: ',x1,'x2: ',x2)