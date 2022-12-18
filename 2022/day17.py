with open("inputs/input-17.txt", "r") as file:
    airflow = file.readline().strip()

# airflow = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

rocks = [
    [[2, 0], [3, 0], [4, 0], [5, 0]],
    [[3, 0], [2, 1], [3, 1], [4, 1], [3, 2]],
    [[4, 0], [4, 1], [4, 2], [3, 2], [2, 2]],
    [[2, 0], [2, 1], [2, 2], [2, 3]],
    [[2, 0], [2, 1], [3, 0], [3, 1]],
]

cave = [["-" for _ in range(7)]]


def add_new_rock_at_top(rock_type):
    cave.append(["." for _ in range(7)])
    cave.append(["." for _ in range(7)])
    cave.append(["." for _ in range(7)])

    new_rows = {
        0: 1,
        1: 3,
        2: 3,
        3: 4,
        4: 2,
    }
    for _ in range(new_rows[rock_type]):
        cave.append(["." for _1 in range(7)])

    row_coord = len(cave) - 1
    rock_coords = []
    for rock_x, rock_y in rocks[rock_type]:
        cave[row_coord - rock_y][rock_x] = "@"
        rock_coords.append([rock_x, row_coord - rock_y])

    return rock_coords


def print_cave():
    for row in cave[::-1]:
        print("|", "".join(row), "|")
    print("\n")


def move_rock(rock_coords, air_direction):
    if air_direction == "<":
        # print(f'Jet of air pushes rock left - ')
        for x, y in rock_coords:
            if x == 0:
                break
            if [x - 1, y] not in rock_coords and cave[y][x - 1] != ".":
                break
        else:
            for x, y in rock_coords:
                cave[y][x] = "."
            for i in range(len(rock_coords)):
                rock_coords[i][0] -= 1
            for x, y in rock_coords:
                cave[y][x] = "#"
        # print_cave()
    elif air_direction == ">":
        # print(f'Jet of air pushes rock right -')
        for x, y in rock_coords:
            if x == 6:
                break
            if [x + 1, y] not in rock_coords and cave[y][x + 1] != ".":
                break
        else:
            for x, y in rock_coords:
                cave[y][x] = "."
            for i in range(len(rock_coords)):
                rock_coords[i][0] += 1
            for x, y in rock_coords:
                cave[y][x] = "#"
        # print_cave()

    for x, y in rock_coords:
        if [x, y - 1] not in rock_coords and cave[y - 1][x] != ".":
            # print(f'Rock comes to rest -')
            # print_cave()
            return False

    for x, y in rock_coords:
        cave[y][x] = "."
    for i in range(len(rock_coords)):
        rock_coords[i][1] -= 1
    for x, y in rock_coords:
        cave[y][x] = "#"
    # print(f'Rock falls 1 unit -')
    if "#" not in cave[-1]:
        cave.pop()
    # print_cave()
    return True


def get_height():
    for i, row in enumerate(cave):
        if "#" not in cave[i]:
            return len(cave) - i - 1
    return len(cave)


i = 0
for c in range(2022):
    coords = add_new_rock_at_top(c % 5)
    # print_cave()
    while move_rock(coords, airflow[i % len(airflow)]):
        i += 1
    i += 1


print(get_height())
# Answer was 3168


cave = [["-" for _ in range(7)]]

height_deltas = []
prev_height = get_height()


cycle_found = False
cycle_length = 0
cycle_offset = 0
cycle_height = 0
for offset in range(1000):
    if cycle_found:
        break
    max_pattern_size = (len(height_deltas) - offset) // 2
    for window_size in range(1, max_pattern_size):
        if cycle_found:
            break
        window = height_deltas[offset : offset + window_size]
        if all(
            height_deltas[j : j + window_size] == window
            for j in range(offset + window_size, len(height_deltas), window_size)
        ):
            print(
                f"Cycle detected of length {window_size} starting from offset {offset}"
            )
            cycle_found = True
            cycle_length = window_size
            cycle_offset = offset
            cycle_height = sum(window)

total_height = sum(height_deltas[:cycle_offset]) + (
    cycle_height * (1000000000000 - cycle_offset) // cycle_length
)
total_height += sum(height_deltas[: (1000000000000 - cycle_offset) % cycle_length])
print(total_height)
