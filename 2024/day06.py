from copy import deepcopy

with open('inputs/input-06.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))
    start_pos = [0, 0]
    for row, line in enumerate(input_):
        for col, char in enumerate(line):
            if char in ['>', '<', '^', 'v']:
                start_pos = [row, col]
                break


def step(lines, row, col, direction):
    if direction == '^':
        if row <= 0:
            return None, None, None
        if lines[row - 1][col] != '#':
            row -= 1
        else:
            direction = '>'
    if direction == '>':
        if col >= len(lines[row]) - 1:
            return None, None, None
        if lines[row][col + 1] != '#':
            col += 1
        else:
            direction = 'v'
    if direction == '<':
        if col <= 0:
            return None, None, None
        if lines[row][col - 1] != '#':
            col -= 1
        else:
            direction = '^'
    if direction == 'v':
        if row >= len(lines) - 1:
            return None, None, None
        if lines[row + 1][col] != '#':
            row += 1
        else:
            direction = '<'
    return row, col, direction


def solve1(lines, start):
    row = start[0]
    col = start[1]
    visited = {(row, col)}
    direction = lines[row][col]
    while True:
        row, col, direction = step(lines, row, col, direction)
        if row is None or col is None:
            break
        visited.add((row, col))
    return len(visited)


def solve2(lines, start):
    ans = 0
    row = start[0]
    col = start[1]
    visited = {(row, col)}
    direction = lines[row][col]
    while True:
        row, col, direction = step(lines, row, col, direction)
        if row is None or col is None:
            break
        visited.add((row, col))

    for i, j in visited:
        if i == start[0] and j == start[1]:
            continue
        row = start[0]
        col = start[1]
        direction = lines[row][col]
        visited = {(row, col, direction)}
        new_grid = deepcopy(lines)
        _ = [x for x in new_grid[i]]
        _[j] = '#'
        new_grid[i] = ''.join(_)
        while True:
            row, col, direction = step(new_grid, row, col, direction)
            if row is None or col is None:
                # We exited the grid
                break
            if (row, col, direction) in visited:
                ans += 1
                break
            visited.add((row, col, direction))
    return ans


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_, start_pos))
    print(solve2(input_, start_pos))

