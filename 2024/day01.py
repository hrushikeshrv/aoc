with open('inputs/input-01.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))
    left_ = []
    right_ = []
    for l in input_:
        _ = l.strip().split(" ")
        left_.append(_[0])
        right_.append(_[-1])


def solve1(left, right):
    ans = 0
    for x, y in zip(list(sorted(left)), list(sorted(right))):
        ans += abs(int(x)-int(y))
    return ans

def count(num, l):
    c = 0
    for i in l:
        if i == num:
            c += 1
    return c


def solve2(left, right):
    ans = 0
    for x, y in zip(left, right):
        ans += int(x) * count(x, right)
    return ans


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(left_, right_))
    print(solve2(left_, right_))

