import os
import time
import random
import msvcrt
from colors import color

WIDTH = 6
HEIGHT = 5
SYMBOLS = "☻♥♦♣♠•○♂♀♪♫►◄¶§▲▼0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

KEY_QUIT = "q"
KEY_UP = "w"
KEY_DOWN = "s"
KEY_LEFT = "a"
KEY_RIGHT = "d"
KEY_ACTION = " "

COLOR_CURSOR = "yellow"
COLOR_CELL = "grey"
COLOR_TEXT = "white"
COLOR_TEXT_HIGHLIGHT = "black"

WRONG_GUESS_DELAY = 1


def generate_field():
    unique_symbols = WIDTH * HEIGHT // 2
    symbols = list(SYMBOLS[:unique_symbols] * 2)

    random.shuffle(symbols)
    symbols = iter(symbols)

    field = []
    for _ in range(HEIGHT):
        row = []

        for _ in range(WIDTH):
            row.append(next(symbols))

        field.append(row)

    return field


def get_color(row, col, cursor_row, cursor_col):
    if col == cursor_col and row == cursor_row:
        return COLOR_CURSOR
    else:
        return COLOR_CELL

def get_text_color(row, col, cursor_row, cursor_col):
    if col == cursor_col and row == cursor_row:
        return COLOR_TEXT_HIGHLIGHT
    else:
        return COLOR_TEXT


def print_separators(separator, row_index, row_len, cursor_row, cursor_col):
    for col_index in range(row_len):
        cell_color = get_color(row_index, col_index, cursor_row, cursor_col)
        print(color(separator, bg=cell_color), end="")
        print(" ", end="")


def show_field(field, cursor_row, cursor_col, visible_cells):
    separator = "     "
    cell_template = "  {}  "

    for row_index, row in enumerate(field):
        print_separators(separator, row_index, len(row), cursor_row, cursor_col)
        print()

        for col_index, cell in enumerate(row):
            cell_color = get_color(row_index, col_index, cursor_row, cursor_col)
            text_color = get_text_color(row_index, col_index, cursor_row, cursor_col)
            if (row_index, col_index) in visible_cells:
                cell_value = cell
            else:
                cell_value = " "
            print(color(cell_template.format(cell_value), fg=text_color, bg=cell_color, style="bold"), end="")
            print(" ", end="")

        print()

        print_separators(separator, row_index, len(row), cursor_row, cursor_col)
        print()
        print()


def get_key():
    c = msvcrt.getch()
    c = chr(c[0])
    return c.lower()


def are_same(locations, field):
    [(row1, col1), (row2, col2)] = locations
    value1 = field[row1][col1]
    value2 = field[row2][col2]

    return value1 == value2


def main():
    field = generate_field()
    temp_visible_cells = []
    perm_visible_cells = []
    cursor_row = 0
    cursor_col = 0

    while True:
        os.system("cls")
        visible_cells = temp_visible_cells + perm_visible_cells
        show_field(field, cursor_row, cursor_col, visible_cells)

        if len(perm_visible_cells) == WIDTH * HEIGHT:
            print()
            print("You won!")
            return

        # Wrong guess entered
        if len(temp_visible_cells) == 2:
            time.sleep(WRONG_GUESS_DELAY)
            temp_visible_cells = []
            continue

        key = get_key()

        if key == KEY_QUIT:
            return
        elif key == KEY_UP:
            cursor_row = max(0, cursor_row - 1)
        elif key == KEY_DOWN:
            cursor_row = min(HEIGHT - 1, cursor_row + 1)
        elif key == KEY_LEFT:
            cursor_col = max(0, cursor_col - 1)
        elif key == KEY_RIGHT:
            cursor_col = min(WIDTH - 1, cursor_col + 1)
        elif key == KEY_ACTION:
            location = (cursor_row, cursor_col)
            temp_visible_cells.append(location)

            if len(temp_visible_cells) < 2:
                continue

            if are_same(temp_visible_cells, field):
                perm_visible_cells += temp_visible_cells
                temp_visible_cells = []


if __name__ == "__main__":
    main()
