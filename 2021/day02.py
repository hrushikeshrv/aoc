"""
Problem 2 - https://adventofcode.com/2021/day/2

Part 1 -
    Given a list of forward, up, and down move instructions calculate the final position and return
    the product of x and y coordinates

Part 2 -
    Given the same moves but a different interpretation, return the product of x and y coordinates
"""

# Set up the input
with open('inputs/input-02.txt', 'r') as file:
    lines = list(map(lambda x: (x.split()[0], int(x.split()[1])), file.readlines()))


# Solution to part 1
def solve_1(moves):
    x, y = 0, 0
    for move in moves:
        if move[0] == 'forward':
            x += move[1]
        elif move[0] == 'down':
            y += move[1]
        elif move[0] == 'up':
            y -= move[1]
    return x * y


ans = solve_1(lines)
print(ans)
# Answer was 2147104


# Solution to part 2
def solve_2(moves):
    aim = 0
    x, y = 0, 0
    for move in moves:
        if move[0] == 'forward':
            x += move[1]
            y += aim * move[1]
        elif move[0] == 'down':
            aim += move[1]
        elif move[0] == 'up':
            aim -= move[1]
    return x * y


ans = solve_2(lines)
print(ans)
# Answer was 2044620088
