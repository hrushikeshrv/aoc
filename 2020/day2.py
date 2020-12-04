"""
Problem 1 - https://adventofcode.com/2020/day/2

Part 1 -
    Given a list of password and conditions the passwords have to fulfill, return the number of passwords that fulfill the conditions 

Part 2 -
    Same as part 1 with different conditions
"""

#Set up the input
with open('input-02122020.txt', 'r') as file:
    s = file.readlines()


#Solution to part 1
def valid_1(password, lower, upper, letter):
    """
    Takes in a password and checks if it is valid
    """

    l_count = 0
    for char in password:
        if char == letter:
            l_count += 1

    if int(lower) <= l_count <= int(upper):
        return 1
    else:
        return 0

def solve_1(passw):
    valid = 0
    for p in passw:
        password = p.split()[-1]
        lower = p.split('-')[0]
        upper = p.split()[0].split('-')[-1]
        letter = p.split(':')[0][-1]

        valid += valid_1(password, lower, upper, letter)
    
    return valid

ans_1 = solve_1(s)
print(ans_1)
#Answer was 418

#Solution to part 2
def valid_2(password, lower, upper, letter):
    """
    Takes in a password and checks if it is valid
    """
    if password[lower] == letter and password[upper] != letter:
        return 1
    elif password[lower] != letter and password[upper] == letter:
        return 1
    else:
        return 0

def solve_2(passw):
    valid = 0
    for p in passw:
        password = p.split()[-1]
        lower = int(p.split('-')[0]) - 1
        upper = int(p.split()[0].split('-')[-1]) - 1
        letter = p.split(':')[0][-1]

        valid += valid_2(password, lower, upper, letter)
    
    return valid

ans_2 = solve_2(s)
print(ans_2)
#Answer was 616