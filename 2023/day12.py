# Thanks to GitHub @mebeim for the walkthrough for this day
# https://github.com/mebeim/aoc/blob/master/2023/README.md#day-12---hot-springs

with open("inputs/input-12.txt") as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))

cache = {}


def place_parts(sequence, parts, curr_len=0):
    if (sequence, tuple(parts), curr_len) in cache:
        return cache[(sequence, tuple(parts), curr_len)]

    if not sequence:
        if len(parts) == 0 and curr_len == 0:
            return 1
        if len(parts) == 1 and curr_len == parts[0]:
            return 1
        return 0

    if len(parts) > 0 and curr_len > parts[0]:
        return 0
    if len(parts) == 0 and curr_len > 0:
        return 0

    char = sequence[0]
    count = 0
    if char == "#" or char == "?":
        count += place_parts(sequence[1:], parts, curr_len + 1)
    if char == "." or char == "?":
        if curr_len == 0:
            count += place_parts(sequence[1:], parts, 0)
        elif len(parts) > 0 and curr_len == parts[0]:
            count += place_parts(sequence[1:], parts[1:], 0)

    cache[(sequence, tuple(parts), curr_len)] = count
    return count


def solve1(lines):
    count = 0
    for line in lines:
        sequence = line.split()[0]
        parts = list(map(lambda x: int(x), line.split()[1].split(",")))
        count += place_parts(sequence, parts)
    return count


def solve2(lines):
    count = 0
    for line in lines:
        sequence = line.split()[0]
        sequence = "?".join([sequence] * 5)
        parts = list(map(lambda x: int(x), line.split()[1].split(",")))
        parts *= 5
        count += place_parts(sequence, parts)
    return count


if __name__ == "__main__":
    print(solve1(input_))
    print(solve2(input_))
