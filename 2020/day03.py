"""
Problem 3 - https://adventofcode.com/2020/day/3

Part 1 -
    Given an infinite grid of '.' and '#', follow a certain path through the grid and count how many '#'s you encounter

Part 2 -
    Same as part 1 with multiple paths to follow and count
"""

#Set up the input
with open('input-03122020.txt', 'r') as file:
    s = file.readlines()
#Remove the \n at the end of each line
s = [x[:-1] for x in s]
print(s[:10])

#Solution to part 1
def solve_1(l):
    tree_count = 0
    row_ind = 0
    
    for row in l[1:]:
        row_ind += 3
        if row_ind >= len(row):
            row_ind -= len(row)
        
        if row[row_ind] == '#':
            tree_count += 1
    
    return tree_count

ans_1 = solve_1(s)
print(ans_1)
#Answer was 254

#Solution to part 2
def solve_2(l, right, down):
    tree_count = 0
    row_ind = 0

    for row in l[down::down]:
        row_ind += right
        if row_ind >= len(row):
            row_ind -= len(row)
        if row[row_ind] == '#':
            tree_count += 1
    
    return tree_count

cases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ans_2 = 1
for i, j in cases:
    ans_2 *= solve_2(s, i, j)
print(ans_2)
#Answer was 1666768320