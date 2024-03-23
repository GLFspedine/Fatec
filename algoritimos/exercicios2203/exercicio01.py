vh = float(input("Qual o valor da sua hora trabalhada?" ))
th = float(input("Quantas horas você trabalhou?"))
sb = vh*th
ir = sb * 0.05
inss = sb * 0.10
fgts = sb * 0.11
sin = sb * 0.03
if sb <= 900:
    ir = 0
    des = ir + inss
    sl = sb - des
    al = 0
    print("Salário Bruto:", th, "*", vh, ":R$", sb)
    print('(-) IR', '(',al,'%)',         ":R$", ir)
    print('(-) INSS (10%)',              ":R$", inss)
    print('(-) FGTS (11%)',              ":R$", fgts)
    print("Total de descontos",          ":R$", des)
    print("Salário liquido",             ":R$", sl)
elif sb <= 1500:
    ir = sb * 0.05
    des = ir + inss
    sl = sb - des
    al = 5
    print("Salário Bruto:", th, "*", vh, ":R$", sb)
    print('(-) IR', '(',al,'%)',         ":R$", ir)
    print('(-) INSS (10%)',              ":R$", inss)
    print('(-) FGTS (11%)',              ":R$", fgts)
    print("Total de descontos",          ":R$", des)
    print("Salário liquido",             ":R$", sl)
elif sb <= 2500:
    ir = sb * 0.1
    des = ir + inss
    sl = sb - des
    al = 10
    print("Salário Bruto:", th, "*", vh, ":R$", sb)
    print('(-) IR', '(',al,'%)',         ":R$", ir)
    print('(-) INSS (10%)',              ":R$", inss)
    print('(-) FGTS (11%)',              ":R$", fgts)
    print("Total de descontos",          ":R$", des)
    print("Salário liquido",             ":R$", sl)
else:
    ir = sb * 0.2
    des = ir + inss
    sl = sb - des
    al = 20
    print("Salário Bruto:", th, "*", vh, ":R$", sb)
    print('(-) IR', '(',AL,'%)',         ":R$", ir)
    print('(-) INSS (10%)',              ":R$", inss)
    print('(-) FGTS (11%)',              ":R$", fgts)
    print("Total de descontos",          ":R$", des)
    print("Salário liquido",             ":R$", sl)

