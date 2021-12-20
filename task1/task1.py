f1 = open('file_1.txt', 'r')
l1 = f1.read()
n = int(l1)

f2 = open('file_2.txt', 'r')
l2 = f2.read()
m = int(l2)

i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()
