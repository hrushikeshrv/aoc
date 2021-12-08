"""
Problem 7 - https://adventofcode.com/2021/day/7

Part 1 -
    Given a list of numbers L, find a number m such that the sum of absolute differences between m and L[i]
    is minimum

Part 2 -
    Given the same list of numbers L, find a number m such that the sum of |L[i] - m| * (|L[i] - m| + 1) / 2 for all i
    is minimum
"""

# Set up the input
with open('input-07.txt', 'r') as file:
    pos = sorted(list(map(lambda x: int(x), file.readline().split(','))))


# Solution to part 1
def solve_1(positions):
    l = len(positions)
    if l % 2 == 0:
        median = positions[l//2 - 1]/2 + positions[l//2]/2
    else:
        median = positions[l//2]
    fuel = 0
    for p in positions:
        fuel += abs(p-median)
    return fuel


ans = solve_1(pos)
print(ans)
# Answer was 348664


# Define helper functions
def fuel_cost(x1, x2):
    """
    Returns the amount of fuel needed to move a crab submarine from x1 to x2
    """
    d = abs(x1 - x2)
    return (d*(d+1))/2


def weighted_average(numbers):
    """
    Returns the weighted average of the numbers array weighted by the frequency of the numbers
    :param numbers:List[int]
    :return: float
    """
    num_dict = {}
    for n in numbers:
        num_dict[n] = num_dict.get(n, 0) + 1
    weighted_sum = 0
    for n in num_dict:
        weighted_sum += n * num_dict[n]
    return weighted_sum/len(numbers)


# Solution to part 2
def solve_2(positions):
    w_a = weighted_average(positions)
    w_a = int(w_a)      # Take the floor of the number if it is a float
    
    fuel = 0
    for p in positions:
        fuel += fuel_cost(p, w_a)
    return fuel


ans = solve_2(pos)
print(ans)
# Answer was 100220525
