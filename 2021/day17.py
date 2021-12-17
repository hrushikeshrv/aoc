"""
Problem 17
"""

x_range = range(277, 319)
y_range = range(53, 93)  # Not taking negatives for the first part

test_x_range = range(20, 31)
test_y_range = range(5, 11)


# Solution to part 1
def solve_1(target_y_range, max_y):
    vy = 0
    max_vel = 0
    candidates = []
    while vy <= max_y:
        vy += 1
        n = 1
        y = n * vy + n * (n - 1) / 2
        while True:
            if y > max_y:
                break
            if y in target_y_range:
                max_vel = vy
                candidates.append((max_vel, n))
                print(f'Found a velocity - {vy}. y is {y} at time {n}')
            n += 1
            y = n * vy + n * (n - 1) / 2
    while candidates:
        vel, n = candidates.pop()
        # Find the correct value of n
        # Iterate over all x velocities from 1 to max_x
        # If we find a matching x velocity which results in x coord being in x_range, this y velocity is correct
        
    return max_vel * (max_vel + 1) / 2


ans = solve_1(test_y_range, 10)
print(ans)
