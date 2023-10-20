# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
maxCalories = 0
localMaxCalories = 0
for num in input_lines:
    if not num:
        maxCalories = max(localMaxCalories, maxCalories)
        localMaxCalories = 0
    else:
        localMaxCalories += int(num)
print(maxCalories) # Answer: 66616

# Part Two
caloriesArray = []
maxCalories = 0
for num in input_lines:
    if not num:
        caloriesArray.append(maxCalories)
        maxCalories = 0
    else:
        maxCalories += int(num)
if maxCalories:
    caloriesArray.append(maxCalories)
print(sum(sorted(caloriesArray)[-3:])) # Answer: 199172