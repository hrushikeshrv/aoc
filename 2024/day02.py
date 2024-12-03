with open('inputs/input-02.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def is_safe(report):
    increasing = True
    if int(report[0]) > int(report[1]):
        increasing = False
    for i in range(1, len(report)):
        diff = abs(int(report[i]) - int(report[i-1]))
        if diff < 1 or diff > 3:
            return False
        if increasing:
            if int(report[i]) < int(report[i-1]):
                return False
        else:
            if int(report[i]) > int(report[i-1]):
                return False
    return True


def solve1(lines):
    safe = 0
    for line in lines:
        if is_safe(line.split(' ')):
            safe += 1
    return safe


def solve2(lines):
    safe = 0
    for line in lines:
        line = line.split(' ')
        for i in range(len(line)):
            line_popped = line[:]
            line_popped.pop(i)
            if is_safe(line_popped):
                safe += 1
                break
    return safe


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

