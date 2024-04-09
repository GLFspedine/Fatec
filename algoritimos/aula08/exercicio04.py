frase = input(f"Digite uma frase:").lower()
palavra = input(f"Digite uma palavra dessa frase: ").lower()
npalavra = frase.count(palavra)

print(f"{palavra} aparce: {npalavra} vezes")
