from collections import Counter
with open('/Users/sudhamhebbar/Documents/AOC2024/Day1/input.txt', 'r') as files:
    lines = files.readlines()
first = []
second = []
for line in lines:
    tmp = line.split("   ")
    first.append(int(tmp[0]))
    second.append(int(tmp[1].strip()))
print(first)
print(second)

#PART 1
# first.sort()
# second.sort()
# n = len(first)
# res = 0
# for i in range(n):
#     res += abs(int(first[i]) - int(second[i]))
# print(res)

#PART 2
count = Counter()

for i in second:
    count[i]+=1
res = 0
for j in first:
    res+= j*count[j]
print(res)