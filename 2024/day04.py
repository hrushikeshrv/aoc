with open('inputs/input-04.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def get_slice(lines, row, col):
    n_rows = len(lines)
    n_cols = len(lines[0])
    res = ['', '', '', '']
    if col + 4 <= n_cols:
        res[0] = lines[row][col:col+4]
    if row + 4 <= n_rows:
        res[1] = lines[row][col] + lines[row+1][col] + lines[row+2][col] + lines[row+3][col]
    if col + 4 <= n_cols and row + 4 <= n_rows:
        res[2] = lines[row][col] + lines[row+1][col+1] + lines[row+2][col+2] + lines[row+3][col+3]
    if col - 3 >= 0 and row + 4 <= n_rows:
        res[3] = lines[row][col] + lines[row+1][col-1] + lines[row+2][col-2] + lines[row+3][col-3]

    return res


def solve1(lines):
    n = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            res = get_slice(lines, row, col)
            for r in res:
                if r == 'XMAS' or r == 'SAMX':
                    n += 1
    return n


def solve2(lines):
    n_rows = len(lines)
    n_cols = len(lines[0])
    n = 0
    for row in range(1, n_rows-1):
        for col in range(1, n_cols-1):
            d1 = lines[row-1][col-1] + lines[row][col] + lines[row+1][col+1]
            d2 = lines[row+1][col-1] + lines[row][col] + lines[row-1][col+1]
            # print(f'Row {row}, Col {col}: {d1}, {d2}')
            if (d1 == 'MAS' or d1 == 'SAM') and (d2 == 'MAS' or d2 == 'SAM'):
                n += 1
    return n


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

