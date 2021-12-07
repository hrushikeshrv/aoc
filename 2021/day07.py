"""

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
