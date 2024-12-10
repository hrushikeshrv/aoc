with open('inputs/input-10.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def get_neighbours(row, col, n_rows, n_cols):
    n = []
    if 0 < row:
        n.append((row - 1, col))
    if 0 < col:
        n.append((row, col - 1))
    if row < n_rows - 1:
        n.append((row + 1, col))
    if col < n_cols - 1:
        n.append((row, col + 1))
    return n


def find_trail_peaks(lines, row, col, n_rows, n_cols, cache={}, visited=set()):
    if lines[row][col] == '9':
        return {(row, col)}
    if (row, col) in cache:
        return cache[(row, col)]
    visited.add((row, col))
    n = get_neighbours(row, col, n_rows, n_cols)
    ans = set()
    for new_row, new_col in n:
        if int(lines[new_row][new_col]) == int(lines[row][col]) + 1:
            for x in find_trail_peaks(lines, new_row, new_col, n_rows, n_cols, cache, visited):
                ans.add(x)
    cache[(row, col)] = ans
    return ans


def find_trail_heads(lines, row, col, n_rows, n_cols, cache={}):
    if lines[row][col] == '9':
        return 1
    if (row, col) in cache:
        return cache[(row, col)]
    n = get_neighbours(row, col, n_rows, n_cols)
    ans = 0
    for new_row, new_col in n:
        if int(lines[new_row][new_col]) == 1 + int(lines[row][col]):
            ans += find_trail_heads(lines, new_row, new_col, n_rows, n_cols, cache)
    cache[(row, col)] = ans
    return ans


def solve1(lines):
    starts = set()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '0':
                starts.add((row, col))
    scores = 0
    for row, col in starts:
        peaks = find_trail_peaks(lines, row, col, len(lines), len(lines[0]))
        scores += len(peaks)
    return scores


def solve2(lines):
    starts = set()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '0':
                starts.add((row, col))
    scores = 0
    for row, col in starts:
        peaks = find_trail_heads(lines, row, col, len(lines), len(lines[0]))
        scores += peaks
    return scores


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

