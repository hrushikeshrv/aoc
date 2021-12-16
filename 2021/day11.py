"""
Problem 11 - https://adventofcode.com/2021/day/11
"""

# Set up the input
with open('input-11.txt', 'r') as file:
    octopuses = list(map(lambda x: list(x.strip()), file.readlines()))

with open('input-11-test.txt', 'r') as file:
    test_octopuses = list(map(lambda x: list(x.strip()), file.readlines()))


# Define helper functions
def increment_step(octopus_map, max_x, max_y):
    flashes = 0
    stack = []
    for row in range(max_y+1):
        for col in range(max_x+1):
            octopus_map[row][col] = str(int(octopus_map[row][col]) + 1)
            if int(octopus_map[row][col]) > 9:
                flashes += 1
                stack.append((col, row))
    while stack:
        col, row = stack.pop()
        for x, y in [(col-1, row), (col-1, row-1), (col, row-1), (col+1, row-1), (col+1, row), (col+1, row+1), (col, row+1), (col-1, row+1)]:
            if 0 <= x <= max_x and 0 <= y <= max_y and int(octopus_map[y][x]) > 0:
                octopus_map[y][x] = str(int(octopus_map[y][x]) + 1)
                if int(octopus_map[y][x]) > 9:
                    flashes += 1
                    stack.append((x, y))
    return flashes


def solve_1(octopus_map, steps):
    flashes = 0
    max_x = len(octopus_map) - 1
    max_y = len(octopus_map[0]) - 1
    for i in range(steps):
        flashes += increment_step(octopus_map, max_x, max_y)
    return flashes


ans = solve_1(test_octopuses, 100)
print(ans)
