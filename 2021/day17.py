"""
Problem 17
"""

x_range = range(277, 319)
y_range = range(52, 92)  # Not taking negatives for the first part

test_x_range = range(20, 31)
test_y_range = range(4, 10)


# Solution to part 1
def solve_1(target_y_range, max_y):
    vy = 0
    found_max_vel = False
    while True:
        if found_max_vel:
            break
        vy += 1
        n = 1
        y = n * vy + n * (n - 1) / 2
        # print(f'y currently for vy = {vy} and n = {n} is {y}')
        while y not in target_y_range:
            if y > max_y:
                found_max_vel = True
                break
            n += 1
            y = n * vy + n * (n - 1) / 2
    vy -= 1
    return vy * (vy + 1) / 2


ans = solve_1(y_range, 92)
print(ans)
