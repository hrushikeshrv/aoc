"""
Problem 5 - https://adventofcode.com/2021/day/5

Part 1 -
    Given a list of lines on a 2D graph, find the number of integral points where at least 2 horizontal or vertical
    lines intersect

Part 2 -
    Given the same set up, find the number of integral points where at least 2 horizontal, vertical, or diagonal
    lines intersect
"""

# Set up the input
with open('inputs/input-05.txt', 'r') as file:
    vents = file.readlines()


# Solution to part 1
def solve_1(vent_map, dimension):
    # Assume the ocean_floor is a dimension x dimension grid
    ocean_floor = [[0 for i in range(dimension)] for j in range(dimension)]
    for vent in vent_map:
        coords = vent.split('->')
        start = coords[0].split(',')
        end = coords[1].split(',')
        if int(start[0]) != int(end[0]) and int(start[1]) != int(end[1]):
            continue
        if int(start[0]) == int(end[0]):
            # Same x coordinate => row changes, column remains the same
            start_row, end_row = int(start[1]), int(end[1])
            if start_row > end_row:
                start_row, end_row = end_row, start_row
            for i in range(start_row, end_row + 1):
                ocean_floor[i][int(start[0])] += 1
                
        elif int(start[1]) == int(end[1]):
            # Same y coordinate => column changes, row remains the same
            start_column, end_column = int(start[0]), int(end[0])
            if start_column > end_column:
                start_column, end_column = end_column, start_column
            for i in range(start_column, end_column + 1):
                ocean_floor[int(start[1])][i] += 1
    
    dangerous_vents = 0
    for row in ocean_floor:
        for cell in row:
            if cell >= 2:
                dangerous_vents += 1
    return dangerous_vents, ocean_floor


ans, _ = solve_1(vents, 10)
print(ans)
# Answer was 7414


# Define helper functions
def get_diagonal_points(start_x, start_y, end_x, end_y):
    """
    Returns a list of tuples that contains diagonal points from one point to another
    :param start_x:
    :param start_y:
    :param end_x:
    :param end_y:
    :return:
    """
    points = []
    y_inc = 1
    if int(start_x) > int(end_x):
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
    if start_y > end_y:
        y_inc = -1
    while start_x <= end_x:
        points.append((start_x, start_y))
        start_x += 1
        start_y += y_inc
    
    return points


def get_points_from_line(line):
    """
    Returns a list of points on a vertical or horizontal line. Returns an empty list otherwise
    :param line:
    :return:
    """
    coords = line.split('->')
    start = list(map(lambda x: int(x), coords[0].split(',')))
    end = list(map(lambda x: int(x), coords[1].split(',')))
    
    points = []
    if start[0] == end[0]:
        if start[1] > end[1]:
            start, end = end, start
        row = start[1]
        while row <= end[1]:
            points.append((start[0], row))
            row += 1
        
    elif start[1] == end[1]:
        if start[0] > end[0]:
            start, end = end, start
        col = start[0]
        while col <= end[0]:
            points.append((col, start[1]))
            col += 1
    
    elif start[0] != end[0]:
        slope = (int(start[1]) - int(end[1])) / (int(start[0]) - int(end[0]))
        if abs(slope) == 1:
            points = get_diagonal_points(start[0], start[1], end[0], end[1])
    
    return points


def update_ocean_floor(points, ocean_floor):
    """
    Updates all the given points on the ocean floor and increments their value by 1
    :param points:
    :param ocean_floor:
    :return:
    """
    for point in points:
        ocean_floor[point[0]][point[1]] += 1
    return ocean_floor


# Solution to part 2
def solve_2(vent_map, dimension):
    ocean_floor = [[0 for i in range(dimension)] for j in range(dimension)]
    # Also consider lines at 45 degrees
    for vent in vent_map:
        points = get_points_from_line(vent)
        update_ocean_floor(points, ocean_floor)
        
    dangerous_vents = 0
    for row in ocean_floor:
        for cell in row:
            if cell >= 2:
                dangerous_vents += 1
    return dangerous_vents


ans = solve_2(vents, 1000)
print(ans)
# Answer was 19676
