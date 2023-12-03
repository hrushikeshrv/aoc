with open("inputs/input-03.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def get_neighbours(row, col, n_rows, n_cols):
    neighbours = []
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for d_row, d_col in deltas:
        if 0 <= row + d_row < n_rows and 0 <= col + d_col < n_cols:
            neighbours.append((row + d_row, col + d_col))
    return neighbours


def get_number(number_map, row, col, n_cols, seen):
    if not number_map[row][col].isnumeric():
        seen.add((row, col))
        return 0
    if (row, col) in seen:
        return 0

    num = number_map[row][col]
    curr_col = col - 1
    while curr_col >= 0:
        if number_map[row][curr_col].isnumeric():
            seen.add((row, curr_col))
            num = number_map[row][curr_col] + num
        else:
            break
        curr_col -= 1

    curr_col = col + 1
    while curr_col < n_cols:
        if number_map[row][curr_col].isnumeric():
            seen.add((row, curr_col))
            num += number_map[row][curr_col]
        else:
            break
        curr_col += 1
    return int(num)


def solve1(number_map):
    seen = set()
    n_rows = len(number_map)
    n_cols = len(number_map[0])

    part_sum = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if not number_map[row][col].isnumeric() and number_map[row][col] != ".":
                neighbours = get_neighbours(row, col, n_rows, n_cols)
                for neighbour in neighbours:
                    part_sum += get_number(
                        number_map, neighbour[0], neighbour[1], n_cols, seen
                    )
    return part_sum


def solve2(number_map):
    n_rows = len(number_map)
    n_cols = len(number_map[0])

    gear_ratio = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if number_map[row][col] == "*":
                neighbours = get_neighbours(row, col, n_rows, n_cols)
                adj_numbers = []
                seen = set()
                for neighbour in neighbours:
                    _ = get_number(number_map, neighbour[0], neighbour[1], n_cols, seen)
                    if _ > 0:
                        adj_numbers.append(_)
                if len(adj_numbers) == 2:
                    gear_ratio += adj_numbers[0] * adj_numbers[1]
    return gear_ratio


if __name__ == "__main__":
    print(solve1(lines))
    print(solve2(lines))
