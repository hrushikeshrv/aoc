"""
Problem 9 - https://adventofcode.com/2020/day/9

Part 1 -
    Given a list of numbers in which the next number has to be the sum of any 2 numbers from the previous 25 numbers, find the first number that violates this rule

Part 2 -
    Find a contiguous set of numbers (of any length greater than 1) which sum to the violating number from part 1 and return the sum of the min and max number in that set of numbers
"""

# Set up the input
with open('inputs/input-09122020.txt', 'r') as file:
    nums = file.readlines()


# Define helper functions
def is_valid(num, prev):
    flag = False
    for i in prev:
        for j in prev:
            # Slice off the last character since it is a newline character
            if int(i[:-1]) + int(j[:-1]) == int(num[:-1]):
                flag = True
    return flag


# Solution to part 1
def solve_1(nums):
    for num in range(25, len(nums)):
        if not is_valid(nums[num], nums[num - 25:num]):
            # Slice off the last character since it is a newline character
            return int(nums[num][:-1])


ans_1 = solve_1(nums)
print(ans_1)


# Answer was 556543474

# Solution to part 2
def solve_2(nums, prev):
    for i in range(2, len(nums)):
        for j in range(i, len(nums)):
            s = nums[j - i:j]
            l = [int(x[:-1]) for x in s]
            if sum(l) == prev:
                return min(l) + max(l)


ans_2 = solve_2(nums, ans_1)
print(ans_2)
# Answer was 7609632
