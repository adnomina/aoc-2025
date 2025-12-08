import sys

filename = ""

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("No file specified. Quitting.")
    quit()


def find_remaining_digits(number: str, remaining_digits: int) -> str:
    if remaining_digits == 0:
        return ""
    elif remaining_digits == len(number):
        return number

    max_num = 0
    max_idx = 0
    possible_range = range(len(number) - remaining_digits, -1, -1)

    for idx in possible_range:
        digit = int(number[idx])

        if digit >= max_num:
            max_num = digit
            max_idx = idx

    return str(max_num) + find_remaining_digits(number[max_idx + 1:], remaining_digits - 1)


def run():
    with open(filename) as file:
        total_joltage = 0

        for line in file:
            number = line.strip("\n")

            total_joltage += int(find_remaining_digits(number, 12))

        return total_joltage


if __name__ == "__main__":
    total_joltage = run()
    print(total_joltage)
