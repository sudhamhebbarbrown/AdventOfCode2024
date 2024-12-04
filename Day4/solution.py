with open('/Users/sudhamhebbar/Documents/AOC2024/Day4/input.txt', 'r') as files:
    lines = files.readlines()
matrix = []
for line in lines:
    matrix.append(list(line.strip()))

n = len(matrix)
m = len(matrix[0])
req = 'XMAS'
moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]
cross_moves = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
# def check_directions(i, j):
#     res = 0
#     for dx, dy in moves:
#         x = i
#         y = j
#         curr = ''
#         while(x>=0 and x<n and y>=0 and y<m):
#             curr += matrix[x][y]
#             x += dx
#             y += dy
#             if (curr == 'XMAS'):
#                 res += 1
#                 break
#     return res

def check_part2(i, j):
    for dx, dy in moves:
        x = i + dx
        y = j + dy
        if not (x>=0 and x<n and y>=0 and y<m):
            return 0
    leftcross = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
    rightcross = matrix[i-1][j+1] + matrix[i][j] + matrix[i+1][j-1]
    print(leftcross, rightcross)
    if (leftcross == 'MAS' or leftcross == 'SAM') and (rightcross == 'MAS' or rightcross == 'SAM'):
        return 1
    return 0
total = 0
for i in range(n):
    for j in range(m):
        if(matrix[i][j] == 'A'):
            total += check_part2(i, j)
print(total)