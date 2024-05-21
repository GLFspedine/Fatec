nomes = {}
for x in range(3):
    chave = input(f"Ddigite o {x}° Sobrenome: ")
    valor = input(f"Ddigite o {x}° Idade: ")
    nomes.update({chave:valor})

velho = max(nomes, key=nomes)