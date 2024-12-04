# matrix = []
# with open('/Users/sudhamhebbar/Documents/AOC2024/Day2/input.txt', 'r') as files:
#     lines = files.readlines()
# for line in lines:
#     row = [int(num) for num in line.split()]
#     matrix.append(row)

# # Part 1
# def check_row(row, direction, lowerlimit=1, upperlimit=3):
#     count = 0
#     prev = row[0]
#     for num in row[1:]:
#         diff = num - prev if direction == "increasing" else prev - num
#         if not (lowerlimit <= diff <= upperlimit):
#             count += 1
#             if count > 1:
#                 return False
#         else:
#             prev = num
#     return True

# res = 0
# for row in matrix:
#     if check_row(row, "increasing") or check_row(row, "decreasing"):
#         res += 1

# print(res)

def aoc02():
    ok = lambda r: sorted(r) in [r,r[::-1]] and all(1<=abs(i-j)<=3 for i,j in zip(r,r[1:]))
    ok2 = lambda r: any(ok(r[:i]+r[i+1:]) for i in range(len(r)))
    print(sum(ok([int(x) for x in r.split()]) for r in open("/Users/sudhamhebbar/Documents/AOC2024/Day2/input.txt")))
    print(sum(ok2([int(x) for x in r.split()]) for r in open("/Users/sudhamhebbar/Documents/AOC2024/Day2/input.txt")))
aoc02()