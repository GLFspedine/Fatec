#importar a Bibliotéca inteira:

import math

#importando a Bibliotéca seletiva: separar oque deseja entre virgulas.

from math import pow,sqrt

x1 = float(input("enter com x1: "))
y1 = float(input("enter com y1: "))
x2 = float(input("enter com x2: "))
y2 = float(input("enter com y2: "))

dx = x2-x1
dy = y2-y1
d = sqrt(pow(dx,2)+pow(dy,2))
print('Distância = ', d)

#sem importa a Bibliotéca

a1 = float(input("enter com a1: "))
b1 = float(input("enter com b1: "))
a2 = float(input("enter com a2: "))
b2 = float(input("enter com b2: "))

cx = a2-a1
cy = b2-b1
c = ((cx**2)+(cy**2))**0.5
print('Distância = ', c)