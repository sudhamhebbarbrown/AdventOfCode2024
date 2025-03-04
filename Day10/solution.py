from collections import deque
with open('/Users/sudhamhebbar/Documents/AOC2024/Day10/input.txt', 'r') as files:
    lines = files.readlines()
grid = []
seed = []
for line in lines:
    row = [int (num) for num in line.strip()]
    grid.append(row)

n = len(grid)
m = len(grid[0])
for i in range(n):
    for j in range(m):
        if(grid[i][j] == 0):
            seed.append((i, j))
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(i, j):
    queue = deque([(i, j, 0)])
    visited = set()
    res = set()
    while(queue):
        i, j, curr = queue.pop()
        if(curr == 9):
            res.add((i, j))
            continue
        visited.add((i, j))
        for dx, dy in moves:
            x = dx + i
            y = dy + j
            if(0<=x<n and 0<=y<m and grid[x][y] == curr + 1 and (x, y) not in visited):
                queue.append((x, y, curr + 1))
    return len(res)

def dfs(i, j, visited):
    if(grid[i][j] == 9):
        return 1
    visited.add((i, j))
    res = 0
    for dx, dy in moves:
        x = dx + i
        y = dy + j
        if(0<=x<n and 0<=y<m and grid[x][y] == grid[i][j] + 1 and (x, y) not in visited):
            res += dfs(x, y, visited)
    visited.remove((i, j))
    return res
total = 0
for x, y in seed:
    total += dfs(x, y, set())
print(total)




