nota1 = float(input('Qual é a primeira nota? '))
nota2 = float(input('Qual é a segunda nota? '))
media = (nota1+nota2)/2
if media >= 5:
    print('Parabéns foi aprovado, sua nota é: ', media)
else:
    print('Você foi reprovado, sua nota é: ', media)