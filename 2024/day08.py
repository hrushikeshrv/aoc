with open('inputs/input-08.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def get_antinodes(loc1, loc2, n_rows, n_cols, cont=False):
    row_diff = loc1[0] - loc2[0]
    col_diff = loc1[1] - loc2[1]
    n1 = [loc1[0] + row_diff, loc1[1] + col_diff]
    n2 = [loc2[0] - row_diff, loc2[1] - col_diff]
    ans = []
    while 0 <= n1[0] < n_rows and 0 <= n1[1] < n_cols:
        ans.append(n1.copy())
        n1[0] += row_diff
        n1[1] += col_diff
        if not cont:
            break
    while 0 <= n2[0] < n_rows and 0 <= n2[1] < n_cols:
        ans.append(n2.copy())
        n2[0] -= row_diff
        n2[1] -= col_diff
        if not cont:
            break
    return ans


def solve1(lines):
    locations = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != '.':
                if char not in locations:
                    locations[char] = []
                locations[char].append((row, col))
    ans = 0
    antinode_locations = set()
    for key in locations:
        for i in range(len(locations[key])):
            for j in range(i+1, len(locations[key])):
                res = get_antinodes(locations[key][i], locations[key][j], len(lines), len(lines[0]))
                for loc in res:
                    if tuple(loc) not in antinode_locations:
                        antinode_locations.add(tuple(loc))
                        ans += 1
    return ans


def solve2(lines):
    locations = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != '.':
                if char not in locations:
                    locations[char] = []
                locations[char].append((row, col))
    antinode_locations = set()
    for loc in locations:
        for antinode in locations[loc]:
            antinode_locations.add(antinode)
    for key in locations:
        for i in range(len(locations[key])):
            for j in range(i + 1, len(locations[key])):
                res = get_antinodes(locations[key][i], locations[key][j], len(lines), len(lines[0]), cont=True)
                for loc in res:
                    if tuple(loc) not in antinode_locations:
                        antinode_locations.add(tuple(loc))
    return len(antinode_locations)


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))
