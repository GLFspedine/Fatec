palavra = input(f"Digite uma palavra: ").upper()

if palavra == (palavra[::-1]):
    print("é um Palindromo")
else:
    print("não é um Palindromo")