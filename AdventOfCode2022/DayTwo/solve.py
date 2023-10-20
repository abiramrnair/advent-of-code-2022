# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
opp_code = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

human_code = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

end_code = {
    'X': 'lose',
    'Y': 'tie',
    'Z': 'win'
}

outcome_code = {
    'lose': 0,
    'tie': 3,
    'win': 6
}

shape_code = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

def getOutcome(human, opp):
    if human == opp:
        return 'tie'
    if human == 'rock' and opp == 'scissors':
        return 'win'
    if human == 'paper' and opp == 'rock':
        return 'win'
    if human == 'scissors' and opp == 'paper':
        return 'win'
    return 'lose'

def calculateScore(human, opp):
    outcome = getOutcome(human_code[human], opp_code[opp])
    score = outcome_code[outcome] + shape_code[human_code[human]]
    return score

def calculateScoreTwo(human, outcome):
    score = outcome_code[outcome] + shape_code[human]
    return score

total_score = 0
for line in input_lines:
    opp, human = line.split(' ')
    total_score += calculateScore(human, opp)
print(total_score) # Answer: 10718

# Part Two
def getHumanMove(opp, end):
    if end == 'tie':
        return opp
    if end == 'win':
        if opp == 'rock':
            return 'paper'
        if opp == 'paper':
            return 'scissors'
        if opp == 'scissors':
            return 'rock'
    if end == 'lose':
        if opp == 'rock':
            return 'scissors'
        if opp == 'paper':
            return 'rock'
        if opp == 'scissors':
            return 'paper'

total_score = 0
for line in input_lines:
    opp, end = line.split(' ')
    human = getHumanMove(opp_code[opp], end_code[end])
    total_score += calculateScoreTwo(human, end_code[end])
print(total_score)