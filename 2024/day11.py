with open('inputs/input-11.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def expand_stone(stone, times, cache={}):
    if times == 0:
        return 1
    if (stone, times) in cache:
        return cache[(stone, times)]
    if stone == '0':
        ans = expand_stone('1', times - 1, cache)
        cache[(stone, times)] = ans
        return ans
    if len(stone) % 2 == 0:
        ans = (
            expand_stone(str(int(stone[:len(stone) // 2])), times - 1, cache)
            + expand_stone(str(int(stone[len(stone) // 2:])), times - 1, cache)
        )
        cache[(stone, times)] = ans
        return ans
    ans = expand_stone(str(int(stone) * 2024), times - 1, cache)
    cache[(stone, times)] = ans
    return ans


def solve1(lines):
    ans = 0
    for stone in lines[0].split(' '):
        ans += expand_stone(stone, 25)
    return ans


def solve2(lines):
    ans = 0
    for stone in lines[0].split(' '):
        ans += expand_stone(stone, 75)
    return ans


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

