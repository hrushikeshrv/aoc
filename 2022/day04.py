with open("inputs/input-04.txt.", "r") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def solve1(lines):
    count = 0
    for line in lines:
        line = line.split(",")
        p1 = line[0].split("-")
        p2 = line[1].split("-")
        if int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]):
            count += 1
        elif int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1]):
            count += 1
    return count


ans = solve1(lines)
print(ans)


def solve2(lines):
    count = 0
    for line in lines:
        line = line.split(",")
        p1 = line[0].split("-")
        p2 = line[1].split("-")
        if int(p2[0]) <= int(p1[0]) <= int(p2[1]):
            count += 1
        elif int(p2[0]) <= int(p1[1]) <= int(p2[1]):
            count += 1
        elif int(p1[0]) <= int(p2[0]) <= int(p1[1]):
            count += 1
        elif int(p1[0]) <= int(p2[1]) <= int(p1[1]):
            count += 1
    return count


ans = solve2(lines)
print(ans)
