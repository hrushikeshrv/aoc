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


def expand_basin(vent_map, starting_point, max_x, max_y, ignore_points):
    basin_set = set()
    new_points = set()
    ignore_points.add(starting_point)
    # Expand in the +x direction
    current_x = starting_point[0]
    while current_x < max_x:      # TODO may throw index error
        if int(vent_map[starting_point[1]][current_x+1]) == 9:
            break
        current_x += 1
        if current_x == max_x or int(vent_map[starting_point[1]][current_x]) <= int(vent_map[starting_point[1]][current_x+1]):
            # basin_size += 1
            basin_set.add((current_x, starting_point[1]))
            new_points.add((current_x, starting_point[1]))
        else:
            break
    # Expand in the -x direction
    current_x = starting_point[0]
    while current_x > 0:
        if int(vent_map[starting_point[1]][current_x-1]) == 9:
            break
        current_x -= 1
        if current_x == 0 or int(vent_map[starting_point[1]][current_x]) <= int(vent_map[starting_point[1]][current_x-1]):
            # basin_size += 1
            basin_set.add((current_x, starting_point[1]))
            new_points.add((current_x, starting_point[1]))
        else:
            break
    
    # Expand in the +y direction
    current_y = starting_point[1]
    while current_y < max_y:
        if int(vent_map[current_y+1][starting_point[0]]) == 9:
            break
        current_y += 1
        if current_y == max_y or int(vent_map[current_y][starting_point[0]]) <= int(vent_map[current_y+1][starting_point[0]]):
            # basin_size += 1
            basin_set.add((starting_point[0], current_y))
            new_points.add((starting_point[0], current_y))
        else:
            break
    
    # Expand in the -y direction
    current_y = starting_point[1]
    while current_y > 0:
        if int(vent_map[current_y-1][starting_point[0]]) == 9:
            break
        current_y -= 1
        if current_y == 0 or int(vent_map[current_y][starting_point[0]]) <= int(vent_map[current_y-1][starting_point[0]]):
            # basin_size += 1
            basin_set.add((starting_point[0], current_y))
            new_points.add((starting_point[0], current_y))
        else:
            break
    
    # print(f'Considering low point {vent_map[starting_point[1]][starting_point[0]]}.')
    # print(f'Found new points {new_points}')
    new_points = new_points.difference(ignore_points)
    # print(f'Ignoring {ignore_points}')
    
    # print(f'New points are now {new_points}')
    # raise ValueError
    for new_point in new_points:
        basin_set.update(expand_basin(vent_map, new_point, max_x, max_y, ignore_points))
    return basin_set


def solve_2(vent_map):
    low_points = get_low_points(vent_map)
    max_x = len(vent_map[0]) - 1
    max_y = len(vent_map) - 1
    basin_sizes = []
    for point in low_points:
        basin_sizes.append(len(expand_basin(vent_map, point, max_x, max_y, set())))
    basin_sizes.sort()
    # return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]
    return basin_sizes[-4:]


ans = solve_2(vents)
print(ans)
