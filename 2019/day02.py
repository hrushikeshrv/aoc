with open('inputs/input-02.txt') as file:
    input_ = list(map(lambda x: x.strip(), file.readlines()))


def solve1(lines):
    program = lines[0].split(',')
    program[1] = '12'
    program[2] = '2'
    for i in range(0, len(program), 4):
        if program[i] == '1':
            program[int(program[i+3])] = str(int(program[int(program[i+1])]) + int(program[int(program[i+2])]))
        elif program[i] == '2':
            program[int(program[i+3])] = str(int(program[int(program[i+1])]) * int(program[int(program[i+2])]))
        elif program[i] == '99':
            break
    return program[0]


def solve2(lines):
    for a in range(100):
        for b in range(100):
            program = lines[0].split(',')
            program[1] = str(a)
            program[2] = str(b)
            for i in range(0, len(program), 4):
                if program[i] == '1':
                    program[int(program[i + 3])] = str(
                        int(program[int(program[i + 1])]) + int(program[int(program[i + 2])]))
                elif program[i] == '2':
                    program[int(program[i + 3])] = str(
                        int(program[int(program[i + 1])]) * int(program[int(program[i + 2])]))
                elif program[i] == '99':
                    break
            if program[0] == '19690720':
                return 100 * a + b
    return 0


if __name__ == "__main__" or __name__ == "aoc.core":
    print(solve1(input_))
    print(solve2(input_))

