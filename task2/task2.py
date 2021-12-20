f1 = open('num1.txt', 'r')
r1 = f1.read()
xo = float(r1)

f2 = open('num2.txt', 'r')
r2 = f2.read()
yo = float(r2)

f3 = open('num3.txt', 'r')
r3 = f3.read()
r = float(r3)

f4 = open('num4.txt', 'r')
r4 = f4.read()
y = float(r4)

f5 = open('num5.txt', 'r')
r5 = f5.read()
x = float(r5)

if (x - xo) * (x - xo) + (y - yo) * (y - yo) < r * r:
    print("Точка принадлежит окружности")
elif (x - xo) * (x - xo) + (y - yo) * (y - yo) > r * r:
    print("Точка не принадлежит окружности")
else:
    print("Точка на окружности")
    
