with open('inputs/input-14.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

lines = [x.split('->') for x in lines]
lines = [[list(map(lambda pair: int(pair), pair.split(','))) for pair in row] for row in lines]


def build_map(rocks):
    min_x = min(min(map(lambda y: y[0], x)) for x in rocks)
    max_y = max(max(map(lambda y: y[1], x)) for x in rocks) + 1
    # Normalize coordinates
    max_x = 0
    for row in rocks:
        for i in range(len(row)):
            row[i][0] -= min_x
            if row[i][0] > max_x:
                max_x = row[i][0]
    cave_map = [['.' for col in range(max_x+1)] for row in range(max_y)]
    for row in rocks:
        for i in range(len(row)-1):
            start_x, start_y = row[i]
            end_x, end_y = row[i+1]
            
            if start_y == end_y:
                if start_x < end_x:
                    for j in range(start_x, end_x + 1):
                        cave_map[start_y][j] = '#'
                else:
                    for j in range(end_x, start_x + 1):
                        cave_map[start_y][j] = '#'
            else:
                if start_y < end_y:
                    for j in range(start_y, end_y):
                        cave_map[j][start_x] = '#'
                else:
                    for j in range(end_y, start_y):
                        cave_map[j][start_x] = '#'
    return cave_map, 500 - min_x
    
    
cave_map, origin_x = build_map(lines)


def solve1(cave_map, origin_x):
    max_y = len(cave_map)
    max_x = len(cave_map[0])
    grain_on_screen = True
    n_grains = 0
    while grain_on_screen:
        grain = [origin_x, 0]
        n_grains += 1
        while True:
            if grain[0] < 0 or grain[0] >= max_x:
                grain_on_screen = False
                break
            if grain[1] >= max_y:
                grain_on_screen = False
                break
                
            if cave_map[grain[1]+1][grain[0]] == '.':
                grain[1] += 1
            elif cave_map[grain[1]+1][grain[0]-1] == '.':
                grain[1] += 1
                grain[0] -= 1
            elif cave_map[grain[1]+1][grain[0]+1] == '.':
                grain[1] += 1
                grain[0] += 1
            else:
                cave_map[grain[1]][grain[0]] = 'o'
                break
    
    return n_grains-1


print(solve1(cave_map, origin_x))
# Answer was 1298

with open('inputs/input-14.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

lines = [x.split('->') for x in lines]
lines = [[list(map(lambda pair: int(pair), pair.split(','))) for pair in row] for row in lines]

cave_map, origin_x = build_map(lines)


def clear_lines(n):
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def solve2(cave_map, origin_x):
    max_y = len(cave_map)
    max_x = len(cave_map[0])
    for i in range(len(cave_map)):
        cave_map[i] = ['.' for j in range(max_y)] + cave_map[i] + ['.' for j in range(max_y)]
    cave_map.append(['.' for i in range(len(cave_map[0]))])
    cave_map.append(['#' for i in range(len(cave_map[0]))])
    origin_x += max_y
    source_blocked = False
    n_grains = 0
    while not source_blocked:
        grain = [origin_x, 0]
        n_grains += 1
        while True:
            if cave_map[grain[1] + 1][grain[0]] == '.':
                grain[1] += 1
            elif cave_map[grain[1] + 1][grain[0] - 1] == '.':
                grain[1] += 1
                grain[0] -= 1
            elif cave_map[grain[1] + 1][grain[0] + 1] == '.':
                grain[1] += 1
                grain[0] += 1
            else:
                cave_map[grain[1]][grain[0]] = 'o'
                if grain == [origin_x, 0]:
                    source_blocked = True
                break
    return n_grains


print(solve2(cave_map, origin_x))
# Answer was 25585
