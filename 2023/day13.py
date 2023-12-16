with open("inputs/input-13.txt") as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def get_grid_score(grid):
    for row in range(len(grid)):
        i = 0
        match = False
        while row - i >= 0 and row + i + 1 < len(grid):
            if grid[row - i] != grid[row + i + 1]:
                match = False
                break
            else:
                match = True
            i += 1
        if match:
            return 100 * (row + 1)

    for col in range(len(grid[0])):
        i = 0
        match = False
        while col - i >= 0 and col + i + 1 < len(grid[0]):
            if any(grid[j][col - i] != grid[j][col + i + 1] for j in range(len(grid))):
                match = False
                break
            else:
                match = True
            i += 1
        if match:
            return col + 1


def solve1(lines):
    grids = []
    curr_grid = []
    for line in lines:
        if not line:
            if len(curr_grid) > 0:
                grids.append(curr_grid)
                curr_grid = []
        else:
            curr_grid.append(line)
    grids.append(curr_grid)

    score = 0
    for grid in grids:
        score += get_grid_score(grid)
    return score


def transpose(grid):
    return list(map("".join, zip(*grid)))


def count_differences(list1, list2):
    diff = 0
    for line1, line2 in zip(list1, list2):
        diff += sum(a != b for a, b in zip(line1, line2))
        if diff > 1:
            break
    return diff


def find_reflections(grid):
    height = len(grid)
    perfect = imperfect = 0

    for size in range(1, height // 2 + 1):
        top = grid[:size]
        bottom = grid[size : 2 * size]
        diff = count_differences(top, bottom[::-1])

        if diff == 0:
            perfect = size
        if diff == 1:
            imperfect = size

        if perfect and imperfect:
            break

        top = grid[height - 2 * size : height - size]
        bottom = grid[height - size :]
        diff = count_differences(top, bottom[::-1])

        if diff == 0:
            perfect = height - size
        if diff == 1:
            imperfect = height - size

        if perfect and imperfect:
            break
    return perfect, imperfect


def solve2(lines):
    grids = []
    curr_grid = []
    for line in lines:
        if not line:
            if len(curr_grid) > 0:
                grids.append(curr_grid)
                curr_grid = []
        else:
            curr_grid.append(line)
    grids.append(curr_grid)

    score = 0
    for grid in grids:
        score += 100 * find_reflections(grid)[1]
        score += find_reflections(transpose(grid))[1]
    return score


if __name__ == "__main__":
    print(solve1(input_))
    print(solve2(input_))
