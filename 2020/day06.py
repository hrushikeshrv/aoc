"""
Problem 6 - https://adventofcode.com/2020/day/6

Part 1 -
    Given a series sets of strings, count the total number of distinct characters in the sets of strings

Part 2 -
    Given the same series of sets of strings, count the total number of common characters present in each individual set of strings
"""
from collections import Counter

# Set up the input
with open('input-06122020.txt', 'r') as file:
    yesses = file.readlines()


# Define helper functions
def get_answers_1(y):
    cache = ''
    answers = []
    for line in y:
        if line == '\n':
            answers.append(cache)
            cache = ''
        else:
            cache += line.replace('\n', '')
    # Append the last cache not counted in the for loop
    answers.append(cache)
    return answers


def get_answers_2(y):
    cache = ''
    n = 0
    answers = []
    for line in y:
        if line == '\n':
            answers.append((cache, n))
            cache = ''
            n = 0
        else:
            cache += line.replace('\n', '')
            n += 1
    answers.append((cache, n))
    return answers


# Solution to part 1
def solve_1():
    answers = get_answers_1(yesses)
    yes = 0
    for answer in answers:
        yes += len(set(answer))
    return yes


ans_1 = solve_1()
print(ans_1)


# Answer was 6310

# Solution to part 2
def solve_2():
    answers = get_answers_2(yesses)
    yes = 0
    for answer in answers:
        freq = dict(Counter(answer[0]))
        for v in freq.values():
            if v == answer[1]:
                yes += 1
    return yes


ans_2 = solve_2()
print(ans_2)
# Answer was 3193
