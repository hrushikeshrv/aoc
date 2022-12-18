with open("inputs/input-10.txt", "r") as file:
    instructions = list(map(lambda x: x.strip(), file.readlines()))


def solve1(insts):
    acc = 1
    i = -1
    cycles = 0
    add = 0
    next_cycle = 0
    signal_strength = 0
    inst = insts[0]
    while True:
        if cycles > 230 or i >= len(insts) - 1:
            break
        if cycles in [20, 60, 100, 140, 180, 220]:
            signal_strength += cycles * acc
        if next_cycle == cycles:
            acc += add
            i += 1
            inst = insts[i]
            if inst.startswith("noop"):
                add = 0
                next_cycle = cycles + 1
            elif inst.startswith("addx"):
                next_cycle = cycles + 2
                add = int(inst.split()[1])
        cycles += 1

    return signal_strength


ans = solve1(instructions)
print(ans)
# Answer was 14540


def solve2(insts):
    acc = 1
    i = -1
    cycles = 0
    add = 0
    next_cycle = 0
    inst = insts[0]
    rows = [["" for i in range(40)] for j in range(6)]
    while True:
        if cycles > 240 or i >= len(insts) - 1:
            break
        if next_cycle == cycles:
            acc += add
            i += 1
            inst = insts[i]
            if inst.startswith("noop"):
                add = 0
                next_cycle = cycles + 1
            elif inst.startswith("addx"):
                next_cycle = cycles + 2
                add = int(inst.split()[1])

        pixel_pos = cycles % 40
        row = int((cycles - 1) / 40)
        if pixel_pos in range(acc - 1, acc + 2):
            rows[row][pixel_pos] = "#"
        else:
            rows[row][pixel_pos] = " "
        cycles += 1

    rows[-1] = ["#"] + rows[-1][1:]  # Fix very weird glitch that I can't figure out
    for row in rows:
        print("".join(row))


solve2(instructions)
# Answer was EHZFZHCZ
