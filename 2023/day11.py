from itertools import combinations

with open("inputs/input-11.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def get_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def solve1(lines):
    n_rows = len(lines)
    n_cols = len(lines[0])

    expand_cols = []
    for col in range(n_cols):
        if all(l[col] == "." for l in lines):
            expand_cols.append(col)
    expand_rows = []
    for row in range(n_rows):
        if all(col == "." for col in lines[row]):
            expand_rows.append(row)
    for i, col in enumerate(expand_cols):
        for row in range(n_rows):
            lines[row] = lines[row][: col + i] + "." + lines[row][col + i :]
    n_cols = len(lines[0])

    for i, row in enumerate(expand_rows):
        lines.insert(row + i, "".join(["." for i in range(n_cols)]))
    n_rows = len(lines)

    galaxies = []
    for row in range(n_rows):
        for col in range(n_cols):
            if lines[row][col] == "#":
                galaxies.append((row, col))

    galaxy_pairs = list(combinations(galaxies, 2))
    lengths = 0
    for galaxy1, galaxy2 in galaxy_pairs:
        lengths += get_distance(galaxy1, galaxy2)
    return lengths


def solve2(lines):
    n_rows = len(lines)
    n_cols = len(lines[0])
    galaxies = []
    for row in range(n_rows):
        for col in range(n_cols):
            if lines[row][col] == "#":
                galaxies.append([row, col])

    for col in reversed(range(n_cols)):
        if all(l[col] == "." for l in lines):
            for i in range(len(galaxies)):
                if galaxies[i][1] > col:
                    galaxies[i][1] += 999999

    for row in reversed(range(n_rows)):
        if all(col == "." for col in lines[row]):
            for i in range(len(galaxies)):
                if galaxies[i][0] > row:
                    galaxies[i][0] += 999999

    galaxy_pairs = list(combinations(galaxies, 2))
    lengths = 0
    for galaxy1, galaxy2 in galaxy_pairs:
        lengths += get_distance(galaxy1, galaxy2)
    return lengths


if __name__ == "__main__":
    # print(solve1(lines))
    print(solve2(lines))
