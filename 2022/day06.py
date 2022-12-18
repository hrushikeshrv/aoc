with open("inputs/input-06.txt", "r") as file:
    line = file.read().strip()


def solve1(line):
    for i in range(4, len(line)):
        if len(set(line[i - 4 : i])) == 4:
            return i


ans = solve1(line)
print(ans)


def solve2(line):
    for i in range(14, len(line)):
        if len(set(line[i - 14 : i])) == 14:
            return i


ans = solve2(line)
print(ans)
