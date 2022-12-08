with open('input-08.txt', 'r') as file:
    trees = list(map(lambda x: x.strip(), file.readlines()))


def solve1(trees):
    rows = len(trees)
    cols = len(trees[0])
    visible = set()
    for i in range(rows):
        visible.add((i, 0))
        visible.add((i, cols-1))
    for i in range(cols):
        visible.add((0, i))
        visible.add((rows-1, i))
    
    for r in range(rows):
        highest_yet = 0
        for c in range(cols):
            tree = int(trees[r][c])
            if tree > highest_yet:
                visible.add((r, c))
                highest_yet = tree
    
    for r in range(rows):
        highest_yet = 0
        for c in range(cols-1, -1, -1):
            tree = int(trees[r][c])
            if tree > highest_yet:
                visible.add((r, c))
                highest_yet = tree
    
    for c in range(cols):
        highest_yet = 0
        for r in range(rows):
            tree = int(trees[r][c])
            if tree > highest_yet:
                visible.add((r, c))
                highest_yet = tree
    
    for c in range(cols):
        highest_yet = 0
        for r in range(rows-1, -1, -1):
            tree = int(trees[r][c])
            if tree > highest_yet:
                visible.add((r, c))
                highest_yet = tree
    
    return len(visible)

ans = solve1(trees)
print(ans)
# Answer was 1798

def viewing_distance(row, col, n_rows, n_cols):
    if row == 0 or row == n_rows-1 or col == 0 or col == n_cols-1:
        return 0

    height = int(trees[row][col])
    left = 0
    c = col
    while c >= 0:
        c -= 1
        if c < 0:
            break
        left += 1
        if int(trees[row][c]) >= height:
            break

    right = 0
    c = col
    while c < n_cols:
        c += 1
        if c >= n_cols:
            break
        right += 1
        if int(trees[row][c]) >= height:
            break
    
    up = 0
    r = row
    while r >= 0:
        r -= 1
        if r < 0:
            break
        up += 1
        if int(trees[r][col]) >= height:
            break
    
    down = 0
    r = row
    while r < n_rows:
        r += 1
        if r >= n_rows:
            break
        down += 1
        if int(trees[r][col]) >= height:
            break
    
    return up * right * down * left


def solve2(trees):
    max_view = 0
    rows = len(trees)
    cols = len(trees[0])
    for r in range(rows):
        for c in range(cols):
            dist = viewing_distance(r, c, rows, cols)
            if dist > max_view:
                max_view = dist
    return max_view

ans = solve2(trees)
print(ans)
# Answer was 259308
