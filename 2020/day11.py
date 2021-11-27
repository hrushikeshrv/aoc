"""
Problem 11 - https://adventofcode.com/2020/day/11
#TODO - AAdd solution to part 2
Part 1 -
    Given a grid of seats and the rules for the seats to be filled or emptied, figure out the number of occupied seats at equillibrium

Part 2 - 
    Same as part 1 with different rules
"""
# Just to satisfy mypy
from typing import List

# Set up the input
with open('input-11122020.txt', 'r') as file:
    s = file.readlines()

seats_1 = [x[:-1] for x in s]

seats: List = list()

for row in seats_1:
    seats.append([])
    for col in row:
        seats[-1].append(col)


# Define helper functions
def get_neighbours(seat, max_row, max_col):
    """
    Takes in the coordinates of a seat and returns all the neighbours of the seat
    """
    
    r = seat[0]
    c = seat[1]
    
    if 0 < r < max_row and 0 < c < max_col:
        return [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c),
                (r + 1, c + 1)]
    
    if r == 0:
        if c == 0:
            return [(r, c + 1), (r + 1, c), (r + 1, c + 1)]
        elif c == max_col:
            return [(r, c - 1), (r + 1, c - 1), (r + 1, c)]
        return [(r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    elif r == max_row:
        if c == 0:
            return [(r - 1, c), (r - 1, c + 1), (r, c + 1)]
        elif c == max_col:
            return [(r, c - 1), (r - 1, c), (r - 1, c - 1)]
        return [(r, c - 1), (r, c + 1), (r - 1, c - 1), (r - 1, c), (r - 1, c + 1)]
    
    elif c == 0:
        return [(r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c), (r + 1, c + 1)]
    elif c == max_col:
        return [(r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c - 1), (r - 1, c)]


def get_new_seat_from_neighbours(seats, seat, neighbours):
    if seat == 'L' and not any(seats[n[0]][n[1]] == '#' for n in neighbours):
        return '#'
    elif seat == '#' and sum([seats[n[0]][n[1]] == '#' for n in neighbours]) >= 4:
        return 'L'
    else:
        return seat


# Solution to part 1
def solve_1(seats: List[list]) -> int:
    repeat_flag = True
    replace_list: List = list()
    
    while repeat_flag:
        repeat_flag = False
        if replace_list:
            for r, c in replace_list:
                if seats[r][c] == '#':
                    seats[r][c] = 'L'
                elif seats[r][c] == 'L':
                    seats[r][c] = '#'
                else:
                    raise ValueError('"."s are not supposed to be changed. Check solve_1()\'s implementation.')
            replace_list = []
        
        for row in range(len(seats)):
            for col in range(len(seats[row])):
                if seats[row][col] == '.':
                    continue
                
                neighbours = get_neighbours((row, col), len(seats) - 1, len(seats[0]) - 1)
                new_seat = get_new_seat_from_neighbours(seats, seats[row][col], neighbours)
                
                if new_seat != seats[row][col]:
                    replace_list.append((row, col))
                    repeat_flag = True
    
    occ = 0
    for row in seats:
        for col in row:
            if col == '#':
                occ += 1
    return occ


ans_1 = solve_1(seats)
print(ans_1)


# Answer was 2481

# Solution to part 2
def solve_2(seats):
    raise NotImplementedError
