with open('input-07.txt', 'r') as file:
    commands = list(map(lambda x: x.strip(), file.readlines()))

dirs = {}
def calc_size(dir_name, cmds):
    dir_stack = [dir_name]
    
    size = 0
    for i in range(len(cmds)):
        cmd = cmds[i]

        if cmd == '$ cd ..':
            dir_stack.pop()
            if not dir_stack:
                break
        elif cmd.startswith('$ cd'):
            child_name = cmd.split()[-1]
            dir_stack.append(child_name)
            calc_size(dir_stack[-1], cmds[i+1:])
        
        if cmd[0].isnumeric():
            size += int(cmd.split()[0])

    while dir_name in dirs:
        # TODO - Very hacky, assumes directories with duplicate names have to have different sizes
        #       But I've run out of time now.
        if dirs[dir_name] != size:
            dir_name += '0'
        else:
            break
    dirs[dir_name] = size
    return size


def solve1(cmds):
    calc_size('/', cmds[1:])
    print(dirs)
    size = 0
    for s in dirs.values():
        if s <= 100000:
            size += s
    return size

ans = solve1(commands)
print(ans)
# Answer was 1749646


def solve2():
    space_needed = dirs['/'] - 40000000
    min_dir = dirs['/']
    for d in dirs.values():
        if d < min_dir and d > space_needed:
            min_dir = d
    return min_dir

ans = solve2()
print(ans)
# Answer was 1498966
