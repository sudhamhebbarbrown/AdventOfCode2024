with open("Day25/input.txt") as file:
    lines = file.read()

locksandkeys = lines.split("\n\n")
locks = []
keys = []

for l in locksandkeys:
    tmp = l.split('\n')
    grid = [list(s) for s in tmp]
    if(grid[0][0] == '.'):
        keys.append(grid)
    else:
        locks.append(grid)

numlocks = []
numkeys = []
for lock in locks:
    trans = zip(*lock)
    heights = []
    for row in trans:
        heights.append(row.count('#')-1)
    numlocks.append(heights)

for key in keys:
    trans = zip(*key)
    heights = []
    for row in trans:
        heights.append(row.count('#')-1)
    numkeys.append(heights)

n = len(numkeys)
m = len(numlocks)

def isOverlap(lock, key):
    for i in range(5):
        if(lock[i] + key[i] >5):
            return 0
    return 1
res = 0
for lock in numlocks:
    for key in numkeys:
        res+= isOverlap(lock, key)
print(res)
