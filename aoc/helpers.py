"""
A collection of helper functions
"""


def get_neighbours(
    row: int, col: int, n_rows: int, n_cols: int
) -> list[tuple[int, int]]:
    """
    Takes a position in a grid and returns neighbors.
    Only considers up, down, left, and right.
    :param row: The row in the grid
    :param col: The column in the grid
    :param n_rows: The number of rows in the grid
    :param n_cols: The number of columns in the grid
    :return:
    """
    n = []
    if 0 < row:
        n.append((row - 1, col))
    if 0 < col:
        n.append((row, col - 1))
    if row < n_rows - 1:
        n.append((row + 1, col))
    if col < n_cols - 1:
        n.append((row, col + 1))
    return n


def inside_grid(row: int, col: int, n_rows: int, n_cols: int) -> bool:
    """
    Returns True if the passed row and column is inside the grid
    :param row: The row in the grid
    :param col: The column in the grid
    :param n_rows: The number of rows in the grid
    :param n_cols: The number of columns in the grid
    :return: True if the passed row and column is inside the grid
    """
    return 0 <= row < n_rows and 0 <= col < n_cols
