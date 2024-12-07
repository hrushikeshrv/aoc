with open('inputs/input-07.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def evaluate(a, b, op):
    if op == '+':
        return a + b
    if op == '*':
        return a * b
    if op == '||':
        return int(str(a) + str(b))


def calculate(nums, target, operations=('*', '+')):
    if len(nums) == 1:
        return nums[0] == target
    if len(nums) == 2:
        return any(evaluate(nums[0], nums[1], op) == target for op in operations)
    return any(
        calculate(
            [evaluate(nums[0], nums[1], op)] + nums[2:],
            target,
            operations
        ) for op in operations
    )


def solve1(lines):
    ans = 0
    for line in lines:
        _ = line.split(':')
        target = int(_[0])
        numbers = list(map(lambda x: int(x), _[1].strip().split(' ')))
        if calculate(numbers, target):
            ans += int(target)
    return ans


def solve2(lines):
    ans = 0
    for line in lines:
        _ = line.split(':')
        target = int(_[0])
        numbers = list(map(lambda x: int(x), _[1].strip().split(' ')))
        if calculate(numbers, target, ('+', '*', '||')):
            ans += int(target)
    return ans


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))
