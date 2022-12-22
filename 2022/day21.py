with open('inputs/input-21.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

monkeys = {}
for line in lines:
    line = line.split(':')
    monkeys[line[0].strip()] = int(line[1].strip()) if line[1].strip().isnumeric() else line[1].strip().split()


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


def get_human_expression(monkey, monkey_jobs):
    if monkey == 'humn':
        return 'H'
    if monkey == 'root':
        m1, _, m2 = monkey_jobs[monkey]
        return f'{get_human_expression(m1, monkey_jobs)} = {get_human_expression(m2, monkey_jobs)}'
    if isinstance(monkey_jobs[monkey], int):
        return monkey_jobs[monkey]
    m1, op, m2 = monkey_jobs[monkey]
    return f'({get_human_expression(m1, monkey_jobs)} {op} {get_human_expression(m2, monkey_jobs)})'

print(get_human_expression('root', monkeys))
# Pasted this equation into an online equation solver to get the answer,
# instead of implementing an equation solver - https://www.mathpapa.com/equation-solver/
