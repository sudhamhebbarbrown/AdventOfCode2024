with open("/Users/sudhamhebbar/Documents/AOC2024/Day15/input.txt") as f:
    lines = f.readlines()

grid = []
for line in lines:
    grid.append(list(line.strip()))

def print_grid(grid):
    for row in grid:
        print("".join(row))

n = len(grid)
m = len(grid[0])
#move all the boxes to make space for the robot and boxes
def moveright(x, y):
    # Start from the robot's current position
    next_pos = y + 1
    
    # Loop to find the next available `.`
    while next_pos < m:
        if grid[x][next_pos] == '#':
            # If we encounter a wall, stop moving
            return False
        elif grid[x][next_pos] == 'O':
            # If we encounter a box, find the next available `.`
            next_next_pos = next_pos + 1
            while next_next_pos < m and grid[x][next_next_pos] != '.':
                if grid[x][next_next_pos] == '#':
                    # Stop moving if a wall is encountered
                    return False
                next_next_pos += 1
            if next_next_pos < m:
                # Move the box to the next `.`
                grid[x][next_pos] = '.'
                grid[x][next_next_pos] = 'O'
            else:
                # No available space for the box to move
                return False
        elif grid[x][next_pos] == '.':
            # If we encounter an empty space, move the robot
            grid[x][y] = '.'
            grid[x][next_pos] = '@'
            return True
        next_pos += 1

    return False

print_grid(grid)
print(moveright(2, 3))
print_grid(grid=grid)

