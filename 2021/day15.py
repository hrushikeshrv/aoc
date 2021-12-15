"""
Problem 15 - https://adventofcode.com/2021/day/15
"""

# Set up the input
with open('input-15.txt', 'r') as file:
    vents = list(map(lambda x: x.strip(), file.readlines()))
    max_x_1 = len(vents[0]) - 1
    max_y_1 = len(vents) - 1
    print(max_x_1, max_y_1)
    cache_1 = [[None for x in range(max_x_1 + 1)] for y in range(max_y_1 + 1)]

with open('input-15-test.txt', 'r') as file:
    test_vents = list(map(lambda x: x.strip(), file.readlines()))
    test_max_x = len(test_vents[0]) - 1
    test_max_y = len(test_vents) - 1
    test_cache = [[None for test_x in range(test_max_x + 1)] for test_y in range(test_max_y + 1)]


# Define helper functions
def shortest_path(x, y, max_x, max_y, cache, entering, vent_map):
    if x == max_x - 1 and y == max_y - 1:
        return int(vent_map[y][x])
    if cache[y][x] is not None:
        return cache[y][x]
    paths = []
    for new_x, new_y in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if (new_x, new_y) == entering:
            continue
        if not 0 <= new_x <= max_x or not 0 <= new_y <= max_y:
            continue
        if cache[new_y][new_x] is not None:
            return cache[new_y][new_x]
        print(f'Finding shortest path from {x, y}. Considering neighbour {new_x, new_y}')
        paths.append(shortest_path(new_x, new_y, max_x, max_y, cache, entering, vent_map) + int(vent_map[new_y][new_x]))
    cache[y][x] = min(paths)
    return min(paths)


# Solution to part 1
def solve_1(vent_map, max_x, max_y, cache):
    return shortest_path(0, 0, max_x, max_y, cache, (None, None), vent_map)


ans = solve_1(test_vents, test_max_x, test_max_y, test_cache)
print(ans)
