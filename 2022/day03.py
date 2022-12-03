with open('input-03.txt.', 'r') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))

def solve1(lines):
    score = 0
    for line in lines:
        s1 = set(line[:len(line)//2])
        s2 = set(line[len(line)//2:])
        common = list(s2.intersection(s1))[0]
        if common.islower():
            _ = ord(common) - 96
        else:
            _ = ord(common) - 38
        score += _
    return score

ans = solve1(lines)
print(ans)
# Answer was 8085

def solve2(lines):
    i = 0
    score = 0
    while i < len(lines):
        group = lines[i:i+3]
        i += 3
        s1 = set(group[0])
        s2 = set(group[1])
        s3 = set(group[2])
        common = list(s1.intersection(s2).intersection(s3))[0]
        if common.islower():
            _ = ord(common) - 96
        else:
            _ = ord(common) - 38
        score += _
    return score

ans = solve2(lines)
print(ans)
# Answer was 2515
