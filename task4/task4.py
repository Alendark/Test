nums = []
for i in range(int(input())):  
    nums.append(int(input()))

m = sorted(nums)[len(nums) // 2]
print(sum(abs(v - m) for v in nums))
