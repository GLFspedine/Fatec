frase = input(f"Digite uma palavra: ").upper()
frase1 = frase.strip()
palavras = frase1.split()
frase2 = ' '
for palavra in palavras:
    frase2 = frase2 + palavra
frase3 = frase2[::-1]
if frase3 == frase2:
    palindromo = True

else:
    palindromo = False

if palindromo:
    print("é um Palindromo")
else:
    print("não é um Palindromo")