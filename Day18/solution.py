from collections import deque
with open("/Users/sudhamhebbar/Documents/AOC2024/Day18/input.txt") as f:
    lines = f.readlines()
SIZE = 71
grid = [['.']*SIZE for _ in range(SIZE)]
n = 0
for line in lines:
    
    a, b = line.strip().split(',')
    grid[int(b)][int(a)] = '#'
    n+=1
def print_grid(grid):
    for row in grid:
        print("".join(row))

def part1(grid):
    visited = set()
    queue = deque([(0, 0, 0)])  # (cost, x, y)
    target = (SIZE - 1, SIZE - 1)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Check start and target validity
    if grid[0][0] == '#' or grid[SIZE - 1][SIZE - 1] == '#':
        return -1  # No path if start or target is blocked

    while queue:
        cost, x, y = queue.popleft()
        if (x, y) == target:
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in moves:
            i, j = x + dx, y + dy
            if 0 <= i < SIZE and 0 <= j < SIZE and (i, j) not in visited and grid[i][j] != '#':
                queue.append((cost + 1, i, j))
    return -1
# print(part1(grid=grid))
