#!/usr/bin/env python
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="List contents of a directory.")
parser.add_argument('dir', nargs='?', default=os.getcwd(), type=Path, help="Directory path.")
parser.add_argument('-a', '--all', action = "store_true" ,help="Show everything, including hidden items.")
args = parser.parse_args()
dir_path_abs = args.dir.resolve().absolute()
show_all = args.all

def list_visible_files(directory):
    for f in directory.iterdir():
        if f.name[0]!='.':
            print (f.name)

def list_hidden_files(directory):
    for f in directory.iterdir():
        print(f.name)

def main():
    if show_all:
        list_hidden_files(dir_path_abs)
    else:
        list_visible_files(dir_path_abs)


if __name__ == '__main__':
    main()

