from math import floor

with open('inputs/input-01.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def solve1(lines):
    result = 0
    for num in lines:
        result += floor(int(num) / 3) - 2
    return result


def solve2(lines):
    result = 0
    for num in lines:
        while int(num) > 0:
            num = max(floor(int(num) / 3) - 2, 0)
            result += num
    return result


if __name__ == "__main__" or __name__ == 'aoc.core':
    print(solve1(input_))
    print(solve2(input_))

