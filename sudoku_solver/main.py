import os
from colorama import Fore, Style


def clean_screen():
    os.system("cls")


def print_sudoku_puzzle(sudoku_puzzle):
    clean_screen()
    for index, row in enumerate(sudoku_puzzle):
        if index == 0:
            print(f"{Fore.RED}-{Style.RESET_ALL}"*37)
        else:
            print("-"*37)
        print(f"{Fore.RED}|{Style.RESET_ALL} ", end = '')
        print(" | ".join(map(str, row)).replace("0","\u2666"), end = '')
        print(f" {Fore.RED}|{Style.RESET_ALL}")
    print(f"{Fore.RED}-{Style.RESET_ALL}"*37)


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

    print_sudoku_puzzle(sudoku_puzzle)


if __name__ == "__main__":
    main()
