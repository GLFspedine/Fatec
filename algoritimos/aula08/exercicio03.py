frase = input("digite uma frase: ").lower()
a = frase.count("a")
e = frase.count("e")
i = frase.count("i")
o = frase.count("o")
u = frase.count("u")
vogais = a + e + i + o + u
print(f"Esse é o número de vogais na frase: {vogais}!")