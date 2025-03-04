from collections import defaultdict, deque
with open("/Users/sudhamhebbar/Documents/AOC2024/Day24/input.txt") as file:
    lines = file.readlines()
allvars = set()
codes = {}
for line in lines:
    a, b = line.strip().split(":")
    codes[a] = int(b)
    allvars.add(a)
def build_graph():
    graph = defaultdict(list)  # Adjacency list
    in_degree = defaultdict(int)  # Track in-degrees
    operations = [] 
    dependencies = []
    with open("/Users/sudhamhebbar/Documents/AOC2024/Day24/rules.txt") as file:
        lines = file.readlines()
    for line in lines:
        gate, var = line.split("->")
        a, b = gate.replace("AND", ":").replace("XOR", ":").replace("OR", ":").split(':')
        t = (var.strip(), [a.strip(), b.strip()], line.strip())
        allvars.add(var.strip())
        allvars.add(a.strip())
        allvars.add(b.strip()) 
        dependencies.append(t)
    for target, sources, operation in dependencies:
        for source in sources:
            graph[source].append(target)
            in_degree[target] += 1
        if target not in in_degree:
            in_degree[target] = 0  # Ensure target nodes are added
        operations.append((target, operation))
    return graph, in_degree, operations

def topological_sort(graph, in_degree, operations):
    zero_in_degree = deque([node for node in graph if in_degree[node] == 0])
    topo_order = []
    operation_map = {target: operation for target, operation in operations}

    while zero_in_degree:
        current = zero_in_degree.popleft()
        if current in operation_map:
            topo_order.append(operation_map[current])  # Add the operation to the sorted list

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return topo_order
    
graph, in_degree, operations = build_graph()
for node in allvars:
    if node not in in_degree:
        in_degree[node] = 0
sorted_operations = topological_sort(graph, in_degree, operations)
print(sorted_operations)
for operation in sorted_operations:
    gate, var = operation.split("->") 
    if("AND" in gate):
        a, b = gate.split("AND")
        a = a.strip()
        b = b.strip()
        var = var.strip()
        codes[var] = codes[a] & codes[b]
    elif("XOR" in gate):
        a, b = gate.split("XOR")
        a = a.strip()
        b = b.strip()
        var = var.strip()
        codes[var] = codes[a] ^ codes[b]
    else:
        a, b = gate.split("OR")
        a = a.strip()
        b = b.strip()
        var = var.strip()
        codes[var] = codes[a] | codes[b]
maxnum = 0
zcodes = set()
for i in allvars:
    if(i.startswith("z")):
        zcodes.add(i)
        maxnum = max(maxnum, int(i.strip("z")))

res = [0]*(maxnum + 1)
print(res)
for zcode in zcodes:
    idx = int(zcode.strip("z"))
    print(idx)
    res[idx] = str(codes[zcode])
res.reverse()
s = ''.join(res)

print(int(s, 2))

           