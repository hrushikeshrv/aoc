with open('inputs/input-11.txt', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

lines = [
    'Monkey 0:',
    '  Starting items: 79, 98',
    '  Operation: new = old * 19',
    '  Test: divisible by 23',
    '    If true: throw to monkey 2',
    '    If false: throw to monkey 3',
    '',
    'Monkey 1:',
    '  Starting items: 54, 65, 75, 74',
    '  Operation: new = old + 6',
    '  Test: divisible by 19',
    '    If true: throw to monkey 2',
    '    If false: throw to monkey 0',
    '',
    'Monkey 2:',
    '  Starting items: 79, 60, 97',
    '  Operation: new = old * old',
    '  Test: divisible by 13',
    '    If true: throw to monkey 1',
    '    If false: throw to monkey 3',
    '',
    'Monkey 3:',
    '  Starting items: 74',
    '  Operation: new = old + 3',
    '  Test: divisible by 17',
    '    If true: throw to monkey 0',
    '    If false: throw to monkey 1',
]
lines = list(map(lambda x: x.strip(), lines))

current_monkey = None
monkey_dict = {}
monkey_attrs = {}
for line in lines:
    if not line:
        monkey_dict[current_monkey] = monkey_attrs
        monkey_attrs = {}
        continue
    if line.startswith('Monkey'):
        current_monkey = line.split()[1][:-1]
    elif line.startswith('Starting'):
        monkey_attrs['Starting items:'] = line.split(':')[-1].split(',')
    elif line.startswith('Operation'):
        monkey_attrs['Operation'] = line.split(':')[1].strip()
    elif line.startswith('Test'):
        monkey_attrs['Test'] = int(line.split()[-1])
    elif line.startswith('If true'):
        monkey_attrs['If true'] = line.split()[-1]
    elif line.startswith('If false'):
        monkey_attrs['If false'] = line.split()[-1]
monkey_dict[current_monkey] = monkey_attrs


def toss(monkeys, inspections, div_three=True):
    for m in monkeys:
        attrs = monkeys[m]
        for i in range(len(attrs['Starting items:'])):
            old = int(attrs['Starting items:'][i])
            new = old
            ldict = locals().copy()
            exec(attrs['Operation'], globals(), ldict)
            new = ldict['new']
            if div_three:
                new = int(new / 3)
            if new % attrs['Test'] == 0:
                dest_monkey = monkeys[attrs['If true']]
                dest_monkey['Starting items:'].append(new)
            else:
                dest_monkey = monkeys[attrs['If false']]
                dest_monkey['Starting items:'].append(new)
        inspections[m] = inspections.get(m, 0) + len(attrs['Starting items:'])
        attrs['Starting items:'] = []
        monkeys[m] = attrs


def solve1(monkeys):
    inspections = {i: 0 for i in monkeys}
    for i in range(20):
        toss(monkeys, inspections)
    _ = list(sorted(inspections.values()))
    return _[-1] * _[-2]


ans = solve1(monkey_dict)
print(ans)
# Answer was 50616


def solve2(monkeys):
    inspections = {i: 0 for i in monkeys}
    for i in range(1):
        toss(monkeys, inspections, False)
    for m in inspections:
        print(f'Monkey {m} inspected {inspections[m]} items.')
    _ = list(sorted(inspections.values()))
    return _[-1] * _[-2]


ans = solve2(monkey_dict)
print(ans)
