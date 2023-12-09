with open("inputs/input-09.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def get_next_value(nums):
    num_stack = [
        nums,
    ]
    while True:
        _ = []
        for i in range(len(num_stack[-1]) - 1):
            _.append(num_stack[-1][i + 1] - num_stack[-1][i])
        num_stack.append(_)
        if all(x == 0 for x in num_stack[-1]):
            break
    val = 0
    for stack in num_stack:
        val += stack[-1]
    return val


def get_prev_value(nums):
    num_stack = [
        nums,
    ]
    while True:
        _ = []
        for i in range(len(num_stack[-1]) - 1):
            _.append(num_stack[-1][i + 1] - num_stack[-1][i])
        num_stack.append(_)
        if all(x == 0 for x in num_stack[-1]):
            break
    val = 0
    for stack in num_stack[::-1]:
        val = stack[0] - val
    return val


def solve1(lines):
    for i in range(len(lines)):
        lines[i] = list(map(lambda x: int(x), lines[i].split()))
    ans = 0
    for line in lines:
        ans += get_next_value(line)
    return ans


def solve2(lines):
    for i in range(len(lines)):
        lines[i] = list(map(lambda x: int(x), lines[i].split()))
    ans = 0
    for line in lines:
        ans += get_prev_value(line)
    return ans


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
