def sum(nums):
    total = 0
    for i in nums:
       total += i
    return total

print(sum([1,2,3,4]))

def product(nums):
    total = 1
    for i in nums:
        total = total * i
    return total

print(product([1,2,3]))