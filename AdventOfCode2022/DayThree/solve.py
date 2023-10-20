# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
def getPriority(letter):
    if letter.islower():
        return (ord(letter) % 97) + 1
    else:
        return (ord(letter) % 65) + 27
def findCommonLetter(line):
    a = line[0:len(line) // 2]
    b = line[len(line) // 2:]
    common = set(a).intersection(set(b))
    return list(common)[0]

total_sum = 0
for line in input_lines:
    common = findCommonLetter(line)
    total_sum += getPriority(common)
print(total_sum)

# Part Two
total_sum = 0
for i in range(0, len(input_lines), 3):
    a = input_lines[i]
    b = input_lines[i + 1]
    c = input_lines[i + 2]
    common = (set(a).intersection(set(b))).intersection(set(c))
    total_sum += getPriority(list(common)[0])
print(total_sum)