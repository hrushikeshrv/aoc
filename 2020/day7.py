"""
Problem 7 - https://adventofcode.com/2020/day/7

Part 1 - 
    Given a list of bag colors and a list of bag colors that are kept inside each bag, return how many distinct bags contain the shiny golden bag inside them at some depth

Part 2 -
    Given the same lists, start with the shiny golden bag and return the total number of bags inside the shiny golden bag
"""

#Set up the input
with open('input-07122020.txt', 'r') as file:
    rules = file.readlines()

#Define helper functions
def get_contents(rules):
    """
    From the list of rules about which bag contains which bag(s), returns a dictionary with a bag color as the key and a list of bags it contains as the value --
    
    for e.g. -

    red bags contain 1 black, 2 golden bag
    yellow bags contain 3 pink, 1 red bag
    golden bags contain no other bag

    is turned into this dictionary --

    {
        'red': [(1, 'black'), (2, 'golden')],
        'yellow': [(3, 'pink'), (1, 'red')],
        'golden': [('no', 'other')]
    }
    """
    contents = {}
    for rule in rules:
        _ = rule.split('contain')
        rule1 = ' '.join(_[0].split()[:-1])
        rule2 = _[1][:-1].strip().split(',')
        l = []
        l.append([])
        for bag in rule2:
            x = bag.split()
            l[-1].append((x[0], ' '.join(x[1:-1])))
            contents[rule1] = l[-1]
    return contents

bag_contents = get_contents(rules)

def bag_contains_target(bag_contents, bag, target):
    """
    Takes in the contents dictionary constructed in the last step, the bag (bag) to start from and the bag to search for (target) and searches for target starting from bag. Similar to DFS
    """
    #If the bag contains no other bags, return False
    if bag == 'other' or bag_contents[bag][0][1] == 'other':
        return False
    elif any(b[1] == target for b in bag_contents[bag]):
        return True
    #Otherwise, the bag is not empty and doesn't contain the target bag immediately, go one level deeper
    else:
        return any(bag_contains_target(bag_contents, b[1], target) for b in bag_contents[bag])

#Solution to part 1
def solve_1(bag_contents):
    n = 0
    for bag in bag_contents.keys():
        if bag_contains_target(bag_contents, bag, 'shiny gold'):
            n += 1
    return n

ans_1 = solve_1(bag_contents)
print(ans_1)
#Answer was 103