"""
#TODO - Add solution to part 2
Problem 10 - https://adventofcode.com/2020/day/10

Part 1 -
    Given a set of numbers, find the product of the number of pairs of numbers which differ by 1 and the number of pairs of numbers which differ by 3

Part 1 -
    Given the same set of numbers, find the number of ways to arrange them in ascending order such that two consecutive numbers differ by at most 3
"""

#Set up the input
with open('input-10122020.txt', 'r') as file:
    j = file.readlines()

j.append('0\n')
jolts = [int(x[:-1]) for x in j]
jolts.append(max(jolts) + 3)
jolts = sorted(jolts)

#Solution to part 1
def solve_1(jolts):
    diff = {1: 0, 2: 0, 3: 0}
    for i in range(1, len(jolts)):
        d = jolts[i] - jolts[i-1]
        diff[d] += 1
    return diff[1]*diff[3]

ans_1 = solve_1(jolts)
print(ans_1)
#Answer was 1820

#Solution to part 2
def solve_2(jolts):
    raise NotImplementedError