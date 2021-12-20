f1 = open('file_1.txt', 'r')
k1 = f1.read()
cor = k1.split()
kr = [float(x) for x in cor]

f2 = open('file_2.txt', 'r')
k2 = f2.read()
cer = k2.split()
kt = [float(x) for x in cer]

import math

num = 0

while num < len(kt):
    x = kt[num]
    y = kt[num + 1]
    hyp = math.sqrt((x - kr[0])**2 + (y - kr[1])**2)

    if hyp < kr[2]:
        print("1")
    elif hyp == kr[2]:
        print("0")
    else:
        print("2")
    num+=2
