import math
from collections import defaultdict
with open('/Users/sudhamhebbar/Documents/AOC2024/Day8/input.txt', 'r') as files:
    lines = files.readlines()
grid = []
for line in lines:
    row = list(line.strip())
    grid.append(row)

n = len(grid)
m = len(grid[0])

nodes = defaultdict(list)
for i in range(n):
    for j in range(m):
        if(grid[i][j] != '.'):
            nodes[grid[i][j]].append((i, j))


def find_collinear_points_part1(x1, y1, x2, y2):
    # Calculate the slope components (direction vector)
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the distance between the two points
    distance = math.sqrt(dx**2 + dy**2)

    # Normalize the direction vector
    unit_dx = dx / distance
    unit_dy = dy / distance

    # Find the next point in the positive direction
    x3 = x2 + distance * unit_dx
    y3 = y2 + distance * unit_dy

    # Find the next point in the negative direction
    x0 = x1 - distance * unit_dx
    y0 = y1 - distance * unit_dy

    return (x0, y0), (x3, y3)

def find_collinear_points(x1, y1, x2, y2):
    # Calculate the slope components (direction vector)
    dx = x2 - x1
    dy = y2 - y1
    allpoints = []

    # Calculate the distance between the two points
    distance = math.sqrt(dx**2 + dy**2)

    if distance == 0:
        return allpoints  # Avoid division by zero if points are identical

    # Normalize the direction vector
    unit_dx = dx / distance
    unit_dy = dy / distance

    # Find the points in the positive direction
    x3, y3 = x2, y2
    while 0 <= x3 < n and 0 <= y3 < m:
        x3 += distance * unit_dx
        y3 += distance * unit_dy
        allpoints.append((int(x3), int(y3)))

    # Find the points in the negative direction
    x0, y0 = x1, y1
    while 0 <= x0 < n and 0 <= y0 < m:
        x0 -= distance * unit_dx
        y0 -= distance * unit_dy
        allpoints.append((int(x0), int(y0)))

    return allpoints

antinodes = set()
for key, points in nodes.items():
    p = len(points)
    for i in range(p):
        for j in range(i+1, p):
            x1, y1 = points[i]
            x2, y2 = points[j]
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))
            col_points = find_collinear_points(x1, y1, x2, y2)
            for new_x, new_y in col_points:
                if(0<=new_x<n and 0<=new_y<m):
                    antinodes.add((new_x, new_y))
print(len(antinodes))
