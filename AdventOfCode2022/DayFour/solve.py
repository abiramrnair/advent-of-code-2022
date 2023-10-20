# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
def isPairWithinRange(p1, p2):
    p1Lower = p1[0]
    p1Higher = p1[1]
    p2Lower = p2[0]
    p2Higher = p2[1]
    if int(p1Lower) >= int(p2Lower) and int(p1Higher) <= int(p2Higher):
        return True
    return False
def isPairOverlapping(p1, p2):
    p1Lower = p1[0]
    p1Higher = p1[1]
    p2Lower = p2[0]
    p2Higher = p2[1]
    if int(p2Lower) <= int(p1Higher) and int(p2Lower) >= int(p1Lower):
        return True
    return False
fully_contained = 0
for line in input_lines:
    pair_one, pair_two = line.split(',')
    pair_one = pair_one.split('-')
    pair_two = pair_two.split('-')
    if isPairWithinRange(pair_one, pair_two) or isPairWithinRange(pair_two, pair_one):
        fully_contained += 1
print(fully_contained) # Answer: 490

# Part Two
num_overlaps = 0
for line in input_lines:
    pair_one, pair_two = line.split(',')
    pair_one = pair_one.split('-')
    pair_two = pair_two.split('-')
    if isPairOverlapping(pair_one, pair_two) or isPairOverlapping(pair_two, pair_one):
        num_overlaps += 1
print(num_overlaps) # Answer: 921