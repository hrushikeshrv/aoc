with open('inputs/input-12.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))
    
lines = [
    'aabqponm',
    'abcryxxl',
    'accszExk',
    'acctuvwj',
    'abdefghi',
]

n_rows = len(lines)
n_cols = len(lines[0])


def find_path(heights, path, end_row, end_col):
    # Caching and base case
    global n_rows, n_cols
    row, col = path[-1]
    if row == end_row and col == end_col:
        return 0
    
    # Find valid neighbours
    candidate_squares = []
    _ = [(row, col-1), (row+1, col), (row, col+1), (row-1, col)]
    for s in _:
        if 0 <= s[0] < n_rows and 0 <= s[1] < n_cols:
            if ord(heights[s[0]][s[1]]) - ord(heights[row][col]) <= 1:
                if s not in path:
                    candidate_squares.append(s)

    if not candidate_squares:
        return n_rows * n_cols + 100
    min_dist = n_rows * n_cols + 100
    for square in candidate_squares:
        path.append(square)
        dist = 1 + find_path(heights, path, end_row, end_col)
        if dist < min_dist:
            min_dist = dist
        path.pop()
    return min_dist


def solve1(heights: list[str]):
    start_row = 0
    start_col = 0
    end_row = 0
    end_col = 0
    i = 0
    while i < len(heights):
        if 'E' in heights[i]:
            end_row = i
            end_col = heights[i].index('E')
            heights[end_row] = heights[end_row][:end_col] + 'z' + heights[end_row][end_col+1:]
            break
        i += 1
    i = 0
    while i < len(heights):
        if 'S' in heights[i]:
            start_row = i
            start_col = heights[i].index('S')
            heights[start_row] = heights[start_row][:start_col] + 'a' + heights[start_row][start_col + 1:]
            break
        i += 1
    return find_path(heights, [(start_row, start_col)], end_row, end_col)


ans = solve1(lines)
print(ans)
