"""
Problem 5 - https://adventofcode.com/2020/day/5

Part 1 - 
    Given instructions on how to find a seat id given a boarding pass and given a set of boarding passes, find the boarding pass with the maximum id

Part 2 - 
    With the same instructions on how to find the id of a seat, find the seat id missing from the list.
"""

#Set up the input
with open('input-05122020.txt', 'r') as file:
    passes = file.readlines()

#Define helper function(s)
def get_seat_from_code(code, row_flag = True):
    """
    Takes in a sequence and returns the row_id or column_id that sequence will result in
    """ 
    if row_flag:
        seat_range = [0, 127]
    else:
        seat_range = [0, 7]

    for char in code:
        if char == 'F' or char == 'L':
            seat_range = [seat_range[0], (seat_range[0] + seat_range[1])//2]
        else:
            seat_range = [(seat_range[0] + seat_range[1])//2 + 1, seat_range[1]]
    
    if seat_range[0] == seat_range[1]:
        return seat_range[0]
    else:
        raise ValueError("get_seat_from_code didn't run to completion.")


#Solution to part 1
def solve_1(l):
    max_id = 0
    
    for p in l:
        row_code = p[:7]
        col_code = p[-4:-1]

        row = get_seat_from_code(row_code, True)
        col = get_seat_from_code(col_code, False)

        seat_id = 8*row + col
        if max_id < seat_id:
            max_id = seat_id
    
    return max_id

ans_1 = solve_1(passes)
print(ans_1)
#Answer was 963

#Solution to part 2
def solve_2(l):
    seat_ids = []
    for p in l:
        row_code = p[:7]
        col_code = p[-4:-1]

        row = get_seat_from_code(row_code, True)
        col = get_seat_from_code(col_code, False)

        seat_id = 8*row + col
        seat_ids.append(seat_id)
    
    seat_ids = sorted(seat_ids)
    missing = []
    for i in range(len(seat_ids)):
        if seat_ids[i] - seat_ids[i-1] > 1:
            print(f'Seat between {seat_ids[i-1]} and {seat_ids[i]} is missing.')
            missing.append((seat_ids[i-1] + seat_ids[i])/2)
    
    return missing

ans_2 = solve_2(passes)
print(ans_2)
#Answer was 592