"""
Problem 9 - https://adventofcode.com/2021/day/9

Part 1 -
    Given a 2D map of vent heights, find the lowest points and return the
    sum of their "risk" values

Part 2 -
    Given the same 2D map, find all the "basins" in the map and return
    the product of the 3 largest basins
"""

# Set up the input
with open('input-09.txt', 'r') as file:
    vents = list(map(lambda x: x.strip(), file.readlines()))


# Define helper functions
def get_neighbours(x, y, max_x, max_y):
    neighbours = []
    if x >= 1:
        if y >= 1:
            neighbours += [(x-1, y), (x, y-1)]
        else:
            neighbours += [(x-1, y)]
        if y < max_y:
            neighbours += [(x, y+1)]
        if x < max_x:
            neighbours += [(x+1, y)]
    else:
        if y >= 1:
            neighbours += [(x, y-1), (x+1, y)]
        else:
            neighbours += [(x, y+1), (x+1, y)]
        if y < max_y:
            neighbours += [(x, y+1)]
    return neighbours


# Solution to part 1
def solve_1(vent_map):
    max_x = len(vent_map[0])-1
    max_y = len(vent_map)-1
    
    risk = 0
    for row_ind in range(max_y+1):
        for col_ind in range(max_x+1):
            neighbours = get_neighbours(col_ind, row_ind, max_x, max_y)
            num = int(vent_map[row_ind][col_ind])
            smallest = True
            for n in neighbours:
                if int(vent_map[n[1]][n[0]]) <= num:
                    smallest = False
            if smallest:
                risk += num+1
    return risk


ans = solve_1(vents)
print(ans)
# Answer was 468


def get_new_neighbours(x, y, max_x, max_y, ignore_set):
    _ = get_neighbours(x, y, max_x, max_y)
    neighbours = []
    for n in _:
        if n not in ignore_set:
            neighbours.append(n)
    return neighbours


def get_low_points(vent_map):
    max_x = len(vent_map[0]) - 1
    max_y = len(vent_map) - 1
    low_points = []
    
    for row_ind in range(max_y + 1):
        for col_ind in range(max_x + 1):
            neighbours = get_neighbours(col_ind, row_ind, max_x, max_y)
            num = int(vent_map[row_ind][col_ind])
            smallest = True
            for n in neighbours:
                if int(vent_map[n[1]][n[0]]) <= num:
                    smallest = False
            if smallest:
                low_points.append((col_ind, row_ind))
    return low_points


def fill_basin(vent_map, x, y, max_x, max_y, visited_points):
    size = 1
    visited_points.add((x, y))
    for n in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        # If the new point is within the boundaries of the map
        # and the new point is not a 9
        # and we have not visited this point before, then recurse here
        if 0 <= n[0] <= max_x and 0 <= n[1] <= max_y and vent_map[n[1]][n[0]] != '9' and n not in visited_points:
            size += fill_basin(vent_map, n[0], n[1], max_x, max_y, visited_points)
    return size


def solve_2(vent_map):
    low_points = get_low_points(vent_map)
    max_x = len(vent_map[0]) - 1
    max_y = len(vent_map) - 1
    basin_sizes = []
    for point in low_points:
        basin = fill_basin(vent_map, point[0], point[1], max_x, max_y, set())
        basin_sizes.append(basin)
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


ans = solve_2(vents)
print(ans)
# Answer was 1280496
