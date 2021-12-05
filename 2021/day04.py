"""
Problem 4 - https://adventofcode.com/2021/day/4

Part 1 -
    Given a list of bingo boards and the order in which numbers are drawn, find the board that will win first
    and return a score

Part 2 -
    Find the last board that will win and return its score
"""

# Set up the input
with open('input-04.txt', 'r') as file:
    lines = file.readlines()
    draws = lines[0].split(',')
    boards = []
    curr_board = []
    for line in lines[2:]:
        if line == '\n':
            boards.append(curr_board)
            curr_board = []
            continue
        curr_board.append(line.split())


# Define helper functions
def has_bingo(board):
    """
    Checks if a board has won by checking if all of a particular row or column has None values.
    :param board: List[List[str]]
    :return: bool
    """
    # Assume the dimension of the board to be 5x5 (given)
    for row in board:
        if all([x is None for x in row]):
            return True
    
    for i in range(5):
        col = [x[i] for x in board]
        if all([x is None for x in col]):
            return True
    
    return False


def update_boards(number):
    """
    Updates all boards and replaces the drawn number with None
    :param number: int
    :return: None
    """
    number = int(number)
    for board in boards:
        for row in board:
            for i in range(len(row)):
                if row[i] is None:
                    continue
                if int(row[i]) == number:
                    row[i] = None


def get_board_score(board):
    """
    Calculates the score of the winning board as per the rules of the problem
    :param board: List[List[str]]
    :return: int
    """
    score = 0
    for row in board:
        for num in row:
            if num is not None:
                score += int(num)
    return score
    

# Solution to part 1
def solve_1(boards, draws):
    board_won = False
    i = 0
    while not board_won:
        drawn_number = int(draws[i])
        i += 1
        # print(f'Drawing {drawn_number}')
        update_boards(drawn_number)
        for board in boards:
            if has_bingo(board):
                return get_board_score(board) * drawn_number


ans = solve_1(boards, draws)
print(ans)
# Answer was 8580


# Solution to part 2
def solve_2():
    n_boards_won = 0
    last_winning_board = None
    i = 0
    # This is bad time complexity but anyway
    while n_boards_won < len(boards)-1:
        drawn_number = int(draws[i])
        i += 1
        update_boards(drawn_number)

        n_boards_won = 0
        for board in boards:
            if has_bingo(board):
                n_boards_won += 1
            else:
                last_winning_board = board
    new_draws = draws[i:]
    new_boards = [last_winning_board]
    return solve_1(new_boards, new_draws)


ans = solve_2()
print(ans)
# Answer was 9576
