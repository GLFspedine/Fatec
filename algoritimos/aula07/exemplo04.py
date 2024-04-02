frase = input('Digite uma frase: ')
qa = 0
for i in frase:
    if i in "AEIOUaeiouãíóúàáéü":
        qa = qa + 1
    else:
        qa = qa + 0
print(f'A quantiade de "a" que aparecem na frase é: {qa}')
