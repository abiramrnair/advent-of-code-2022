# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
forest = []
for line in input_lines:
    forest.append(list(line))
ROWS, COLS = len(forest), len(forest[0])

def isVisible(i, j):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        visible = True
        x_inc, y_inc = direction
        x = i + x_inc
        y = j + y_inc
        while x >= 0 and x < ROWS and y >= 0 and y < COLS:
            if forest[x][y] >= forest[i][j]:
                visible = False
            x += x_inc
            y += y_inc
        if visible:
            return visible
    return False

def getScenicScore(i, j):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    score = 1
    for direction in directions:
        view_dist = 0
        x_inc, y_inc = direction
        x, y = i + x_inc, j + y_inc
        while x >= 0 and x < ROWS and y >= 0 and y < COLS:
            if forest[x][y] >= forest[i][j]:
                view_dist += 1
                break
            view_dist += 1
            x += x_inc
            y += y_inc
        score *= view_dist
    return score

total_visible = 0
for i in range(ROWS):
    for j in range(COLS):
        if i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1:
            total_visible += 1
        else:
            if isVisible(i, j):
                total_visible += 1
print(total_visible) # Answer: 1782

# Part Two
max_scenic_score = 0
for i in range(ROWS):
    for j in range(COLS):
        max_scenic_score = max(max_scenic_score, getScenicScore(i, j))
print(max_scenic_score) # Answer: 474606