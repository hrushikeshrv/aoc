"""
Problem 13 - https://adventofcode.com/2021/day/13

Part 1 -
    Given a transparent paper with some dots and instructions on how to
    fold the paper, fold it once and return the number of dots visible

Part 2 -
    Given the same transparent paper with some dots, perform a series of
    folds and return the resulting 8 digit code
"""


# Set up the input
def build_map(lines, line_count):
    max_x, max_y = 0, 0
    folds = []
    for c in lines:
        if not c[0].isnumeric() and c.strip():
            _ = c.split()[2].split('=')
            folds.append((_[0], int(_[1])))
            continue
        if not c.strip():
            continue
        _ = c.strip().split(',')
        
        if int(_[0]) > max_x:
            max_x = int(_[0])
        if int(_[1]) > max_y:
            max_y = int(_[1])
    dots = [['.' for i in range(max_x + 1)] for j in range(max_y + 1)]
    for i in range(line_count):
        _ = dot_coordinates[i].split(',')
        dots[int(_[1])][int(_[0])] = '#'
    return dots, folds


with open('inputs/input-13.txt', 'r') as file:
    dot_coordinates = file.readlines()
    dots, folds = build_map(dot_coordinates, 928)
    

# Define helper functions
def combine_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        if list1[i] == '#' or list2[i] == '#':
            result.append('#')
        else:
            result.append('.')
    return result


def fold(dot_map, along, position):
    max_x = len(dot_map[0])
    max_y = len(dot_map)
    if along == 'x':
        for i in range(1, max_x - position):
            list1 = [dot_map[j][position - i] for j in range(max_y)]
            list2 = [dot_map[j][position + i] for j in range(max_y)]
            result = combine_lists(list1, list2)
            for j in range(max_y):
                dot_map[j][position - i] = result[j]
        for i in range(len(dot_map)):
            dot_map[i] = dot_map[i][:position]
    else:
        for i in range(1, max_y - position):
            dot_map[position - i] = combine_lists(dot_map[position - i], dot_map[position + i])
        dot_map = dot_map[:position]
    return dot_map


# Solution to part 1
def solve_1(dot_map, along, position):
    dot_map = fold(dot_map, along, position)
    dot_count = 0
    for i in range(len(dot_map)):
        for j in range(len(dot_map[0])):
            if dot_map[i][j] == '#':
                dot_count += 1
    return dot_count


ans = solve_1(dots, 'x', 655)
print(ans)
# Answer was 790


# Solution to part 2
def solve_2(dot_map, folds):
    for f in folds:
        dot_map = fold(dot_map, f[0], int(f[1]))
    for row in dot_map:
        print(' '.join(row))


solve_2(dots, folds)
# Answer was PGHZBFJC
