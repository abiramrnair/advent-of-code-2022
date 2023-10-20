# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
cycle = 0
X = 1
signal_strength_sum = 0

instructions = input_lines[::-1]

while len(instructions):
    instruction = instructions.pop()
    cycles = 0
    val = 0
    if instruction == 'noop':
        cycles = 1
    else:
        cycles = 2
        _, val = instruction.split(' ')
    i = 0
    while i < cycles:
        i += 1
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength_sum += (cycle * X)

    X += int(val)

print(signal_strength_sum) # Answer: 17940

# Part Two
cycle = 0
X = 1
signal_strength_sum = 0
instructions = input_lines[::-1]
screen = ''

while len(instructions):
    instruction = instructions.pop()
    cycles = 0
    val = 0
    if instruction == 'noop':
        cycles = 1
    else:
        cycles = 2
        _, val = instruction.split(' ')
    i = 0
    while i < cycles:
        i += 1
        cycle += 1
        position = cycle - 1
        if (position % 40) in [X - 1, X, X + 1]:
            screen += '#'
        else:
            screen += '.'
    X += int(val)

for i in range(0, len(screen), 40):
    print(screen[i:i+40]) # Answer: ZCBAJFJZ