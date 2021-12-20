with open('num.txt', 'r') as f:
    nums = f.read()

nums = nums.split()
n = [int(x) for x in nums]

m = sorted(n)[len(n) // 2]
print(sum(abs(v - m) for v in n))
