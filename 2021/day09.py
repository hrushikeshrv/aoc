"""
Problem 9 - https://adventofcode.com/2021/day/9
"""

# Set up the input
with open('input-09.txt', 'r') as file:
    vents = list(map(lambda x: x.strip(), file.readlines()))

with open('input-09-test.txt', 'r') as file:
    test_vents = list(map(lambda x: x.strip(), file.readlines()))


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


# ans = solve_1(vents)
# print(ans)
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


def fill_basin(vent_map, starting_point, max_x, max_y, visited_points):
    # print(f'Starting from low point {starting_point} - {vent_map[starting_point[1]][starting_point[0]]}')
    visited_points.add(starting_point)
    new_points = set()
    basin_points = {(starting_point[0], starting_point[1])}
    neighbours = get_new_neighbours(starting_point[0], starting_point[1], max_x, max_y, visited_points)
    for n in neighbours:
        # If this neighbour is also a low point, add it to new_points
        second_neighbours = get_new_neighbours(n[0], n[1], max_x, max_y, visited_points)
        smallest = True
        number = int(vent_map[n[1]][n[0]])
        # print(f'Considering point {n} - {number}')
        for n2 in second_neighbours:
            # print(f'Found neighbour {n2} - {vent_map[n2[1]][n2[0]]}')
            if int(vent_map[n2[1]][n2[0]]) <= number:
                smallest = False
        if smallest and len(second_neighbours) > 0:
            # print(f'{number} is in the basin because it is smaller than its neighbours {second_neighbours}')
            new_points.add(n)
            basin_points.add(n)
    new_points = new_points.difference(visited_points)
    for new_point in new_points:
        basin_points.update(fill_basin(vent_map, new_point, max_x, max_y, visited_points))
    return basin_points


def solve_2(vent_map):
    low_points = get_low_points(vent_map)
    # print(f'Found low points {low_points}')
    max_x = len(vent_map[0]) - 1
    max_y = len(vent_map) - 1
    basin_sizes = []
    for point in low_points:
        basin = fill_basin(vent_map, point, max_x, max_y, set())
        # print(f'Found basin {basin}')
        basin_sizes.append(len(basin))
    basin_sizes.sort()
    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]
    # return basin_sizes[-4:]


ans = solve_2(vents)
print(ans)
