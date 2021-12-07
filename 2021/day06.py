"""
Problem 6 - https://adventofcode.com/2021/day/6

Part 1 -
    Given a list of numbers and rules to manipulate the list. Find the length of
    the list after 80 iterations

Part 2 -
    With the same setup, find the length of the list after 256 iterations.
"""

# Set up the input
with open('input-06.txt', 'r') as file:
    ages = list(map(lambda x: int(x), file.readline().split(',')))


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
# Answer was 393019


# Define helper functions
def get_total_fish(days):
    """
    Returns a list of 7 elements containing the number of fish
    that would be present after "days" days
    """
    countdowns = {
        0: 1,
        1: 0, 
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    fish_count = []
    for i in range(days+1):
        todays_fish = 0
        new_fish = countdowns[0]
        for key in range(8):
            todays_fish += countdowns[key]
            countdowns[key] = countdowns[key+1]
        countdowns[6] += new_fish
        countdowns[8] = new_fish
        if i >= days-7:
            fish_count.append(todays_fish)
    
    return fish_count


# Solution to part 2
def solve_2(ages_list, days):
    fish_population = get_total_fish(days)
    total_fish = 0
    for age in ages_list:
        total_fish += fish_population[-age]
    return total_fish


ans = solve_2(ages, 256)
print(ans)
# Answer was 1757714216975
