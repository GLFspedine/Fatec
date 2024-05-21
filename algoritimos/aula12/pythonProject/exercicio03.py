def segundos(h, m, s):
    hs = h * 3600
    ms = m * 60
    return (hs + ms + s)

#...

horas = int(input("Digite um valor para Horas: "))
minutos = int(input("Digite um valor para Minutos: "))
seg = int(input("Digite um valor para Segundos: "))

print(f"Valor total em segundos: {segundos(horas, minutos, seg)}")