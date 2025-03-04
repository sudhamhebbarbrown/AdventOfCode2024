with open('/Users/sudhamhebbar/Documents/AOC2024/Day9/input.txt', 'r') as files:
    lines = files.readlines()

s = lines[0]
# s = s.strip()
# res = ''
# i = 0
# currId = 0
# n = len(s)
# while(i<n):
#     if(i%2 == 0):
#         toadd = [str(currId)]*int(s[i])
#         currId+=1
#         res += ''.join(toadd)
#     else:
#         toadd = ['.']*(int(s[i]))
#         res += ''.join(toadd)
#     i+=1

# i = 0
# j = len(res)-1

# res = list(res)
# while(i<j):
#     while(i<j and res[i] != '.'):
#         i+=1
#     while(i<j and res[j] not in '1234567890'):
#         j-=1
#     res[i], res[j] = res[j], res[i]
#     i+=1
#     j-=1
# currId = 0
# total = 0
# print(''.join(res))
# for i in res:
#     if(i=='.'):
#         break
#     total = total + (currId * int(i))
#     currId+=1
# print(total)
from math import floor
from itertools import repeat

# read input_data from file
with open("/Users/sudhamhebbar/Documents/AOC2024/Day9/input.txt", "r") as file:
  input_data = file.read()
disk_map = list(map(int, input_data.strip()))

# convert disk_map to memory list
memory = []
block = 0
for i in range(len(disk_map)):
  if i % 2 == 0:
    memory += list(repeat(int(block), disk_map[i]))
  else:
    memory += list(repeat('.', disk_map[i]))
  block += .5

num_idx = [i for i in range(len(memory) - 1, -1, -1) if memory[i] != '.']
for idx in num_idx:
  # if gap left of number, swap them
  gap = memory.index('.')
  if gap < idx:
    memory[idx], memory[gap] = memory[gap], memory[idx]

# calculate checksum
total = 0
for i in range(len(memory)):
  val = memory[i]
  if val != '.':
    total += i * val

print(total)