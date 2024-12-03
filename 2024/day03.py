import re

with open('inputs/input-03.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


mul_re = re.compile(r'(mul\(\d+,\d+\))')
mul_re_2 = re.compile(r'(mul\(\d+,\d+\))|(do\(\)|don\'t\(\))')


def solve1(lines):
    ans = 0
    for line in lines:
        match = mul_re.findall(line)
        for group in match:
            if group is not None:
                _ = group[4:].split(',')
                ans += int(_[0]) * int(_[1][:-1])
    return ans


def solve2(lines):
    ans = 0
    enabled = True
    for line in lines:
        match = mul_re_2.findall(line)
        for group in match:
            if group is None:
                continue
            if enabled:
                if group[0]:
                    _ = group[0][4:].split(',')
                    ans += int(_[0]) * int(_[1][:-1])
                if group[1] == "don't()":
                    enabled = False
            else:
                if group[1] == "do()":
                    enabled = True
    return ans


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

