"""
Problem 14 - https://adventofcode.com/2020/day/14

Part 1 -
    Given instructions on how a computer writes numbers to memory using a bitmask, find the sum of the numbers stored in memory

Part 2 -
    Apply the bitmask to the locations instead of the numbers being stored and return the sum of the numbers stored in memory
"""

#Set up the input
with open('input-14122020.txt', 'r') as file:
    inst = file.readlines()

instructions = [x[:-1] for x in inst]

#Define helper functions
def binary_enum(iterator, key = 'X'):
    diff_list = []
    diff_list.append(''.join(iterator).replace(key, '0'))
    for l in reversed(range(len(iterator))):
        if iterator[l] == key:
            curr_len = len(diff_list)
            for diff in range(curr_len):
                _ = [x for x in diff_list[diff]]
                _[l] = '1'
                diff_list.append(''.join(_))
    return diff_list


#Solution to part 1
def solve_1(instructions):
    mask = ''
    loc_dict = {}
    for i in instructions:
        if i.startswith('mask'):
            mask = i.split('=')[1].strip()
            continue
        #Get the location to store in
        loc = i.split(']')[0].split('[')[1]
        #Get the number to store
        num = bin(int(i.split('=')[1].strip())).replace('0b', '')
        
        #Pre-pad the number to be the same length as the mask
        while len(num) < len(mask):
            num = '0' + num
        #Strings are immutable so represent the number as a list instead
        num_l = [x for x in num]

        for j in range(len(mask)):
            if mask[j] != 'X':
                num_l[j] = mask[j]
        
        loc_dict[loc] = int(''.join(num_l), 2)

    return sum(loc_dict.values())

ans_1 = solve_1(instructions)
print(ans_1)
#Answer was 13727901897109

#Solution to part 2
def solve_2(instructions):
    loc_dict = {}
    mask = ''
    for i in instructions:
        if i.startswith('mask'):
            mask = i.split('=')[1].strip()
            continue
        #This time convert the location to binary instead of the number since the mask modifies the loc
        loc = bin(int(i.split(']')[0].split('[')[1])).replace('0b', '')
        num = int(i.split('=')[1].strip())

        #Pre-pad the location till it's the same length as the mask
        while len(loc) < len(mask):
            loc = '0' + loc
        
        #Strings are immutable so represent the location as a list instead
        loc_l = [x for x in loc]

        for j in range(len(mask)):
            if mask[j] == '1':
                loc_l[j] = '1'
            elif mask[j] == 'X':
                loc_l[j] = 'X'
        
        locations = binary_enum(loc_l)

        for loc in locations:
            loc_dict[loc] = num
    
    return sum(loc_dict.values())

ans_2 = solve_2(instructions)
print(ans_2)
#Answer was 5579916171823