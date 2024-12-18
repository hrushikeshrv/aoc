with open('inputs/tests/input-15.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))
    grid_ = []
    moves_ = ''
    idx = 0
    start_ = (0, 0)
    for i, l in enumerate(input_):
        grid_.append([x for x in l])
        for j, char in enumerate(l):
            if char == '@':
                start_ = (i, j)
        if l.startswith('########') and i > 1:
            idx = i+1
            break
    for i in range(idx+1, len(input_)):
        moves_ += input_[i].strip()

n_rows = len(grid_)
n_cols = len(grid_[0])


def clear_lines(n: int) -> None:
    """
    Clears the last n lines printed so we can print there again

    :param n: The number of lines to clear
    """
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def solve1(grid, moves, start):
    row, col = start
    for move in moves:
        if move == '<':
            index = col - 1
            for i_ in range(index, -1, -1):
                if grid[row][i_] == '.':
                    index = i_
                    break
                if grid[row][i_] == '#':
                    index = -1
                    break
            if index > -1:
                for i_ in range(index, col):
                    grid[row][i_] = grid[row][i_ + 1]
                grid[row][col] = '.'
                col -= 1
        if move == '>':
            index = col + 1
            for i_ in range(index, n_cols):
                if grid[row][i_] == '.':
                    index = i_
                    break
                if grid[row][i_] == '#':
                    index = n_cols + 1
                    break
            if index < n_cols:
                for i_ in range(index, col, -1):
                    grid[row][i_] = grid[row][i_ - 1]
                grid[row][col] = '.'
                col += 1
        if move == '^':
            index = row - 1
            for i_ in range(index, -1, -1):
                if grid[i_][col] == '.':
                    index = i_
                    break
                if grid[i_][col] == '#':
                    index = -1
                    break
            if index > -1:
                for i_ in range(index, row):
                    grid_[i_][col] = grid[i_ + 1][col]
                grid[row][col] = '.'
                row -= 1
        if move == 'v':
            index = row + 1
            for i_ in range(row + 1, n_rows):
                if grid[i_][col] == '.':
                    index = i_
                    break
                if grid[i_][col] == '#':
                    index = n_rows + 1
                    break
            if index < n_rows:
                for i_ in range(index, row, -1):
                    grid[i_][col] = grid[i_ - 1][col]
                grid[row][col] = '.'
                row += 1
    # for r in grid:
    #     print(''.join(r))
    ans = 0
    for i_, r in enumerate(grid):
        for j, c in enumerate(r):
            if grid[i_][j] == 'O':
                ans += 100 * i_ + j
    return ans


def solve2(grid, moves, start):
    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            if grid[i][j] == 'O':
                grid[i][j] = ']'
                grid[i].insert(j, '[')
            elif grid[i][j] != '@':
                grid[i].insert(j, grid[i][j])
            elif grid[i][j] == '@':
                grid[i].insert(j+1, '.')
            j += 2
    for row in grid:
        print(''.join(row))


if __name__ == "__main__" or __name__ == "aoc.core":
    # print(solve1(grid_, moves_, start_))
    print(solve2(grid_, moves_, start_))

