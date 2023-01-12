#!/usr/bin/env python
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="List contents of a directory.")
parser.add_argument('dir', nargs='?', default=os.getcwd(), type=Path, help="Directory path.")

arg = parser.parse_args()
dir_path_abs = arg.dir.resolve().absolute()

# print (f"This is the absolute path to current working directory {dir_path_abs}")

def listing_all_files(dir):
    for f in dir.iterdir():
        print(f.name)


if __name__ == '__main__':
    listing_all_files(dir_path_abs)

