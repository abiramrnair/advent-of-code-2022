# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
def containsDuplicate(string):
    obj = {}
    for char in string:
        if char not in obj:
            obj[char] = 0
        obj[char] += 1
    for key in obj:
        if obj[key] > 1:
            return True
    return False
for line in input_lines:
    i = 0
    while i + 4 < len(line):
        if not containsDuplicate(line[i:i+4]):
            print(line[i:i+4])
            print(i+4)
            break
        i += 1
# Answer: 1287

# Part Two
for line in input_lines:
    i = 0
    while i + 14 < len(line):
        if not containsDuplicate(line[i:i+14]):
            print(line[i:i+14])
            print(i+14)
            break
        i += 1
# Answer: 3716