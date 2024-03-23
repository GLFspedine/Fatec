a = float(input("digite o tamanho do lado a: "))
b = float(input("digite o tamanho do lado b: "))
c = float(input("digite o tamanho do lado c: "))
if ((a+b)<c) or ((b+c)<a) or ((a+c)<b):
    print('Não é um triângulo!')
else:
    if (a == b and a == c):
        print('Triângulo Equilatero')
    else:
        if (a == b or a == c):
            print('Triângulo Isósceles')
        else:
            print('Triângulo Escaleno')