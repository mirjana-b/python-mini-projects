import os
from colorama import Fore, Style


def help_commands():
    os.system("cls")
    print(f"{Fore.GREEN}These are commands that you can choose:{Style.RESET_ALL}")
    print()
    print(f"{Fore.GREEN}n{Style.RESET_ALL} to read next page")
    print(f"{Fore.GREEN}p{Style.RESET_ALL} to read previous page")
    print(f"{Fore.GREEN}f{Style.RESET_ALL} together with word that you want to search for in text")
    print(f"{Fore.GREEN}q{Style.RESET_ALL} if you want to quit")
    print()
    input(f"{Fore.GREEN}Press any key to go back:{Style.RESET_ALL} ")
