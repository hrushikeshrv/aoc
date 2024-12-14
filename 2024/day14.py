from PIL import Image

with open('inputs/input-14.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))

x_dim = 101
y_dim = 103


def get_robot_pos(x, y, x_vel, y_vel, n):
    visited = set()
    for i in range(n):
        if (x, y) in visited:
            return get_robot_pos(x, y, x_vel, y_vel, n % i)
        visited.add((x, y))
        x += x_vel
        y += y_vel
        if x >= x_dim:
            x -= x_dim
        if y >= y_dim:
            y -= y_dim
        if x < 0:
            x += x_dim
        if y < 0:
            y += y_dim
    return x, y


def solve1(lines):
    positions = []
    for line in lines:
        pos, vel = line.split(' ')
        x, y = tuple(map(int, pos[2:].split(',')))
        x_vel, y_vel = tuple(map(int, vel[2:].split(',')))
        positions.append(get_robot_pos(x, y, x_vel, y_vel, 100))

    ans = 1
    grid_sums = [0, 0, 0, 0]
    for x, y in positions:
        if x < x_dim // 2:
            if y < y_dim // 2:
                grid_sums[0] += 1
            elif y > y_dim // 2:
                grid_sums[2] += 1
        elif x > x_dim // 2:
            if y < y_dim // 2:
                grid_sums[1] += 1
            elif y > y_dim // 2:
                grid_sums[3] += 1
    for s in grid_sums:
        ans *= s
    return ans


def save_grid(grid, name):
    # Save this grid as a 101x103 image for inspecting visually
    img = Image.new("L", (x_dim, y_dim))
    pixels = img.load()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            pixels[col, row] = 0 if grid[row][col] == ' ' else 255
    img.save(f"inputs/tests/14/{name}.png")
    print(f'Saved {name}.png')


def get_subgrid_idx(x, y, grid_dimension=25):
    x_id = x // grid_dimension
    y_id = y // grid_dimension
    return (y_dim // grid_dimension) * y_id + x_id


def solve2(lines):
    data = []
    for line in lines:
        pos, vel = line.split(' ')
        x, y = tuple(map(int, pos[2:].split(',')))
        x_vel, y_vel = tuple(map(int, vel[2:].split(',')))
        data.append([x, y, x_vel, y_vel])
    for i in range(x_dim * y_dim):
        grid_dimension = 25
        threshold = 200
        grid = [[' ' for x in range(x_dim)] for y in range(y_dim)]
        subgrid_counts = [0 for x in range(x_dim * y_dim // grid_dimension + 1)]
        for d in data:
            d[0] += d[2]
            d[1] += d[3]
            if d[0] >= x_dim:
                d[0] -= x_dim
            if d[1] >= y_dim:
                d[1] -= y_dim
            if d[0] < 0:
                d[0] += x_dim
            if d[1] < 0:
                d[1] += y_dim
            subgrid_counts[get_subgrid_idx(d[0], d[1], grid_dimension)] += 1
            if isinstance(grid[d[1]][d[0]], str):
                grid[d[1]][d[0]] = 1
            else:
                grid[d[1]][d[0]] += 1
        for subgrid in subgrid_counts:
            if subgrid > threshold:
                save_grid(grid, i)
                break
        if i % 100 == 0:
            print(f'Processed {i} steps')


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

