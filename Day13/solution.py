import re
with open("/Users/sudhamhebbar/Documents/AOC2024/Day13/input.txt") as f:
    lines = f.readlines()

n = len(lines)
from math import gcd
from collections import deque
from math import gcd

def is_reachable(buttonA, buttonB, target):
    a_x, a_y = buttonA
    b_x, b_y = buttonB
    target_x, target_y = target

    # Compute GCDs
    gcd_x = gcd(a_x, b_x)
    gcd_y = gcd(a_y, b_y)

    # Check divisibility
    if target_x % gcd_x != 0 or target_y % gcd_y != 0:
        return False
    return True

def bfs(buttonA, buttonB, target):
    a_x, a_y = buttonA
    b_x, b_y = buttonB
    target_x, target_y = target

    # Check if the target is reachable using GCD
    
    queue = deque([(0, 0, 0, 0, 0)])  # (tokens, x, y, buttons)
    visited = set()

    while queue:
        tokens, x, y, button_a, button_b = queue.popleft()

        # Debugging print

        # Check if the target is reached
        if (x, y) == (target_x, target_y):
            return tokens

        # Check if the state is valid and hasn't been visited
        if ((x, y) in visited) or (button_a>=100) or (button_b>=100):
            continue
        visited.add((x, y))

        # Press B
        queue.append((tokens + 1, x + b_x, y + b_y, button_a, button_b+1))

        # Press A
        queue.append((tokens + 3, x + a_x, y + a_y, button_a+1, button_b))

    return 0

res = 0
for i in range(0, n, 4):
    first = lines[i]
    second = lines[i+1]
    third = lines[i+2]
    matches = re.findall(r'[XY]\+(\d+)', first)
    buttonA = (int(matches[0]), int(matches[1]))
    matches = re.findall(r'[XY]\+(\d+)', second)
    buttonB = (int(matches[0]), int(matches[1]))
    pattern = r"X=(\d+), Y=(\d+)"
    match = re.search(pattern, third)
    x, y = map(int, match.groups())
    print(is_reachable(buttonA, buttonB, (x, y)))
print(res)


    
