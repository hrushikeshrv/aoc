with open("inputs/input-13.txt", "r") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


lists = []
for l in lines:
    if not l:
        continue
    lists.append(eval(l))


def compare(left, right):
    i = 0
    while True:
        if len(left) <= i < len(right):
            return 1
        elif len(right) <= i < len(left):
            return 0
        elif i >= len(left) and i >= len(right):
            return None
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            elif right[i] < left[i]:
                return 0

        if isinstance(left[i], list) and isinstance(right[i], list):
            result = compare(left[i], right[i])
            if result is not None:
                return result

        if isinstance(left[i], list) and isinstance(right[i], int):
            result = compare(left[i], [right[i]])
            if result is not None:
                return result

        if isinstance(left[i], int) and isinstance(right[i], list):
            result = compare([left[i]], right[i])
            if result is not None:
                return result

        i += 1


def solve1(packets):
    correct_order = 0
    i = 0
    while i < len(packets) - 1:
        res = compare(packets[i], packets[i + 1])
        if res == 1:
            correct_order += i // 2 + 1
        i += 2
    return correct_order


print(solve1(lists))
# Answer was 5350


def solve2(packets):
    packets.append([[2]])
    packets.append([[6]])
    for i in range(len(packets)):
        for j in range(i + 1, len(packets)):
            if compare(packets[i], packets[j]) == 0:
                packets[i], packets[j] = packets[j], packets[i]

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


print(solve2(lists))
# Answer was 19570
