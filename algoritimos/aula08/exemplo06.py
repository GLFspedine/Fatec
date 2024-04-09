nome = input("Digite seu nome completo: ")
nasc = input("Digite a data de nasc <DD/MM/AAAA>: ")
data = nasc.split("/")
palavra = nome.split()
pre_nome = palavra[0]
sobrenome = palavra[1]

print(f"ola {pre_nome}... muito bonito seu sobrenome; {sobrenome}")
print(f"Você nasceu no dia: {data[0]} e no mes: {data[1]}")