
# Main solving logic
with open('/Users/sudhamhebbar/Documents/AOC2024/Day5/input.txt', 'r') as files:
    rules_str = ''.join(line.strip() for line in files)
# parents = collections.defaultdict(list)
# edges = []
# for line in lines:
#     a, b = line.strip().split('|')
#     edges.append((a, b))
#     parents[b].append(a)

with open('/Users/sudhamhebbar/Documents/AOC2024/Day5/rules.txt', 'r') as files:
    lines = files.readlines()

sequences = []
for line in lines:
    sequences.append([int(s) for s in line.strip().split(',')])

# # Solve the problem
# res = 0
# for rule in rules:
#     res += topological_sort_middle_value(rule, edges)
import functools

def parse_rules(rules_str):
    """
    Parse the rules from a multi-line string into a dictionary of rules.
    
    Args:
        rules_str (str): A string containing rules in the format 'x|y', one per line
    
    Returns:
        dict: A dictionary mapping first numbers to their allowed second numbers
    """
    rules = {}
    for line in rules_str.strip().split('\n'):
        first, second = map(int, line.split('|'))
        if first not in rules:
            rules[first] = set()
        rules[first].add(second)
    return rules

def build_order_map(rules):
    """
    Build a comprehensive order map from the given rules.
    
    Args:
        rules (dict): A dictionary of allowed rules
    
    Returns:
        dict: A dictionary representing the order of elements
    """
    # Track direct and transitive orders
    order = {}
    
    # First, add all direct rules
    for first, seconds in rules.items():
        if first not in order:
            order[first] = set()
        order[first].update(seconds)
    
    # Find all possible transitive relationships
    changed = True
    while changed:
        changed = False
        for x in list(order.keys()):
            for y in list(order.get(x, [])):
                if y in order:
                    new_elements = order[y] - order.get(x, set())
                    if new_elements:
                        order[x] = order.get(x, set()).union(new_elements)
                        changed = True
    
    return order

def create_comparator(order_map):
    """
    Create a custom comparator function based on the order map.
    
    Args:
        order_map (dict): A dictionary representing the order of elements
    
    Returns:
        function: A comparison function
    """
    def compare(a, b):
        # If a comes before b in the order map, return negative
        if a in order_map and b in order_map.get(a, set()):
            return -1
        # If b comes before a in the order map, return positive
        if b in order_map and a in order_map.get(b, set()):
            return 1
        
        # If no direct relationship, maintain original order
        return 0
    
    return compare

def is_sorted_sequence(sequence, order_map):
    """
    Check if a sequence is sorted according to the given order map.
    
    Args:
        sequence (list): A list of integers to check
        order_map (dict): A dictionary representing the order of elements
    
    Returns:
        bool: True if the sequence is sorted, False otherwise
    """
    comparator = create_comparator(order_map)
    
    # Check each adjacent pair
    for i in range(len(sequence) - 1):
        if comparator(sequence[i], sequence[i+1]) > 0:
            return False
    return True

def sort_sequence(sequence, order_map):
    """
    Sort a sequence based on the custom comparator.
    
    Args:
        sequence (list): A list of integers to sort
        order_map (dict): A dictionary representing the order of elements
    
    Returns:
        list: Sorted sequence
    """
    comparator = create_comparator(order_map)
    return sorted(sequence, key=functools.cmp_to_key(comparator))

def process_sequences(rules_str, sequences):
    """
    Process sequences, accumulating sorted and sorting unsorted sequences.
    
    Args:
        rules_str (str): Rules defining the order
        sequences (list): List of sequences to process
    
    Returns:
        tuple: (sorted_sequences, sorted_unsorted_sequences)
    """
    # Parse rules and build order map
    rules = parse_rules(rules_str)
    order_map = build_order_map(rules)
    
    # Separate sorted and unsorted sequences
    sorted_sequences = []
    sorted_unsorted_sequences = []
    
    for seq in sequences:
        if is_sorted_sequence(seq, order_map):
            sorted_sequences.append(seq)
        else:
            # Sort the unsorted sequence
            sorted_unsorted_sequences.append(sort_sequence(seq, order_map))
    
    return sorted_sequences, sorted_unsorted_sequences


# Sequences to process

# Process and print results
sorted_sequences, sorted_unsorted_sequences = process_sequences(rules_str, sequences)

part1 = 0
part2 = 0
print("Sorted Sequences (Already Sorted):")
for seq in sorted_sequences:
    n = len(seq)
    part1 += seq[n//2]

print("\nSorted Sequences (Previously Unsorted):")
for seq in sorted_unsorted_sequences:
    n = len(seq)
    part2 += seq[n//2]
print(part1)
print(part2)