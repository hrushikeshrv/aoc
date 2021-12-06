"""
Problem 6 - https://adventofcode.com/2021/day/6
"""

# Set up the input
with open('input-06.txt', 'r') as file:
    ages = list(map(lambda x: int(x), file.readline().split(',')))

with open('input-06-test.txt', 'r') as file:
    test_ages = list(map(lambda x: int(x), file.readline().split(',')))


# Define helper functions
def update_ages(ages_list):
    new_fish = []
    for age in ages_list:
        if age == 0:
            age += 6
            new_fish.append(8)
        else:
            age -= 1
    return ages_list + new_fish


# Solution to part 1
def solve_1(ages_list):
    for i in range(80):
        new_fish = []
        for j in range(len(ages_list)):
            if ages_list[j] == 0:
                ages_list[j] += 6
                new_fish.append(8)
            else:
                ages_list[j] -= 1
        ages_list = ages_list + new_fish
    return len(ages_list)


ans = solve_1(ages)
print(ans)


# Solution to part 2
def solve_2(ages_list):
    for i in range(256):
        new_fish = []
        for j in range(len(ages_list)):
            if ages_list[j] == 0:
                ages_list[j] += 6
                new_fish.append(8)
            else:
                ages_list[j] -= 1
        ages_list = ages_list + new_fish
    return len(ages_list)


ans = solve_2(test_ages)
print(ans)
