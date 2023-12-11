with open("inputs/input-10.txt") as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def get_neighbours(row, col, n_rows, n_cols, char):
    neighbours = []
    deltas = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": [],
    }
    for d_row, d_col in deltas[char]:
        if 0 <= row + d_row < n_rows and 0 <= col + d_col < n_cols:
            neighbours.append((row + d_row, col + d_col))
    return neighbours


def get_start_pipe(row, col, n_rows, n_cols, grid):
    points_north = False
    points_south = False
    points_east = False
    points_west = False
    if (
        0 <= row + 1 < n_rows
        and 0 <= col + 0 < n_cols
        and grid[row + 1][col] in ["|", "J", "L"]
    ):
        points_south = True
    if (
        0 <= row - 1 < n_rows
        and 0 <= col + 0 < n_cols
        and grid[row - 1][col] in ["|", "F", "7"]
    ):
        points_north = True
    if (
        0 <= row - 0 < n_rows
        and 0 <= col + 1 < n_cols
        and grid[row][col + 1] in ["-", "7", "J"]
    ):
        points_east = True
    if (
        0 <= row - 0 < n_rows
        and 0 <= col - 1 < n_cols
        and grid[row][col - 1] in ["-", "F", "L"]
    ):
        points_west = True

    if points_north and points_south:
        return "|"
    if points_east and points_west:
        return "-"
    if points_north and points_east:
        return "L"
    if points_north and points_west:
        return "J"
    if points_south and points_west:
        return "7"
    if points_south and points_east:
        return "F"


def solve1(lines):
    distances = [[None for i in range(len(lines[0]))] for j in range(len(lines))]
    start_idx = (0, 0)
    n_rows = len(lines)
    n_cols = len(lines[0])

    start_found = False
    for row in range(n_rows):
        for col in range(n_cols):
            if lines[row][col] == "S":
                start_idx = (row, col)
                lines[row] = (
                    lines[row][:col]
                    + get_start_pipe(row, col, n_rows, n_cols, lines)
                    + lines[row][col + 1 :]
                )
                start_found = True
                break
        if start_found:
            break

    distances[start_idx[0]][start_idx[1]] = 0
    q = [start_idx]
    while q:
        curr_node = q.pop()
        neighbours = get_neighbours(
            curr_node[0],
            curr_node[1],
            n_rows,
            n_cols,
            lines[curr_node[0]][curr_node[1]],
        )
        for neighbour in neighbours:
            if (
                distances[neighbour[0]][neighbour[1]] is None
                or distances[neighbour[0]][neighbour[1]]
                > distances[curr_node[0]][curr_node[1]] + 1
            ):
                q.append(neighbour)
                distances[neighbour[0]][neighbour[1]] = (
                    distances[curr_node[0]][curr_node[1]] + 1
                )

    for row in distances:
        for i, d in enumerate(row):
            if d is None:
                row[i] = 0
    return max(max(x) for x in distances)


def solve2(lines):
    distances = [[None for i in range(len(lines[0]))] for j in range(len(lines))]
    start_idx = (0, 0)
    n_rows = len(lines)
    n_cols = len(lines[0])

    start_found = False
    for row in range(n_rows):
        for col in range(n_cols):
            if lines[row][col] == "S":
                start_idx = (row, col)
                lines[row] = (
                    lines[row][:col]
                    + get_start_pipe(row, col, n_rows, n_cols, lines)
                    + lines[row][col + 1 :]
                )
                start_found = True
                break
        if start_found:
            break

    distances[start_idx[0]][start_idx[1]] = 0
    q = [start_idx]
    while q:
        curr_node = q.pop()
        neighbours = get_neighbours(
            curr_node[0],
            curr_node[1],
            n_rows,
            n_cols,
            lines[curr_node[0]][curr_node[1]],
        )
        for neighbour in neighbours:
            if (
                distances[neighbour[0]][neighbour[1]] is None
                or distances[neighbour[0]][neighbour[1]]
                > distances[curr_node[0]][curr_node[1]] + 1
            ):
                q.append(neighbour)
                distances[neighbour[0]][neighbour[1]] = (
                    distances[curr_node[0]][curr_node[1]] + 1
                )

    main_loop = set()
    for row in range(n_rows):
        for col in range(n_cols):
            if distances[row][col] is not None:
                main_loop.add((row, col))

    n_inside = 0
    for row in range(n_rows):
        is_inside = False
        for col in range(n_cols):
            if lines[row][col] in ["|", "L", "J"] and (row, col) in main_loop:
                is_inside = not is_inside
            elif is_inside and (row, col) not in main_loop:
                n_inside += 1
    return n_inside


if __name__ == "__main__":
    # Note, run parts 1 and 2 independently. If you run both part 1 and part 2
    # part 1 overwrite some data for part 2, and I don't care enough to fix it right now.
    # Uncomment whichever part you want to solve.
    # print(solve1(lines))
    print(solve2(lines))
