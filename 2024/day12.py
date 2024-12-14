with open('inputs/tests/input-12.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def get_neighbors(lines, row, col, char):
    n_rows = len(lines)
    n_cols = len(lines[0])
    neighbors = []
    if 0 < row and (row - 1, col) and lines[row-1][col] == char:
        neighbors.append((row - 1, col))
    if row < n_rows - 1 and (row + 1, col) and lines[row+1][col] == char:
        neighbors.append((row + 1, col))
    if 0 < col and (row, col - 1) and lines[row][col-1] == char:
        neighbors.append((row, col - 1))
    if col < n_cols - 1 and (row, col + 1) and lines[row][col+1] == char:
        neighbors.append((row, col + 1))
    return neighbors


def get_perimeter_area(lines, row, col, char, cache={}, visited=set()):
    neighbors = get_neighbors(lines, row, col, char)
    if len(neighbors) == 0:
        return 4, 1, visited
    perimeter = 4
    area = 1
    visited.add((row, col))
    for n_row, n_col in neighbors:
        perimeter -= 1
        if (n_row, n_col) not in visited:
            visited.add((n_row, n_col))
            res = get_perimeter_area(lines, n_row, n_col, char, cache, visited)
            perimeter += res[0]
            area += res[1]
            visited = res[2]
    return perimeter, area, visited


def solve1(lines):
    processed = set()
    ans = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if (row, col) not in processed:
                perimeter, area, processed = get_perimeter_area(lines, row, col, lines[row][col])
                ans += perimeter * area
    return ans


def solve2(lines):
    pass


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

