with open('/Users/sudhamhebbar/Documents/AOC2024/Day3/input.txt', 'r') as files:
    lines = files.readlines()
input_string = ''
for line in lines:
    input_string+=line

input_string = "do()" + input_string
import re
# def mul_generator(s):
#     word = "mul"
#     start = 0
#     while True:
#         # Find the next occurrence of "mul"
#         index = s.find(word, start)
#         if index == -1:
#             break  # Stop if no more occurrences
#         yield index
#         # Move the starting point past the current occurrence
#         start = index + len(word)

def mul(a, b):
    return a*b
pattern = r"mul\(\d+,\s*\d+\)"
matches = re.findall(pattern, input_string)
re.finditer

print(matches)
res= 0
for i in matches:
    res += eval(i)
print(res)
import re

def emit_mul_between_do_dont(input_string):
    """
    Generator that emits 'mul(a, b)' matches between 'do()' and 'don't()'.

    :param input_string: The input string to parse.
    :yield: Each 'mul(a, b)' match.
    """
    # Regex patterns
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    mul_pattern = re.compile(r"mul\(\d+,\s*\d+\)")
    
    # Start processing from the beginning of the string
    pos = 0
    while True:
        # Find the next 'do()'
        do_match = do_pattern.search(input_string, pos)
        if not do_match:
            break  # No more 'do()', exit
        
        # Start after 'do()'
        pos = do_match.end()

        # Emit 'mul(a, b)' until 'don't()' is found
        while True:
            dont_match = dont_pattern.search(input_string, pos)
            mul_match = mul_pattern.search(input_string, pos)

            if mul_match and (not dont_match or mul_match.start() < dont_match.start()):
                # Emit mul match
                yield mul_match.group()
                # Move position forward
                pos = mul_match.end()
            else:
                # Stop on 'don't()' or no more 'mul'
                pos = dont_match.end() if dont_match else pos
                break
res = 0
for match in emit_mul_between_do_dont(input_string):
    res += eval(match)
print(res)