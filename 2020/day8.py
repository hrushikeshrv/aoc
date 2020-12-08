"""
Problem 8 - https://adventofcode.com/2020/day/8

Part 1 -
    Given some assembly instructions that have an infinite loop, find the value of the accumulator before the infinite loop starts

Part 2 -
    Fix the infinite loop be replacing 1 jmp instruction by an nop instruction or vice versa and return the value of the accumulator
"""

#Set up the input
with open('input-08122020.txt', 'r') as file:
    instructions = file.readlines()

#Define helper functions
def will_terminate(inst):
    """
    Takes in assembly instructions and returns whether they will terminate
    """
    done_list = []
    i = 0
    while i not in done_list:
        if i >= len(inst):
            return True
        
        instruction = inst[i][:-1]
        if instruction.startswith('acc'):
            done_list.append(i)
            i += 1
        elif instruction.startswith('nop'):
            done_list.append(i)
            i += 1
        elif instruction.startswith('jmp'):
            done_list.append(i)
            i += int(instruction.split()[1])
    
    return len(done_list) == len(instructions)


#Solution to part 1
def solve_1(instructions):
    done_list = []
    i = 0
    acc = 0
    
    while i not in done_list:
        #If we jumped to some instruction out of the instruction list, stop and return the acc. (Second part solution)
        if i >= len(instructions):
            return acc
        #Clean the instruction
        instruction = instructions[i][:-1]
        #If it is an acc instruction, add it to the accumulator and the list of executed instructions and move on
        if instruction.startswith('acc'):
            acc += int(instruction.split()[1])
            done_list.append(i)
            i += 1
        #If it is a nop, add it to the list of executed instructions and move on
        elif instruction.startswith('nop'):
            done_list.append(i)
            i += 1
        #If it is a jump, add it to the list of executed instructions and jump
        elif instruction.startswith('jmp'):
            done_list.append(i)
            i += int(instruction.split()[1])
    #If the while loop terminated because we tried to execute and instruction twice, we ran into and infinite loop, stop and return the accumulator. (First part solution)
    return acc

ans_1 = solve_1(instructions)
print(ans_1)
#Answer was 2003

#Solution to part 2
def solve_2(instructions):
    """
    Brute force. Replace all jmp or nop instructions one by one and check if they will terminate. If yes, run the instructions and return the acc. Otherwise move on and replace the next jmp or nop instruction.
    """
    inst_replaced = []
    for replace in ['jmp', 'nop']:
        #For all instructions
        for inst in range(len(instructions)):
            #If the instruction is a jump or a nop, replace it
            if instructions[inst].startswith(replace) and inst not in inst_replaced:
                inst_replaced.append(inst)
                new_instructions = instructions[:]
                #Replace jmps with nops and nops with jmps, one instruction at a time
                if replace.startswith('jmp'):
                    new_instructions[inst] = 'nop +0\n'
                else:
                    new_instructions[inst] = 'jmp' + instructions[inst][3:]
                
                #Check if these replaced instructions will terminate
                if will_terminate(new_instructions):
                    #If yes, run them and return the acc
                    return solve_1(new_instructions)
                
ans_2 = solve_2(instructions)
print(ans_2)
#Answer was 1984