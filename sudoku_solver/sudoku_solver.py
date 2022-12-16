def num_used_in_row(sudoku_puzzle, row_index, num):
    for col in range(0, len(sudoku_puzzle[row_index])):  # pylint: disable=consider-using-enumerate
        if sudoku_puzzle[row_index][col] == num:
            return True

    return False


def num_used_in_col(sudoku_puzzle, row_index, num):
    for col in range(0, len(sudoku_puzzle[row_index])):
        if sudoku_puzzle[col][row_index] == num:
            return True

    return False


def num_used_in_sub_groups(sudoku_puzzle, row_index, num):
    pass


def solve_sudoku_puzzle(sudoku_puzzle):
    pass
