with open('inputs/input-01.txt') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))


def solve1(lines):
    calibration_val = 0
    for line in lines:
        n = ''
        for i in range(len(line)):
            if line[i].isnumeric():
                n += line[i]
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isnumeric():
                n += line[i]
                break
        calibration_val += int(n)
    return calibration_val


def solve2(lines):
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    calibration_val = 0
    for line in lines:
        print(f'Considering LINE {line}')
        n = ''
        found = False
        for i in range(len(line)):
            if found:
                break
            for j in range(1, len(line)-i+1):
                if j-i > 5:
                    break
                if line[i:i+j] in digits:
                    n += digits[line[i:i+j]]
                    found = True
                    break
                if line[i:i+j].isnumeric():
                    n += line[i:i+j]
                    found = True
                    break
        found = False
        for i in range(len(line)-1, -1, -1):
            if found:
                break
            for j in range(1, len(line)-i+1):
                if j-i > 5:
                    break
                if line[i:i+j] in digits:
                    n += digits[line[i:i+j]]
                    found = True
                    break
                if line[i:i+j].isnumeric():
                    n += line[i:i+j]
                    found = True
                    break
        calibration_val += int(n)
    return calibration_val


if __name__ == '__main__':
    # print(solve1(lines))
    print(solve2(lines))
