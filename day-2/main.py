import sys

filename = ""

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("No file specified. Quitting.")
    quit()


def run(filename):
    invalid_ids = []

    with open(filename) as file:
        line = file.readline().strip("\n")
        id_ranges = line.split(",")

        for id_range in id_ranges:
            [start, stop] = id_range.split("-")

            for num in range(int(start), int(stop) + 1):
                str_num = str(num)

                length = len(str_num)

                for index in range(1, (length // 2) + 1):
                    substr = str_num[:index]

                    if length / index == float(str_num.count(substr)):
                        invalid_ids.append(num)
                        break

    print(sum(invalid_ids))


if __name__ == "__main__":
    run(filename)
