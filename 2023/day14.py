with open('inputs/tests/input-14.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def solve1(lines):
    n_rows = len(lines)
    n_cols = len(lines[0])

    load = 0
    for col in range(n_cols):
        column_load = 0
        multiplier = n_rows
        for row in range(n_rows):
            if lines[row][col] == 'O':
                column_load += multiplier
                multiplier -= 1
            elif lines[row][col] == '#':
                multiplier = n_rows - row - 1
        load += column_load
    return load


def solve2(lines):
    pass


if __name__ == "__main__":
    print(solve1(input_))
    print(solve2(input_))

