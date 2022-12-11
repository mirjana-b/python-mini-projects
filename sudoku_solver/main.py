import os
from colorama import Fore, Style
from sudoku_solver import sudoku_solver


def clean_screen():
    os.system("cls")


def print_sudoku_puzzle(sudoku_puzzle):
    clean_screen()
    puzzle_width_chars = 37

    for index, row in enumerate(sudoku_puzzle):
        border = "|"
        emphasized_border = f"{Fore.RED}{border}{Style.RESET_ALL}"

        if index in (0,3,6):
            print(f"{Fore.RED}-{Style.RESET_ALL}"*puzzle_width_chars)
        else:
            cell_width = 11
            print(("-"*cell_width).join([emphasized_border] * 4))

        cell_width = 3
        row_symbols = [str(num) if num > 0 else " " for num in row]
        cell_groups = [row_symbols[i:i+cell_width]
                       for i in range(0, len(row_symbols), cell_width)]
        cell_strings = [" | ".join(map(str, group)) for group in cell_groups]
        row_string = f" {emphasized_border} ".join(cell_strings)

        print(f"{emphasized_border} {row_string} {emphasized_border}")

    print(f"{Fore.RED}-{Style.RESET_ALL}"*puzzle_width_chars)


def main():
    sudoku_puzzle = [
        [8,7,0,0,0,2,9,0,6],
        [0,9,0,8,0,0,0,0,0],
        [0,0,0,0,0,0,4,8,7],
        [2,6,0,0,5,0,0,0,9],
        [5,8,7,6,4,0,2,0,3],
        [0,4,9,7,0,0,0,0,0],
        [0,3,1,0,8,7,6,2,0],
        [0,0,0,0,6,4,3,0,1],
        [4,0,0,9,3,0,0,0,8]
    ]
    sudoku_solver(sudoku_puzzle)
    print_sudoku_puzzle(sudoku_puzzle)


if __name__ == "__main__":
    main()
