"""
Problem 3 - https://adventofcode.com/2021/day/3

Part 1 -
    Given a list of readings and rules on how to generate two numbers from those readings, return the product of
    the generated numbers

Part 2 -
    Given the same list of readings and rules on how to filter the list to get two numbers, return the
    product of the two numbers
"""

# Set up the input
with open('input-03.txt', 'r') as file:
    lines = file.readlines()


# Solution to part 1
def solve_1(readings):
    gamma = ''
    epsilon = ''
    size = len(readings[0])-1
    
    for i in range(size):
        zero, one = 0, 0
        for reading in readings:
            if reading[i] == '0':
                zero += 1
            elif reading[i] == '1':
                one += 1
        if zero > one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)


ans = solve_1(lines)
print(ans)
# Answer was 3813416


# Define helper functions
def get_common_bit(readings, index):
    """
    Returns the most common bit at index index in list readings
    :param readings: List:str
    :param index: int
    :return:
    """
    zeros, ones = 0, 0
    for reading in readings:
        if reading[index] == '0':
            zeros += 1
        elif reading[index] == '1':
            ones += 1
    if zeros > ones:
        return '0'
    elif ones > zeros:
        return '1'
    else:
        return '-1'


# Solution to part 2
def solve_2(readings):
    o2_candidates = readings[:]
    i = 0
    while len(o2_candidates) > 1:
        common = get_common_bit(o2_candidates, i)
        if common != '-1':
            o2_candidates = [x for x in o2_candidates if x[i] == common]
        else:
            o2_candidates = [x for x in o2_candidates if x[i] == '1']
        i += 1
    
    co2_candidates = readings[:]
    i = 0
    while len(co2_candidates) > 1:
        common = get_common_bit(co2_candidates, i)
        if common != '-1':
            co2_candidates = [x for x in co2_candidates if x[i] != common]
        else:
            co2_candidates = [x for x in co2_candidates if x[i] == '0']
        i += 1
    return int(o2_candidates[0], 2) * int(co2_candidates[0], 2)


ans = solve_2(lines)
print(ans)
# Answer was 2990784
