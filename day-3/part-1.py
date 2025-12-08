import sys

filename = ""

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("No file specified. Quitting.")
    quit()


def find_max(number: str):
    max_num = 0
    max_idx = 0

    for idx, ch in enumerate(number):
        digit = int(ch)

        if digit > max_num:
            max_num = digit
            max_idx = idx

    return (max_idx, max_num)


def get_joltage(number: str):
    (first_idx, first_max) = find_max(number)

    number_length = len(number)

    if first_idx == number_length - 2:
        return int(number[first_idx:])
    elif first_idx == number_length - 1:
        (second_idx, second_max) = find_max(number[:number_length - 1])
        return second_max * 10 + first_max
    else:
        (second_idx, second_max) = find_max(number[first_idx + 1:])
        return first_max * 10 + second_max



def run():
    with open(filename) as file:
        total_joltage = 0

        for line in file:
            number = line.strip("\n")

            joltage = get_joltage(number)
            total_joltage += joltage

        return total_joltage


if __name__ == "__main__":
    joltage = run()
    print(joltage)
