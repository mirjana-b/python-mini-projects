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

def listing_all_files(directory, show_hidden_files):
    for f in directory.iterdir():
        if show_hidden_files:
            print(f.name)
        else:
            if f.name[0]!='.':
                print (f.name)


if __name__ == '__main__':
    listing_all_files(dir_path_abs, show_all)
