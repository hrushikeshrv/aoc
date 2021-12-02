# Set up the input
with open('input-02.txt', 'r') as file:
    lines = list(map(lambda x: (x.split()[0], int(x.split()[1])), file.readlines()))


# Solution to part 1
def solve_1(moves):
    x, y = 0, 0
    for move in moves:
        if move[0] == 'forward':
            x += move[1]
        elif move[0] == 'down':
            y += move[1]
        elif move[0] == 'up':
            y -= move[1]
    return x*y


ans = solve_1(lines)
print(ans)
# Answer was 2147104


# Solution to part 2
def solve_2(moves):
    return


ans = solve_2(lines)
print(ans)
