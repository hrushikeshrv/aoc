import sys
sys.setrecursionlimit(10000)

with open('inputs/input-12.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))
    
# lines = [
#     'aabqponm',
#     'abcryxxl',
#     'accszExk',
#     'acctuvwj',
#     'abdefghi',
# ]

n_rows = len(lines)
n_cols = len(lines[0])
MAX_DIST = n_rows * n_cols + 1


def find_path(heights, curr_dist, row, col, visited):
    candidates = [(row, col-1), (row+1, col), (row, col+1), (row-1, col)]
    neighbours = []
    for s in candidates:
        if 0 <= s[0] < n_rows and 0 <= s[1] < n_cols:
            if ord(heights[row][col]) - ord(heights[s[0]][s[1]]) <= 1:
                neighbours.append(s)
    
    # if all(s in visited for s in neighbours):
    #     return
    relaxed = False
    for s in neighbours:
        if 0 <= s[0] < n_rows and 0 <= s[1] < n_cols:
            if ord(heights[row][col]) - ord(heights[s[0]][s[1]]) <= 1:
                dist = visited.get(s, MAX_DIST)
                if dist > 1 + curr_dist:
                    relaxed = True
                    visited[s] = 1 + curr_dist
    if not relaxed:
        return
    
    for s in neighbours:
        find_path(heights, curr_dist + 1, s[0], s[1], visited)
    

visited = {}
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
    visited[(end_row, end_col)] = 0
    find_path(heights, 0, end_row, end_col, visited)
    return visited[(start_row, start_col)]


ans = solve1(lines)
print(ans)
# Answer was 462


def solve2(heights):
    min_dist = MAX_DIST
    for s in visited:
        if heights[s[0]][s[1]] == 'a':
            if visited[s] < min_dist:
                min_dist = visited[s]
    return min_dist


ans = solve2(lines)
print(ans)
# Answer was 451
