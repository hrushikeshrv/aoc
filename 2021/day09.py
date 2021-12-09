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
    
    valleys = []
    
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
                valleys.append((col_ind, row_ind))
                # print(f'Found low point w number {num}. Neighbours {neighbours}')
                risk += num+1
    return risk


ans = solve_1(vents)
print(ans)
# Answer was 468
