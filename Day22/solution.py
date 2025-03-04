from collections import defaultdict
with open("/Users/sudhamhebbar/Documents/AOC2024/Day22/input.txt") as file:
    lines = file.readlines()
adj = defaultdict(list)
seed = set()
for line in lines:
    a, b = line.strip().split("-")
    adj[a].append(b)
    adj[b].append(a)
    if('t' == a[0]):
        seed.add(a)
    if('t' == b[0]):
        seed.add(b)

def checkLan(start):
    neighbours = adj[start]
    # for mid in neighbours:
    #     neighbours = 
