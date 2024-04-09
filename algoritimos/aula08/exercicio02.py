nasc = input("Digite a data de nasc <dd/mm/aaaa>: ")
data = nasc.split("/")

print(f"{data[2]}/{data[1]}/{data[0]}")