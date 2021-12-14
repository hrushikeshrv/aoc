"""
Problem 14
"""

# Set up the input
with open('input-14.txt', 'r') as file:
    starting_monomer = file.readline().strip()
    file.readline()
    _ = list(map(lambda x: x.strip(), file.readlines()))
    substitutions = {}
    for s in _:
        substitutions[s.split('->')[0].strip()] = s.split('->')[1].strip()

with open('input-14-test.txt', 'r') as file:
    test_starting_monomer = file.readline().strip()
    file.readline()
    _ = list(map(lambda x: x.strip(), file.readlines()))
    test_substitutions = {}
    for s in _:
        test_substitutions[s.split('->')[0].strip()] = s.split('->')[1].strip()


# Solution to part 1
def solve_1(monomer, subs):
    for i in range(1):
        matched_pairs = []
        for j in range(len(monomer)):
            if monomer[j:j+2] in subs:
                matched_pairs.append((j, monomer[j:j+2]))
        new_monomer = ''
        matched_pairs = matched_pairs[::-1]
        j = 0
        while True:
            if j == len(monomer):
                break
            if matched_pairs and j == matched_pairs[-1][0]:
                pair = matched_pairs.pop()
                new_monomer += monomer[j]
                j += 1
                new_monomer += subs[pair[1]]
            new_monomer += monomer[j]
            j += 1
        monomer = new_monomer
    return monomer


ans = solve_1(test_starting_monomer, test_substitutions)
print(ans)
