with open('inputs/input-22.txt', 'r') as file:
    lines = list(map(lambda x: x[:-1], file.readlines()))

# lines = [
#     '        ...#',
#     '        .#..',
#     '        #...',
#     '        ....',
#     '...#.......#',
#     '........#...',
#     '..#....#....',
#     '..........#.',
#     '        ...#....',
#     '        .....#..',
#     '        .#......',
#     '        ......#.',
#     '',
#     '10R5L5R10L4R5L5',
# ]

moves = lines.pop()
lines.pop()
grid = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != ' ':
            grid[(x, y)] = lines[y][x]

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
        'R': (0, -1)
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


def move(grid, x, y, facing, n_steps):
    while (x, y) not in grid:
        x, y = x + facing[0], y + facing[1]
    for j in range(int(n_steps)):
        new_x = x + facing[0]
        new_y = y + facing[1]
        if (new_x, new_y) in grid:
            if grid[(new_x, new_y)] == '#':
                break
            x, y = new_x, new_y
        else:
            while (new_x-facing[0], new_y-facing[1]) in grid:
                new_x -= facing[0]
                new_y -= facing[1]
            if grid[(new_x, new_y)] != '#':
                x, y = new_x, new_y
    return x, y

def solve1(grid, moves):
    x, y = 0, 0
    facing = (1, 0)
    n_steps = ''
    for i in range(len(moves)):
        if moves[i].isalpha():
            x, y = move(grid, x, y, facing, n_steps)
            
            facing = facings[facing][moves[i]]
            n_steps = ''
        else:
            n_steps += moves[i]
    x, y = move(grid, x, y, facing, int(n_steps))
    return 1000 * (y + 1) + 4 * (x + 1) + [(1, 0), (0, 1), (-1, 0), (0, -1)].index(facing)


print(solve1(grid, moves))
