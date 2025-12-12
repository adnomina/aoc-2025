import sys


def get_scroll_count(grid, row, col):
    scrolls = 0

    for y in range(row - 1, row + 2):
        if y < 0 or y > len(grid) - 1:
            continue

        for x in range(col - 1, col + 2):
            if x < 0 or x > len(grid[row]) - 1:
                continue

            if x == col and y == row:
                continue


            if grid[y][x] == "@":
                scrolls += 1

    return scrolls


def create_grid(filename):
    grid = []

    with open(filename) as file:
        for line in file:
            grid.append(line.strip("\n"))

    return grid


def get_accessible_scrolls(grid):
    accessible_scrolls = 0
    next_grid = []

    for row in range(len(grid)):
        shelf = ""

        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                shelf += "."
                continue

            if get_scroll_count(grid, row, col) < 4:
                accessible_scrolls += 1
                shelf += "."
            else:
                shelf += "@"

        next_grid.append(shelf)

    if accessible_scrolls == 0:
        return 0

    return accessible_scrolls + get_accessible_scrolls(next_grid)


def main():
    if len(sys.argv) != 2:
        print("No file specified. Quitting.")
        quit()

    filename = sys.argv[1]

    grid = create_grid(filename)

    accessible_scrolls = get_accessible_scrolls(grid)

    return accessible_scrolls


if __name__ == "__main__":
    print(main())
