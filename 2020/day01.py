"""
Problem 1 - https://adventofcode.com/2020/day/1

Part 1 -
    Given a list of numbers, find the two numbers that sum to 2020 and return their product

Part 2 -
    Given a list of numbers, find the three numbers that sum to 2020 and return their product
"""

# Set up the input
with open('input-01122020.txt', 'r') as file:
    s = file.readlines()

l = list(map(lambda x: int(x), s))


# Solution to part 1
def solve_1(l):
    """
    Solution to AoC 2020 day 1, part 1.
    """
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] + l[j] == 2020:
                return l[i] * l[j]


ans_1 = solve_1(l)
print(ans_1)


# Answer was 437931.

# Solution to part 2
def solve_2(l):
    """
    Solution to AoC 2020 day2, part 2.
    """
    for i in range(len(l)):
        for j in range(i, len(l)):
            for k in range(j, len(l)):
                if l[i] + l[j] + l[k] == 2020:
                    return l[i] * l[j] * l[k]


ans_2 = solve_2(l)
print(ans_2)
# Answer was 157667328
