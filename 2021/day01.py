"""
Problem 1 - https://adventofcode.com/2021/day/1

Part 1 -
    Given a list of numbers, count how many numbers are greater than the number that comes before them
    
Part 2 -
    Take a 3 day sliding sum window of the previous input and solve part 1 on it
"""

# Set up the input
with open('input-01.txt.', 'r') as file:
    lines = list(map(lambda x: int(x), file.readlines()))


# Solution to part 1
def solve_1(measurements):
    increases = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            increases += 1
    return increases


ans = solve_1(lines)
print(ans)
# Answer was 1692


# Solution to part 2
def solve_2(measurements):
    measurements_2 = []
    for i in range(len(measurements)-2):
        measurements_2.append(sum(measurements[i:i+3]))
    return solve_1(measurements_2)


ans = solve_2(lines)
print(ans)
# Answer was 1724
