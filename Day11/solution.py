# def transform_stone(num):
#     """
#     Optimized stone transformation with minimal memory allocation
#     """
#     # 0 becomes 1
#     if num == 0:
#         return [1]
    
#     # Convert to string once
#     s = str(num)
    
#     # Even number of digits: split
#     if len(s) % 2 == 0:
#         mid = len(s) // 2
#         return [int(s[:mid]), int(s[mid:])]
    
#     # Default: multiply by 2024
#     return [num * 2024]

# def simulate_blinks(initial_stones, num_blinks):
#     """
#     Highly optimized blink simulation using in-place list transformation
#     """
#     stones = initial_stones.copy()
    
#     for _ in range(num_blinks):
#         # Preallocate with maximum possible size to reduce reallocations
#         new_stones = [0] * (len(stones) * 2)
#         new_index = 0
        
#         # Transform each stone
#         for stone in stones:
#             # Transform stone and add to new list
#             transformed = transform_stone(stone)
#             for t in transformed:
#                 new_stones[new_index] = t
#                 new_index += 1
        
#         # Trim to actual size
#         stones = new_stones[:new_index]
    
#     return stones

# # Read input
# with open('/Users/sudhamhebbar/Documents/AOC2024/Day11/input.txt', 'r') as files:
#     lines = files.readlines()
# initial_stones = [int(x) for x in lines[0].strip().split()]

# # Simulate 75 blinks
# final_stones = simulate_blinks(initial_stones, 75)

# # Print results
# print(f"Number of stones after 75 blinks: {len(final_stones)}")

from collections import defaultdict

with open("/Users/sudhamhebbar/Documents/AOC2024/Day11/input.txt") as f:
    nums = list(map(int, f.read().split()))
    input = defaultdict(int)
    for num in nums: input[num] += 1

    for i in range(75): 
        if i == 25: print(sum(input.values()))
        updates = defaultdict(int)

        for k, v in input.items():
            s = str(k)
            updates[k] -= v

            if k == 0: 
                updates[1] += v
            elif len(s) % 2 == 0:
                l, r = s[:len(s)//2], s[len(s)//2:]
                updates[int(l)] += v
                updates[int(r)] += v
            else: 
                updates[k*2024] += v

        for k, v in updates.items():
            input[k] += v
            if input[k] == 0: input.pop(k)
       
    print(sum(input.values()))