with open('inputs/input-13.txt') as file:
    _ = list(map(lambda x: x.strip(), file.readlines()))
    input_ = []
    cache = []
    for l in _:
        if not l:
            if cache:
                input_.append(cache)
                cache = []
        else:
            res = l.split(':')[1].strip().split(', ')
            cache.append(int(res[0][2:]))
            cache.append(int(res[1][2:]))
    input_.append(cache)


def solve1(lines):
    ans = 0
    for p in lines:
        D = p[0] * p[3] - p[1] * p[2]
        if D != 0:
            D_x = p[4] * p[3] - p[5] * p[2]
            D_y = p[0] * p[5] - p[1] * p[4]
            if (3 * (D_x / D) + (D_y / D)).is_integer():
                ans += 3 * (D_x / D) + (D_y / D)
        else:
            if p[0] / p[1] == p[2] / p[3] and p[0] / p[1] == p[4] / p[5]:
                # Infinitely many solutions, find the first one with both x and y integers
                i = 0
                while True:
                    res = (p[4] - p[0] * i) / p[2]
                    if res.is_integer():
                        ans += 3 * i + res
                        break
                    i += 1
    return int(ans)


def solve2(lines):
    for p in lines:
        p[4] += 10000000000000
        p[5] += 10000000000000
    return solve1(lines)


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

