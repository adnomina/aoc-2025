import sys


def get_scroll_count(grid, row, col):
    scrolls = 0

    for yy in range(row - 1, row + 2):
        if yy < 0 or yy > len(grid) - 1:
            continue

        for xx in range(col - 1, col + 2):
            if xx < 0 or xx > len(grid[row]) - 1:
                continue

            if xx == col and yy == row:
                continue


            if grid[yy][xx] == "@":
                scrolls += 1

    return scrolls


def main():
    if len(sys.argv) != 2:
        print("No file specified. Quitting.")
        quit()

    filename = sys.argv[1]

    with open(filename) as file:
        grid = []

        for line in file:
            grid.append(line.strip("\n"))

        accessible_scrolls = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == ".":
                    continue

                if get_scroll_count(grid, row, col) < 4:
                    accessible_scrolls += 1

        print(accessible_scrolls)


if __name__ == "__main__":
    main()
