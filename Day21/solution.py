import math
start = 123
MOD = 16777216
def mix(a, b):
    return a^b
def prune(a):
    return a%MOD

def step1(a):
    return prune(mix(a, a*64))

def step2(a):
    return(mix(a, math.floor(a/32)))

def step3(a):
    m = mix(a, a*2048)
    return(prune(m))

def simulate(a, n):
    print("Initial a:", a)
    for i in range(n):
        tmp = step1(a)
        tmp = step2(tmp)
        a = step3(tmp)
    return a

with open('/Users/sudhamhebbar/Documents/AOC2024/Day21/input.txt') as file:
    lines = file.readlines()
res = 0
for line in lines:
    start = int(line.strip())
    res += simulate(start, 2000)

print(res)
