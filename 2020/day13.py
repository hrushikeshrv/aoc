"""
Problem 13 - https://adventofcode.com/2020/day/13

Part 1 -
    Given a list of bus departure times and the earliest time you can depart, return the number of minutes you will have to wait 

Part 2 -
    Given the same list of bus departure times, find the time at which they each leave with some given offset
"""

# Set up the input
with open('input-13122020.txt', 'r') as file:
    data = file.readlines()

earliest_departure = int(data[0])
bus_departures = [int(x) for x in data[1].split(',') if x != 'x']


# Solution to part 1
def solve_1(departure, bus_departures):
    min_time = None
    min_id = -1
    
    for time in bus_departures:
        i = 1
        while time * i < departure:
            i += 1
        
        if min_time is None or time * i - departure < min_time:
            min_id = time
            min_time = time * i - departure
    
    return min_id * min_time


ans_1 = solve_1(earliest_departure, bus_departures)
print(ans_1)


# Answer was 3035

# Solution to part 2
def solve_2():
    raise NotImplementedError
