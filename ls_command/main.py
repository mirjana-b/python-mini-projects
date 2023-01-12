#!/usr/bin/env python
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="List contents of a directory.")
parser.add_argument('dir', nargs='?', default=os.getcwd(), type=Path, help="Directory path.")

arg = parser.parse_args()
dir_path_abs = arg.dir.resolve().absolute()

print (f"This is the absolute path to current working directory {dir_path_abs}")

"Implemente a proof of concept"