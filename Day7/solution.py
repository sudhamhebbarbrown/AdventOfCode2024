from functools import cache
with open('/Users/sudhamhebbar/Documents/AOC2024/Day7/input.txt', 'r') as files:
    lines = files.readlines()
req = []
for line in lines:
    a, b = line.strip().split(":")
    b = b.strip().split(" ")
    req.append((a, b))

def dfs(i, curr):
    # print(curr)
    if(i>=n):
        if(curr == target):
            return True
        else:
            return False
    mul, add = False, False
    conc = False
    if(i == 0):
        mul = dfs(i+1, nums[i])
        add = dfs(i+1, nums[i])
    else:
        mul = dfs(i+1, curr * nums[i])
        add = dfs(i+1, curr + nums[i])
        conc = dfs(i+1, int(str(curr) + str(nums[i])))
    return mul | add | conc
res = 0
for a, b in req:
    target = int(a)
    nums = [int(num) for num in b]
    n = len(nums)
    can_make = dfs(0, 0)
    if(can_make):

        res+=target
print(res)