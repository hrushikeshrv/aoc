with open('input-09.txt', 'r') as file:
    moves = list(map(lambda x: x.strip(), file.readlines()))


def move(tail, head, direction):
    if direction == 'U':
        head[1] += 1
        if tail[0] == head[0]:
            if head[1] - tail[1] > 1:
                tail[1] += 1
        elif abs(head[1] - tail[1]) > 1:
            tail[1] += 1
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1
    
    elif direction == 'R':
        head[0] += 1
        if tail[1] == head[1]:
            if head[0] - tail[0] > 1:
                tail[0] += 1
        elif abs(head[0] - tail[0]) > 1:
            tail[0] += 1
            if tail[1] > head[1]:
                tail[1] -= 1
            elif tail[1] < head[1]:
                tail[1] += 1
    
    elif direction == 'D':
        head[1] -= 1
        if tail[0] == head[0]:
            if tail[1] - head[1] > 1:
                tail[1] -= 1
        elif abs(head[1] - tail[1]) > 1:
            tail[1] -= 1
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1
    
    elif direction == 'L':
        head[0] -= 1
        if tail[1] == head[1]:
            if tail[0] - head[0] > 1:
                tail[0] -= 1
        elif abs(head[0] - tail[0]) > 1:
            tail[0] -= 1
            if tail[1] > head[1]:
                tail[1] -= 1
            elif tail[1] < head[1]:
                tail[1] += 1
    return tail, head


def solve1(lines):
    tail = [0, 0]
    head = [0, 0]
    visited = {(0, 0)}
    for m in lines:
        direction = m.split()[0]
        count = int(m.split()[1])
        for i in range(count):
            tail, head = move(tail, head, direction)
            visited.add(tuple(tail))
    return len(visited)


ans = solve1(moves)
print(ans)
# Answer was 6339


def follow(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    move_map = {
        (0, 0): tail,
        (1, 0): tail,
        (1, 1): tail,
        (0, 1): tail,
        (-1, 1): tail,
        (-1, 0): tail,
        (-1, -1): tail,
        (0, -1): tail,
        (1, -1): tail,
        (0, 2): [tail[0], tail[1]+1],
        (1, 2): [tail[0]+1, tail[1]+1],
        (2, 2): [tail[0]+1, tail[1]+1],
        (2, 1): [tail[0]+1, tail[1]+1],
        (2, 0): [tail[0]+1, tail[1]],
        (2, -1): [tail[0]+1, tail[1]-1],
        (2, -2): [tail[0]+1, tail[1]-1],
        (1, -2): [tail[0]+1, tail[1]-1],
        (0, -2): [tail[0], tail[1]-1],
        (-1, -2): [tail[0]-1, tail[1]-1],
        (-2, -2): [tail[0]-1, tail[1]-1],
        (-2, -1): [tail[0]-1, tail[1]-1],
        (-2, 0): [tail[0]-1, tail[1]],
        (-2, 1): [tail[0]-1, tail[1]+1],
        (-2, 2): [tail[0]-1, tail[1]+1],
        (-1, 2): [tail[0]-1, tail[1]+1],
    }
    return move_map[(x_diff, y_diff)]


def print_rope(knots):
    l = [['.' for i in range(15)] for j in range(15)]
    for i in range(len(knots)):
        k = knots[i]
        l[k[1]][k[0]] = str(i)
    for row in l[::-1]:
        print(''.join(row))
    print('\n\n')


def solve2(lines):
    knots = [[0, 0] for i in range(10)]
    visited = {(0, 0)}
    for m in lines:
        direction = m.split()[0]
        count = int(m.split()[1])
        for i in range(count):
            knots[1], knots[0] = move(knots[1], knots[0], direction)
            for j in range(2, len(knots)):
                knots[j] = follow(knots[j-1], knots[j])
            visited.add(tuple(knots[-1]))
    return len(visited)


ans = solve2(moves)
print(ans)
# Answer was 2541
