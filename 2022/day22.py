with open('inputs/input-22.txt', 'r') as file:
    lines = list(map(lambda x: x[:-1], file.readlines()))

lines = [
    '        ...#',
    '        .#..',
    '        #...',
    '        ....',
    '...#.......#',
    '........#...',
    '..#....#....',
    '..........#.',
    '        ...#....',
    '        .....#..',
    '        .#......',
    '        ......#.',
    '',
    '10R5L5R10L4R5L5',
]

moves = lines.pop()
lines.pop()

facings = {
    (1, 0): {
        'L': (0, -1),
        'R': (0, 1)
    },
    (0, 1): {
        'L': (1, 0),
        'R': (-1, 0)
    },
    (-1, 0): {
        'L': (0, 1),
        'R': (0, 1)
    },
    (0, -1): {
        'L': (-1, 0),
        'R': (1, 0)
    }
}

facing_val = {
    (1, 0): 0,
    (0, 1): 1,
    (-1, 0): 2,
    (0, -1): 3
}


def wrap(grid, x, y, facing_x, facing_y):
    if facing_y == 0:
        if facing_x > 0:
            for i in range(len(grid[y])):
                if grid[y][i] != ' ':
                    if grid[y][i] == '#':
                        return x, y
                    return i, y
        else:
            for i in range(len(grid[y])-1, -1, -1):
                if grid[y][i] != ' ':
                    if grid[y][i] == '#':
                        return x, y
                    return i, y
    else:
        if facing_y > 0:
            for i in range(len(grid)):
                if x >= len(grid[i]):
                    continue
                if grid[i][x] != ' ':
                    if grid[i][x] == '#':
                        return x, y
                    return x, i
        else:
            for i in range(len(grid)-1, -1, -1):
                if x >= len(grid[i]):
                    continue
                if grid[i][x] != ' ':
                    if grid[i][x] == '#':
                        return x, y
                    return x, i


def move(grid, x, y, facing, n_steps, first_move):
    j = 0
    while j < n_steps:
        new_x = x + facing[0]
        new_y = y + facing[1]
        if not first_move and (new_y >= len(grid) or new_x >= len(grid[new_y]) or grid[new_y][new_x] == ' ' or new_x < 0 or new_y < 0):
            # print(f'{new_x, new_y} is out of the map ({len(grid[y])}), ({len(grid)}). Wrapping to ', end='')
            x, y = wrap(grid, x, y, *facing)
            # print(x, y)
        elif grid[new_y][new_x] == '#':
            break
        else:
            x = new_x
            y = new_y
        j += 1
        # print(f'At {x, y}')
    return x, y


def solve1(grid, moves):
    x, y = [0, 0]
    facing = (1, 0)
    n_steps = ''
    first_move = True
    for i in range(len(moves)):
        if moves[i].isalpha():
            n_steps = int(n_steps)
            # Move n_steps steps
            print(f'Moving {facing} {n_steps} steps ({n_steps}{moves[i]})')
            x, y = move(grid, x, y, facing, n_steps, first_move)
            first_move = False
            
            facing = facings[facing][moves[i]]
            n_steps = ''
        else:
            n_steps += moves[i]
    print(f'Moving {facing} {n_steps} steps')
    x, y = move(grid, x, y, facing, int(n_steps), 1)
    return 1000 * (y + 1) + 4 * (x + 1) + facing_val[facing]


print(solve1(lines, moves))
# print(wrap(lines, 15, 11, 0, 1))