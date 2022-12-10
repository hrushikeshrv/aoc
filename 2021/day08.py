"""
Problem 8 - https://adventofcode.com/2021/day/8

Part 1 -
    Given a seven segment display and a random mapping of signals to segments, figure out how many 1s, 4s,
    7s, and 8s appear in the input

Part 2 -
    Given the same seven segment display and a random mapping of signals to segments, figure out which signal
    corresponds to which segment, decode numbers, and return the sum of all numbers
"""

# Set up the input
with open('inputs/input-08.txt', 'r') as file:
    signals = file.readlines()


# Solution to part 1
def solve_1():
    unique_digits = 0
    unique_lengths = {2, 4, 3, 7}
    for s in signals:
        _ = s.split(' | ')
        if len(_) < 2:
            continue
        digits = _[1].split()
        for d in digits:
            if len(d) in unique_lengths:
                unique_digits += 1
    return unique_digits


ans = solve_1()
print(ans)


# Define helper functions
segment_digit_map = {
    ('a', 'b', 'c', 'e', 'f', 'g'): '0',
    ('c', 'f'): '1',
    ('a', 'c', 'd', 'e', 'g'): '2',
    ('a', 'c', 'd', 'f', 'g'): '3',
    ('b', 'c', 'd', 'f'): '4',
    ('a', 'b', 'd', 'f', 'g'): '5',
    ('a', 'b', 'd', 'e', 'f', 'g'): '6',
    ('a', 'c', 'f'): '7',
    ('a', 'b', 'c', 'd', 'e', 'f', 'g'): '8',
    ('a', 'b', 'c', 'd', 'f', 'g'): '9',
}


def get_mapping_from_shuffled_digits(digits):
    digits = sorted(digits.split(), key=lambda x: len(x))
    # The segment x can be represented by the following
    candidates = {x: set() for x in 'abcdefg'}
    for d in digits:
        if len(d) == 2:
            candidates['c'] = set(d)
            candidates['f'] = set(d)
        elif len(d) == 3:
            candidates['a'] = set(d) - candidates['c']
        elif len(d) == 4:
            candidates['d'] = set(d) - candidates['c'] - candidates['a']
            candidates['b'] = set(d) - candidates['c'] - candidates['a']
        elif len(d) == 5:
            diff_set = set(d) - candidates['a'] - candidates['c']
            if len(diff_set) > 0:
                candidates['e'].update(diff_set)
                candidates['g'].update(diff_set)
    
    _ = set()
    _.update(set(digits[-1]) - set(digits[-2]))
    _.update(set(digits[-1]) - set(digits[-3]))
    _.update(set(digits[-1]) - set(digits[-4]))
    
    candidates['c'] = candidates['c'].intersection(_)
    candidates['d'] = candidates['d'].intersection(_)
    candidates['e'] = candidates['e'].intersection(_)
    
    while True:
        dirty = False
        for char in 'abcdefg':
            if len(candidates[char]) == 1:
                for key in candidates:
                    if key == char:
                        continue
                    else:
                        candidates[key] = candidates[key] - candidates[char]
            else:
                dirty = True
        if not dirty:
            break
    
    segment_map = {x: set() for x in 'abcdefg'}
    for key in candidates:
        for letter in candidates[key]:
            segment_map[letter].add(key)
    return segment_map


def get_digit_from_segments(segments, mapping):
    lit_segments = set()
    for s in segments:
        lit_segments.update(mapping[s])
    return segment_digit_map[tuple(sorted(tuple(lit_segments)))]


def get_number_from_segments(segments, mapping):
    n = ''
    for s in segments.split():
        n += get_digit_from_segments(s, mapping)
    return int(n)


# Solution to part 2
def solve_2(test_cases):
    total = 0
    for i in test_cases:
        _ = i.split(' | ')
        digits = _[0]
        number = _[1]
        mapping = get_mapping_from_shuffled_digits(digits)
        total += get_number_from_segments(number, mapping)
    return total


ans = solve_2(signals)
print(ans)
# Answer was 983026
