l = float(input('Digite o valor da largura metros: '))
c = float(input('Digite o valor do compriento metros: '))
a1 = (l * 2.8) * 2
a2 = (c * 2.8) * 2
ap = 2.10 * 0.8
lt = (a1 + a2 - ap) / 3
print("Serão necessarios: ", lt, "litros de tinta para pintar o aposento")