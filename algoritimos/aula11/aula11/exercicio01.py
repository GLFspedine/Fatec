l = []
for x in range(10):
    n = int(input(f"Ddigite o {x}° numeto: "))
    l.append(n)

t = tuple(l)
print(t[::-1])