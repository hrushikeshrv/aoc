with open('inputs/input-21.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

# lines = [
#     'root: pppw + sjmn',
#     'dbpl: 5',
#     'cczh: sllz + lgvd',
#     'zczc: 2',
#     'ptdq: humn - dvpt',
#     'dvpt: 3',
#     'lfqf: 4',
#     'humn: 5',
#     'ljgn: 2',
#     'sjmn: drzm * dbpl',
#     'sllz: 4',
#     'pppw: cczh / lfqf',
#     'lgvd: ljgn * ptdq',
#     'drzm: hmdt - zczc',
#     'hmdt: 32',
# ]

monkeys = {}
for line in lines:
    line = line.split(':')
    monkeys[line[0].strip()] = int(line[1].strip()) if line[1].strip().isnumeric() else line[1].strip().split()

# print(monkeys)


def get_monkey_number(monkey, monkey_jobs):
    if isinstance(monkey_jobs[monkey], int):
        return monkey_jobs[monkey]
    ops = {
        '-': lambda x,y: x-y,
        '+': lambda x,y: x+y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y
    }
    m1, op, m2 = monkey_jobs[monkey]
    return int(ops[op](get_monkey_number(m1, monkeys), get_monkey_number(m2, monkeys)))

print(get_monkey_number('root', monkeys))
