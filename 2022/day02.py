with open('inputs/input-02.txt.', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

def solve_1(strat):
    score = 0
    score_map = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }
    for line in strat:
        score += score_map[line]
    return score

ans = solve_1(lines)
print(ans)
# Answer was 9651

def solve_2(strat):
    score = 0
    score_map = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }
    for line in strat:
        score += score_map[line]
    return score

ans = solve_2(lines)
print(ans)
# Answer was 10560