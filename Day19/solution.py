from functools import cache
with open('/Users/sudhamhebbar/Documents/AOC2024/Day19/dictionary.txt') as file:
    lines = file.readlines()

dictionary = set()
for line in lines:
    li = line.replace(' ', '').strip().split(',')
    for d in li:
        dictionary.add(d)

with open('/Users/sudhamhebbar/Documents/AOC2024/Day19/input.txt') as file:
    lines = file.readlines()

@cache
def dfs(s, i):
    if(i == len(s)):
        return 1
    if(i>len(s)):
        return 0
    res = 0
    for d in dictionary:
        n = len(d)
        if(s[i:i+n] == d):
            res += dfs(s, i+n)
    return res
res = 0
for line in lines:
    res+= dfs(line.strip(), 0)

print(res)