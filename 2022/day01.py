# Set up the input
with open("inputs/input-01.txt.", "r") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def solve_1(cals):
    max_cals = 0
    _ = 0
    for line in cals:
        if not line:
            if _ > max_cals:
                max_cals = _
            _ = 0
        else:
            _ += int(line)
    return max_cals


ans = solve_1(lines)
print(ans)
# Answer was 69177


def solve_2(cals):
    cals_sorted = []
    _ = 0
    for line in cals:
        if not line:
            cals_sorted.append(_)
            _ = 0
        else:
            _ += int(line)
    cals_sorted.sort()
    return sum(cals_sorted[-3:])


ans = solve_2(lines)
print(ans)
# Answer was 207456
