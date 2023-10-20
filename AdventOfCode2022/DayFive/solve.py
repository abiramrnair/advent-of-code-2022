# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
containers = {
    1: 'jhpmsfnv',
    2: 'srlmjdq',
    3: 'nqdhcswb',
    4: 'rscl',
    5: 'mvtpfb',
    6: 'trqnc',
    7: 'gvr',
    8: 'czspdlr',
    9: 'dsjvgpbf'
}
for key in containers:
    containers[key] = list(containers[key])
def moveBoxes(start, end, toMove):
    for _ in range(toMove):
        containers[end].append(containers[start].pop())
def moveBoxesTwo(start, end, toMove):
    boxes = []
    for _ in range(toMove):
        elem = containers[start].pop()
        boxes.append(elem)
    for num in boxes[::-1]:
        containers[end].append(num)
def getTopCrates():
    res = []
    for key in containers:
        res.append(containers[key][-1])
    return ''.join(res)
# for line in input_lines:
#     command = line.split('from')
#     toMove = int(command[0].split(' ')[1])
#     startStack, endStack = command[1].split('to')
#     moveBoxes(int(startStack), int(endStack), toMove)
# print(getTopCrates()) Answer: SBPQRSCDF

# Part Two
for line in input_lines:
    command = line.split('from')
    toMove = int(command[0].split(' ')[1])
    startStack, endStack = command[1].split('to')
    moveBoxesTwo(int(startStack), int(endStack), toMove)
print(getTopCrates()) # Answer: RGLVRCQSB