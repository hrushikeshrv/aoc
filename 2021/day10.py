"""
Problem 10 - https://adventofcode.com/2021/day/10

Part 1 -
    Given a sequence of opening and closing characters, find the "score" of the lines
    which do not follow the opening and closing character order

Part 2 -
    Given the same sequences of opening and closing characters, see if you can
    complete some of the sequences and return the median score of all the completed
    sequences
"""


# Set up the input
with open('input-10.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

# TODO - Delete all test files when done
with open('input-10-test.txt', 'r') as file:
    test_lines = list(map(lambda x: x.strip(), file.readlines()))


opening_char_set = {'[', '(', '{', '<'}
closing_chars = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}
closing_char_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


# Solution to part 1
def solve_1(nav_lines):
    score = 0
    for line in nav_lines:
        opened_chars = []
        for char in line:
            if char in opening_char_set:
                opened_chars.append(char)
            else:
                if char == closing_chars[opened_chars[-1]]:
                    opened_chars.pop()
                else:
                    # Found a corrupted line
                    score += closing_char_points[char]
                    break
    return score


ans = solve_1(lines)
print(ans)
# Answer was 367059


# Define helper functions
def get_incomplete_chars(line):
    opened_chars = []
    for char in line:
        if char in opening_char_set:
            opened_chars.append(char)
        else:
            if char == closing_chars[opened_chars[-1]]:
                opened_chars.pop()
            else:
                return []
    return opened_chars


incomplete_closing_char_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def get_incomplete_line_score(chars):
    score = 0
    while chars:
        closing_char = closing_chars[chars.pop()]
        score *= 5
        score += incomplete_closing_char_score[closing_char]
    return score


# Solution to part 2
def solve_2(nav_lines):
    scores = []
    for line in nav_lines:
        opened_chars = get_incomplete_chars(line)
        if not opened_chars:
            continue
        scores.append(get_incomplete_line_score(opened_chars))
    scores.sort()
    return scores[len(scores)//2]


ans = solve_2(lines)
print(ans)
# Answer was 1952146692
