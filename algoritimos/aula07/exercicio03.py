soma_altura = 0
soma_peso = 0
maior_imc = 0
menor_imc = 100
for i in range(1,6):
        peso = float(input('Digite um peso em Kg: '))
        altura = float(input('Digite uma altura em metros: '))
        imc = peso / (altura ** 2)
        soma_altura = soma_altura + altura
        soma_peso = soma_peso + peso
        if imc > maior_imc:
            maior_imc = imc
        if imc < menor_imc:
            menor_imc = imc
media_altura = soma_altura / 5
media_peso = soma_peso / 5
print(f'O peso medio é: {media_peso:5.3f} A média de altura é: {media_altura:5.3f}')
print(f'O maior IMC é: {maior_imc:5.3f} O menor IMC é: {menor_imc:5.3f}')