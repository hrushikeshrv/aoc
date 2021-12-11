"""
Problem 11 - https://adventofcode.com/2021/day/11
"""

# Set up the input
with open('input-11.txt', 'r') as file:
    octopuses = list(map(lambda x: list(x.strip()), file.readlines()))

with open('input-11-test.txt', 'r') as file:
    test_octopuses = list(map(lambda x: list(x.strip()), file.readlines()))


# Define helper functions
def get_neighbours(x, y, max_x, max_y):
    neighbours = []
    if 0 < x < max_x and 0 < y < max_y:
        neighbours = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
    elif 0 < x < max_x and y == 0:
        neighbours = [(x-1, y), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
    elif 0 < x < max_x and y == max_y:
        neighbours = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y)]
    elif x == 0 and 0 < y < max_y:
        neighbours = [(x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1)]
    elif x == max_x and 0 < y < max_y:
        neighbours = [(x, y-1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1)]
    elif x == 0 and y == 0:
        neighbours = [(x+1, y), (x+1, y+1), (x, y+1)]
    elif x == max_x and y == 0:
        neighbours = [(x-1, y), (x-1, y+1), (x, y+1)]
    elif x == 0 and y == max_y:
        neighbours = [(x, y-1), (x+1, y-1), (x+1, y)]
    elif x == max_x and y == max_y:
        neighbours = [(x-1, y), (x-1, y-1), (x, y-1)]
    return set(neighbours)


def flash_octopuses(octopus_map, flashed_octopuses, max_x, max_y):
    """
    Flashes all octopuses in the map and keeps going till no octopuses flash
    :param max_y:
    :param max_x:
    :param octopus_map:
    :param flashed_octopuses:
    :return:
    """
    new_flashes = 0
    already_flashed = flashed_octopuses.copy()
    for row in range(max_y+1):
        for col in range(max_x+1):
            if int(octopus_map[row][col]) > 9 and (col, row) not in flashed_octopuses:
                # This octopus will flash
                print(f'Flashing {(col, row)}')
                new_flashes += 1
                flashed_octopuses.add((col, row))
                n = get_neighbours(col, row, max_x, max_y)
                for neighbour in n:
                    _ = octopus_map[neighbour[1]][neighbour[0]]
                    _ = str(int(_) + 1)
    while new_flashes > 0:
        new_flashes = flash_octopuses(octopus_map, flashed_octopuses, max_x, max_y)
    newly_flashed = flashed_octopuses - already_flashed
    print(f'{newly_flashed} octopuses flashed')
    for point in newly_flashed:
        octopus_map[point[1]][point[0]] = '0'
    return len(flashed_octopuses) - len(already_flashed)


def increment_step(octopus_map, max_x, max_y):
    flashes = 0
    for row in range(max_y+1):
        for col in range(max_x+1):
            octopus_map[row][col] = str(int(octopus_map[row][col]) + 1)
    flashes += flash_octopuses(octopus_map, set(), max_x, max_y)
    return flashes


def solve_1(octopus_map, steps):
    flashes = 0
    max_x = len(octopus_map) - 1
    max_y = len(octopus_map[0]) - 1
    for i in range(steps):
        flashes += increment_step(octopus_map, max_x, max_y)
        print(f'Counted total {flashes} flashes after step {i+1}')
        print(f'Map now looks like')
        for row in octopus_map:
            print(row)
        if i == 2:
            raise
    return flashes


ans = solve_1(test_octopuses, 100)
print(ans)
