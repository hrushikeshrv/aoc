with open('inputs/input-05.txt', 'r') as file:
    instructions = file.readlines()
    c = 0
    for i in range(len(instructions)):
        if not instructions[i].startswith('move'):
            c += 1
    instructions = list(map(lambda x: x.strip(), instructions[c:]))

# Set up input manually
stacks = [
    ['J', 'Z', 'G', 'V', 'T', 'D','B', 'N'][::-1],
    ['F', 'P', 'W', 'D', 'M', 'R', 'S'][::-1],
    ['Z', 'S', 'R', 'C', 'V'][::-1],
    ['G', 'H', 'P', 'Z', 'J', 'T', 'R'][::-1],
    ['F', 'Q', 'Z', 'D', 'N', 'J', 'C', 'T'][::-1],
    ['M', 'F', 'S', 'G', 'W', 'P', 'V', 'N'][::-1],
    ['Q', 'P', 'B', 'V', 'C', 'G'][::-1],
    ['N', 'P', 'B', 'Z'][::-1],
    ['J', 'P', 'W'][::-1]
]

def solve1(inst):
    for line in inst:
        line = line.split()
        n = int(line[1])
        start = int(line[3])-1
        end = int(line[5])-1
        for i in range(n):
            stacks[end].append(stacks[start].pop())
    
    return ''.join([i[-1] for i in stacks])

ans = solve1(instructions)
print(ans)
# Answer was GFTNRBZPF

# Set up input manually
stacks = [
    ['J', 'Z', 'G', 'V', 'T', 'D','B', 'N'][::-1],
    ['F', 'P', 'W', 'D', 'M', 'R', 'S'][::-1],
    ['Z', 'S', 'R', 'C', 'V'][::-1],
    ['G', 'H', 'P', 'Z', 'J', 'T', 'R'][::-1],
    ['F', 'Q', 'Z', 'D', 'N', 'J', 'C', 'T'][::-1],
    ['M', 'F', 'S', 'G', 'W', 'P', 'V', 'N'][::-1],
    ['Q', 'P', 'B', 'V', 'C', 'G'][::-1],
    ['N', 'P', 'B', 'Z'][::-1],
    ['J', 'P', 'W'][::-1]
]

def solve2(inst):
    for line in inst:
        # print('Stacks are now')
        # for s in stacks:
        #     print(s)

        line = line.split()
        n = int(line[1])
        start = int(line[3])-1
        end = int(line[5])-1
        stacks[end].extend(stacks[start][-n:])
        stacks[start] = stacks[start][:-n]
    
    return ''.join([i[-1] for i in stacks])

ans = solve2(instructions)
print(ans)
# Answer was VRQWPDSGP