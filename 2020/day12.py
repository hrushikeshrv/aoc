"""
Problem 12 - https://adventofcode.com/2020/day/12

Part 1 -
    Given a list of directions, go to the directions and return the coordinates you reach

Part 2 -
    Given a waypoint and instructions to move towards the waypoint, return the coordinates you reach
"""

#Set up the input
with open('input-12122020.txt', 'r') as file:
    d = file.readlines()

directions = [(x[0], int(x[1:-1])) for x in d]

#Solution to part 1
def solve_1(directions):
    facing = 'E'
    pos = [0, 0]
    for d in directions:
        if d[0] == 'N':
            pos[1] += d[1]
        elif d[0] == 'S':
            pos[1] -= d[1]
        elif d[0] == 'E':
            pos[0] += d[1]
        elif d[0] == 'W':
            pos[0] -= d[1]
            
        elif d[0] == 'F':
            if facing == 'E':
                pos[0] += d[1]
            elif facing == 'W':
                pos[0] -= d[1]
            elif facing == 'N':
                pos[1] += d[1]
            elif facing == 'S':
                pos[1] -= d[1]
        
        elif d[0] == 'L':
            if d[1] == 90:
                if facing == 'E':
                    facing = 'N'
                elif facing == 'N':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'E'
            elif d[1] == 180:
                if facing == 'E':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'E'
                elif facing == 'N':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'N'
            elif d[1] == 270:
                if facing == 'E':
                    facing = 'S'
                elif facing == 'N':
                    facing = 'E'
                elif facing == 'W':
                    facing = 'N'
                elif facing == 'S':
                    facing = 'W'
        elif d[0] == 'R':
            if d[1] == 270:
                if facing == 'E':
                    facing = 'N'
                elif facing == 'N':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'E'
            elif d[1] == 180:
                if facing == 'E':
                    facing = 'W'
                elif facing == 'W':
                    facing = 'E'
                elif facing == 'N':
                    facing = 'S'
                elif facing == 'S':
                    facing = 'N'
            elif d[1] == 90:
                if facing == 'E':
                    facing = 'S'
                elif facing == 'N':
                    facing = 'E'
                elif facing == 'W':
                    facing = 'N'
                elif facing == 'S':
                    facing = 'W'
    
    return abs(pos[0]) + abs(pos[1])

ans_1 = solve_1(directions)
print(ans_1)
#Answer was 1482

#Solution to part 2
def solve_2(directions):
    #pos is now the position of the waypoint relative to the boat
    pos = [10, 1]
    boat = [0, 0]

    for d in directions:
        if d[0] == 'N':
            pos[1] += d[1]
        elif d[0] == 'S':
            pos[1] -= d[1]
        elif d[0] == 'E':
            pos[0] += d[1]
        elif d[0] == 'W':
            pos[0] -= d[1]
            
        elif d[0] == 'F':
            boat[0] += d[1]*pos[0]
            boat[1] += d[1]*pos[1]
        
        elif d[0] == 'L':
            if d[1] == 90:
                pos[0], pos[1] = -1*pos[1], pos[0]
            elif d[1] == 180:
                pos[0], pos[1] = -1*pos[0], -1*pos[1]
            elif d[1] == 270:
                pos[0], pos[1] = pos[1], -1*pos[0]
        
        elif d[0] == 'R':
            if d[1] == 270:
                pos[0], pos[1] = -1*pos[1], pos[0]
            elif d[1] == 180:
                pos[0], pos[1] = -1*pos[0], -1*pos[1]
            elif d[1] == 90:
                pos[0], pos[1] = pos[1], -1*pos[0]
        
    return abs(boat[0]) + abs(boat[1])

ans_2 = solve_2(directions)
print(ans_2)
#Answer was 48739