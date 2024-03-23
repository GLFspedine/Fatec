n1 = float(input("Digite a primeira nota:" ))
n2 = float(input("Digite a segunda nota:" ))
m = (n1+n2)/2
if m > 10:
    print("Valores Errados insira valores de notas de 0 a 10")
elif 10 >= m >= 9:
    print("Média:", m, "Nota: A  APROVADO")
elif 8.9 >= m >= 7.5:
    print("Média:", m, "Nota: B  APROVADO")
elif 7.4 >= m >= 6:
    print("Média:", m, "Nota: C  APROVADO")
elif 5.9 >= m >= 4:
    print("Média:", m, "Nota: D  REPROVADO")
elif 3.9 >= m >= 0:
    print("Média:", m, "Nota: E  REPROVADO")
else:
    print("Valores Errados insira valores de notas de 0 a 10")