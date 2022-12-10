"""
Problem 14 - https://adventofcode.com/2021/day/14

Part 1 -
    Given a string and a list of pairs of characters to look for, look for all pairs of characters and substitute them
    using the rule specified. Do this 10 times and return the difference in count of the most frequent and least
    frequent letter

Part 2 -
    Given the same string and same setup, do the same process 40 times and return the same metric.
"""

# Set up the input
with open('inputs/input-14.txt', 'r') as file:
    starting_monomer = file.readline().strip()
    file.readline()
    _ = list(map(lambda x: x.strip(), file.readlines()))
    substitutions = {}
    for s in _:
        substitutions[s.split('->')[0].strip()] = s.split('->')[1].strip()


# Solution to part 1
def solve_1(monomer, subs):
    for i in range(10):
        new_monomer = ''
        for j in range(len(monomer)-1):
            new_monomer += monomer[j]
            if monomer[j:j+2] in subs:
                new_monomer += subs[monomer[j:j+2]]
        new_monomer += monomer[-1]
        monomer = new_monomer
    count = {}
    for char in monomer:
        count[char] = count.get(char, 0) + 1
    count_list = sorted([count[x] for x in count])
    return count_list[-1] - count_list[0]


ans = solve_1(starting_monomer, substitutions)
print(ans)
# Answer was 3048


# Solution to part 2
def solve_2(monomer, subs):
    pairs = {}
    for i in range(len(monomer)-1):
        pairs[monomer[i:i+2]] = pairs.get(monomer[i:i+2], 0) + 1
        
    count = {}
    for char in monomer:
        count[char] = count.get(char, 0) + 1
        
    for i in range(40):
        new_added_pairs = {}
        for key in pairs:
            if key in subs and pairs[key] > 0:
                _1 = key[0] + subs[key]
                _2 = subs[key] + key[1]
                new_added_pairs[_1] = new_added_pairs.get(_1, 0) + pairs[key]
                new_added_pairs[_2] = new_added_pairs.get(_2, 0) + pairs[key]
                count[subs[key]] = count.get(subs[key], 0) + pairs[key]
                pairs[key] -= pairs[key]
                
        for key in new_added_pairs:
            pairs[key] = pairs.get(key, 0) + new_added_pairs[key]
        
    count_list = sorted([count[x] for x in count])
    return count_list[-1] - count_list[0]


ans = solve_2(starting_monomer, substitutions)
print(ans)
# Answer was 3288891573057
