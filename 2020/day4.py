"""
Problem 4 - https://adventofcode.com/2020/day/4

Part 1 -
    Given a set of passports and conditions for a passport to be valid, return the number of valid passports

Part 2 - 
    Same as part 1 with harder validity conditions
"""

#Set up the input
with open('input-04122020.txt', 'r') as file:
    lines = file.readlines()

#Preprocess the input, get passports into a list
def get_passports(l):
    #Initialize a list to contain all passports
    passports = []
    #We need a cache to keep track of when one passport ends and another one starts since they are inconsistently separated by spaces and newlines.
    cache = ''

    for line in l:
        #When we encounter a new line, we end the previous passport here, add it to our list of passports and start a new one
        if line == '\n':
            passports.append(cache)
            cache = ''
            continue
        else:
            cache += line
    #Append the last cache since that doesn't get appended inside the for loop
    passports.append(cache)
    return passports

#Clean the passports list of \ns. No return value, modifies the list given in-place.
def clean(p):
    for passport in range(len(p)):
        p[passport] = p[passport].replace('\n', ' ')
        p[passport] = p[passport].split()

passports = get_passports(lines)
clean(passports)

#Solution to part 1
def solve_1(l):
    checks = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    )
    valids = 0
    for passport in l:
        keys = [x.split(':')[0] for x in passport]
        #If all keys in checks are present in the keys for this passport, this passport is valid.
        if all(c in keys for c in checks):
            valids += 1
    
    return valids

ans_1 = solve_1(passports)
print(ans_1)
#Answer was 245

#Solution to part 2
def check_valid(d):
    """
    Takes in a passport as a dictionary and checks the validity of the keys in the passport
    """
    valid = True
    try:
        #If the birth year is not between 1920 and 2002, this passport is invalid
        if not 1920 <= int(d['byr']) <= 2002:
            valid = False
        #If the issue year is not between 2010 and 2020, this passport is invalid
        if not 2010 <= int(d['iyr']) <= 2020:
            valid = False
        #If the expiry year is not between 2020 and 2030, this passport is invalid
        if not 2020 <= int(d['eyr']) <= 2030:
            valid = False
        
        #If the height is in inches and is not between 59 to 76 inches, this passport is invalid
        if d['hgt'].endswith('in') and not 59 <= int(d['hgt'][:-2]) <= 76:
            valid = False
        #Else if the height is in cm and is not between 150 to 193 cm, this passport is invalid
        elif d['hgt'].endswith('cm') and not 150 <= int(d['hgt'][:-2]) <= 193:
            valid = False
        #Else if the hieght is not in cm and not in inches, this passport is invalid
        elif not d['hgt'].endswith('cm') and not d['hgt'].endswith('in'):
            valid = False
        
        #If the eye color is not one of these, this passport is invalid
        if d['ecl'] not in 'amb blu brn gry grn hzl oth'.split():
            valid = False
        #If the pid is not of length 9 or contains characters other than numbers, this passport is invalid
        if not len(d['pid']) == 9 or not d['pid'].isnumeric():
            valid = False
        
        #Check if the color hair color is in a valid hex format
        color = d['hcl']
        if color[0] != '#' or len(color) != 7:
            valid = False
        else:
            for c in color[1:]:
                if c not in '1234567890abcdef':
                    valid = False
                    break
    #If any of the keys above don't exist in the passport, the passport is invalid 
    except KeyError:
        valid = False
    
    return valid

def solve_2(l):
    checks = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    )
    valids = 0
    for passport in l:
        keys = [x.split(':')[0] for x in passport]
        values = [x.split(':')[1] for x in passport]
        
        p_dict = {keys[i]:values[i] for i in range(len(keys))}
        if check_valid(p_dict):
            valids += 1
    
    return valids

ans_2 = solve_2(passports)
print(ans_2)
#Answer was 133