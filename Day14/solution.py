# import collections
# import re
# import matplotlib.pyplot as plt

# pattern = r"(-?\d+),(-?\d+)"

# # Read input file
# with open("/Users/sudhamhebbar/Documents/AOC2024/Day14/input.txt") as f:
#     lines = f.readlines()

# size_n = 101
# size_m = 103

# def resolve_quadrant(x, y):
#     mid_x = size_n // 2
#     mid_y = size_m // 2
#     if x < mid_x and y < mid_y:
#         return 1
#     if x > mid_x and y > mid_y:
#         return 4
#     if x < mid_x and y > mid_y:
#         return 2
#     if x > mid_x and y < mid_y:
#         return 3
#     else:
#         return 0

# def simulate(x, y, move):
#     curr = 0
#     move_x = move[0]
#     move_y = move[1]
#     x = (x + move_x) % size_n
#     y = (y + move_y) % size_m
#     curr += 1
#     return (x, y)

# # Initialize the grid
# grid = [[0 for _ in range(size_m)] for _ in range(size_n)]
# robots = []

# # Parse input and initialize robots
# for line in lines:
#     matches = re.findall(pattern, line)
#     pos, vel = [(int(x), int(y)) for x, y in matches]
#     x, y = pos
#     grid[x][y] = 1
#     robots.append((pos, vel))
# def graphplot(grid, curr):
# # Render the grid using matplotlib
#     plt.figure(figsize=(10, 10))
#     plt.imshow(grid, cmap="binary", interpolation="none")  # 'binary' for black & white grid
#     plt.title(f"Robot Positions in Grid{curr}")
#     plt.xlabel("Columns")
#     plt.ylabel("Rows")
#     plt.colorbar(label="Occupied (1) or Empty (0)")
#     plt.show()
# # Simulate movement
# for i in range(100):
#     new_robots = []
#     for pos, val in robots:
#         x, y = pos
#         new_pos = simulate(x, y, val)
#         new_robots.append((new_pos, val))
#         grid[x][y] = 0
#         x, y = new_pos
#         grid[x][y] = 1
#     robots = new_robots
#     graphplot(grid, i)

from functools import reduce
from itertools import count, takewhile
from operator import mul
from pathlib import Path

input_text = Path('/Users/sudhamhebbar/Documents/AOC2024/Day14/input.txt').read_text('utf-8').splitlines()
input_data = [[tuple(map(int, eq.split('=')[1].split(','))) for eq in line.split()] for line in input_text]

height = 103
width = 101

def forward(time: int):
    return [((p[0] + v[0] * time) % width, (p[1] + v[1] * time) % height) for p, v in input_data]

def part_1() -> int:
    u = width // 2
    v = height // 2
    quadrants = [0, 0, 0, 0]
    for x, y in forward(100):
        for i, c in enumerate([x < u and y < v, x > u and y < v, x < u and y > v, x > u and y > v]):
            quadrants[i] += c

    return reduce(mul, quadrants)

def part_2() -> int:
    return len(list(takewhile(lambda t: len(input_data) != len(set(forward(t))), count())))

print("Part 1:", part_1())
print("Part 2:", part_2())