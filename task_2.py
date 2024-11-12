import math 

nums = []

for i in range(0, 10):
    nums.append(i+1)

def calculate_sum(nums):
    total = 0
    for items in nums:
        total += items
    return total    

result = calculate_sum(nums)

print(result)